# EventStreams Streaming demo

This is a small example of how one can stream over EventStreams. In this example a video is sent from a producer to the consumer that will 
display the video using Flask. 

The example is based on: https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd

To run:

1. Set up IBM Event Streams (Lite will do fine)
2. Create a topic (in this example "video-demo")
3. Create credentials and note the bootstrap servers (you only need one of them), username and password
4. Alter the bootstrap server lines in the code with your bootstrap server(s)
5. set the environment variables USERNAME and PASSWORD accordingly
6. In a virtual environment, run "pip install -r requirements.txt"
7. Find a small mp4 clip and place in the directory. Name it video.mp4
8. Run the producer: python producer.py
9. Run the consumer: FLASK_APP=consumer.py flask run
10. Surf into http://127.0.0.1:5000 and enjoy :)



