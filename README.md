# Simple Quiz Application

A simple, monolith application using FastAPI framework that ask a question and verifies it.

This application has been created to learn the cloud application development in the simplest possible form.
This means that the application is a monolith and doesn't have any sophisticated logic behind it.

## Architecture

![Architecture diagram](/diagram.JPG)

## Docker

### Build

`docker build -t quiz-app .`

### Run

`docker run -dp 8080:8080 quiz-app`

## Todo's & Open Points

- Uvicorn is probably not a part of the application therefore it could be removed from the Poetry toml file
