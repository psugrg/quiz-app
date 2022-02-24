from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from random import randint

# This is a monolith application where everything is served by the FastApi even the index.html and other static files

# Back-end application

# This creates our FastAPI application
app = FastAPI()

# API


class Quiz(BaseModel):
    arg_1: int
    arg_2: int
    answer: int


@app.post("/answer/")
async def answer(answer: Quiz):
    if (answer.arg_1 + answer.arg_2) == answer.answer:
        print("Good answer!")
        return {"result": True}
    else:
        print("Wrong answer!")
        return {"result": False}


@app.get("/quiz")
async def quiz():
    return {"arg_1": randint(0, 10), "arg_2": randint(0, 10)}


######################################
# Create the front-end sub application
front = FastAPI()

# This line will serve the static files located in the ../public directory
# Since this is a simple "monolith" application we will serve the index.html file
# as well as some java script files
front.mount("/", StaticFiles(directory="../public", html=True), name="static")

# Connect the front-end sub application to the main application (back-end)
app.mount("/", front)
