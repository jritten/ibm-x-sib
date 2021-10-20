from flask import Flask, Response, redirect
from confluent_kafka import Consumer
import certifi
import os
import random
import string

topic = "IBM-SiB"

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
brokers = os.environ.get("BROKERS") or "broker-5-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-3-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-2-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-1-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-0-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-4-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093"


consumer_group = "default"

# Set the Flask App
app = Flask(__name__)


@app.route('/')
def redirect_to_video():
    consumer_group = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    print("Redirecting to: "+consumer_group)
    return redirect("/video/"+consumer_group)

@app.route('/video/<id>', methods=['GET'])
def video(id):
    """
    This is the heart of our video display. Notice we set the mimetype to 
    multipart/x-mixed-replace. This tells Flask to replace any old images with 
    new values streaming through the pipeline.
    """
    # Start up consumer
    conf = {
        'bootstrap.servers': brokers,
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': certifi.where(),
        'sasl.mechanism': 'PLAIN',
        'sasl.username': username,
        'sasl.password': password,
        'group.id': id,
        'default.topic.config': {
                            'enable.auto.commit': 'true',
                            'auto.offset.reset': 'latest'
                        }
    }
    consumer = Consumer(**conf)
    consumer.subscribe([topic])

    return Response(
        get_video_stream(consumer),
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream(consumer):
    """
    Here is where we recieve streamed images from the Kafka Server and convert 
    them to a Flask-readable format.
    """
    meta = False
    while True:
        if not meta:
            yield(b'<meta http-equiv="refresh" content="300">\n')
            meta = True
        else:
            msg = consumer.poll()
            if msg is not None:
                yield (b'--frame\r\n' + b'Content-Type: image/jpg\r\n\r\n' + msg.value() + b'\r\n\r\n')