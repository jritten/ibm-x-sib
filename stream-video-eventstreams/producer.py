import sys
import time
import cv2
from confluent_kafka import Producer
import certifi
import os

topic = "video-demo"

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]


def publish_video():

    # Start up producer
    conf = {
        'bootstrap.servers': "broker-5-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-3-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-2-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-1-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-0-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093,broker-4-3k507nvhhcbmm13z.kafka.svc08.us-south.eventstreams.cloud.ibm.com:9093",
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': certifi.where(),
        'sasl.mechanism': 'PLAIN',
        'sasl.username': username,
        'sasl.password': password,
    }
    producer = Producer(**conf)

    videofile = cv2.VideoCapture("video.mp4")
    
    try:
        print("Sending the frames")
        while(True):
            success, frame = videofile.read()
            frame = cv2.resize(frame,(320,200))  # Reduce the size of the frame so we get speed
            ret, buffer = cv2.imencode('.jpg', frame)
            producer.produce(topic, buffer.tobytes())          
            # Choppier stream, reduced load on processor
            time.sleep(0.2)
            
    except:
        producer.flush()
        print("\nExiting.")
        sys.exit(1)

    videofile.release()


if __name__ == '__main__':
    print("publishing video")
    publish_video()