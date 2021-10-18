# EventStreams Streaming demo

This is a small example of how one can stream over EventStreams. In this example a video from your internal camera is sent from a producer to the consumer that will 
display the video using Flask. 

The example is based on: https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd

To run without docker

1. Set up IBM Event Streams (Lite will do fine)
2. Create a topic (in this example "video-demo")
3. Create credentials and note the bootstrap servers (you only need one of them), username and password
4. Alter the bootstrap server lines in the code with your bootstrap server(s)
5. set the environment variables USERNAME and PASSWORD accordingly
6. In a virtual environment, run "pip install -r requirements.txt"
7. Run the producer: python producer.py
8. Run the consumer: FLASK_APP=consumer.py flask run
9. Surf into http://127.0.0.1:5000 and enjoy :)

Docker version

1. - 7. as local version
8. build the docker: make consumer
9. run the docker: docker run --rm -e USERNAME=$USERNAME -e PASSWORD=$PASSWORD -p 8080:8080 event_consumer
10. Surf into http://127.0.0.1:8080 and enjoy :)



