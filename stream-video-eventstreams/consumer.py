from flask import Flask, Response
from confluent_kafka import Consumer
import certifi
import os

topic = "video-demo"

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

# Start up consumer
conf = {
    'bootstrap.servers': "broker-5-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-3-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-2-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-1-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-0-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-4-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093",
    'security.protocol': 'SASL_SSL',
    'ssl.ca.location': certifi.where(),
    'sasl.mechanism': 'PLAIN',
    'sasl.username': username,
    'sasl.password': password,
    'group.id': 'videolistener-1',
    'default.topic.config': {
                        'enable.auto.commit': 'true',
                        'auto.offset.reset': 'latest'
                    }
}
consumer = Consumer(**conf)
consumer.subscribe([topic])


# Set the Flask App
app = Flask(__name__)

@app.route('/', methods=['GET'])
def video():
    """
    This is the heart of our video display. Notice we set the mimetype to 
    multipart/x-mixed-replace. This tells Flask to replace any old images with 
    new values streaming through the pipeline.
    """
    return Response(
        get_video_stream(), 
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
    """
    Here is where we recieve streamed images from the Kafka Server and convert 
    them to a Flask-readable format.
    """
    while True:
        msg = consumer.poll()
        if msg is not None:
            yield (b'--frame\r\n' + b'Content-Type: image/jpg\r\n\r\n' + msg.value() + b'\r\n\r\n')