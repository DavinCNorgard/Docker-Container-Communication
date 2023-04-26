# Docker-Container-Communication

This project contains two Docker containers that communicate with each other. The containers are named `client-1` and `server-1`. `server-1` conatains a flask server that provides a REST API for `client-1` to consume.
The server uses an open api to get current weather data for any latitude and longitude, and is able to return that info to the client apon request.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Run `docker-compose up` to start both containers.

## Usage

Once the server container is up and running, the client container should send a get request and print the servers response.
you can also access the REST API by making a request to 'http://localhost:5000/?latitude={lat}&longitude={lon}'. This will return a JSON response with a message constaining the weather data.
