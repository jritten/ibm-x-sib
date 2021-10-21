# ibm-x-sib

## Workshop Prerequisites

1.  If you don't already have one, sign-up for an [IBM Cloud pay-as-you-go account](). We will only be using the free Lite Tier service instances for the workshop.

## IBM Event Streams Prerequisites

1. If you don't already have one, create an Event Streams service instance.

    a. Log in to the IBM Cloud console.

    b. Click the [Event Streams service](https://cloud.ibm.com/catalog/event-streams) in the Catalog.

    c. Select the Lite plan on the service instance page.

    d. Enter a name for your service. You can use the default value.

    e. Click Create. The Event Streams Getting started page opens.


2. If you don't already have them, install the following prerequisites:

    - [Git](https://git-scm.com/)
    - [Gradle](https://gradle.org/)
    - Java™ 8 or higher


# Setup the Service Instances and Credentials

## Create an Event Streams Service Instance

## Create a New Topic

## Create New Service Credentials


## [Clone the Repo](https://github.com/jritten/ibm-x-sib)

GitHub Repo: https://github.com/jritten/ibm-x-sib

  -- clone the repo --
$ git clone https://github.com/jritten/ibm-x-sib

  -- cd into stream-video-eventstreams --
$ cd stream-video-eventstreams


## Add the Service Credentials to the App

Add the Event Streams Service Credentials to the App.

  -- add username env var --
$ export USERNAME=”token”

  -- add password env var --
$ export PASSWORD=”<SERVICE_CREDENTIALS_PASSWORD>”

  -- add broker env var (first in list) --
$ export BROKERS=”<KAFKA_BROKERS_SASL[0]>”


# Run the App Locally w Docker

  -- build a docker image --
$ docker build . --tag event_consumer

  -- run the docker image --
$ docker run --rm -e BROKERS=$BROKERS -e USERNAME=$USERNAME -e PASSWORD=$PASSWORD -p 8080:8080 event_consumer

  -- view the app --
http://127.0.0.1:8080


# Run the App w Python3 VM

## Create Python3 VM

## Run the App in Python3 VM

## View the App

  -- view the app --
http://127.0.0.1:5000


# Push the Container Image to Docker Hub

```
  -- tag the docker image --
$ docker tag event_consumer <DOCKERHUB_REPO>/event_consumer:latest
```

  -- push the image to docker hub --
```
$ docker push <DOCKERHUB_REPO>/event_consumer:latest
```
-- copy the image location from the output --
```
$ The push refers to repository [docker.io/<DOCKERHUB_REPO>/event_consumer]
```

# Deploy the App to Code Engine

## Create a New Project

## Create a New App

Add the location of the container image in Docker Hub.
```
[docker.io/<DOCKERHUB_REPO>/event_consumer]
```

Select your Code Engine project.

Configure the Runtime.
Update the Max concurrency to “2”.

Add Environment Variables.
Add your environment variables as key-value pairs so Code Engine can inject them into the application for global use.
Add each key-value pair as a **Literal value**.

Deploy to Code Engine.
Click **Create**.


# View the Live App

## Watch the App Scale Up

## Watch the App Scale Down

Close all instances of the running application (close all the browser tabs where the application is currently running), and watch the application scale down to zero in the **Overview**.

## Auto-Scale the App w Code Engine

Share the App URL with others, and have them start instances of the running App in the browser. Watch Code Engine auto-scale the App based on incoming HTTP-requests in the **Overview**.


