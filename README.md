
This project is a Dockerized Weather API service.
It fetches real-time weather data for a given city using OpenWeather API.

## Weather API Used
OpenWeather API
https://openweathermap.org/api

## Required Environment Variables
API_KEY=f1228154cd3b2b357fc51a901dd6e702

## Build the Docker Image
docker build -t weather-service .

## Run the Container
docker run -d -p 8080:8080 -e API_KEY=f1228154cd3b2b357fc51a901dd6e702

## Test the Service
Open browser:
http://localhost:8080/weather?city=Gaza

Or using curl:
curl http://localhost:8080/weather?city=Gaza

## Stop the Container
docker ps
docker stop <container_id>
