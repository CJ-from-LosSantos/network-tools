import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/initialize")
async def initialize(callback_url: str):
    body = {"url": callback_url}
    return requests.post("http://127.0.0.1:30001/ConfigureMsgRecive", json=body).json()


@app.post("/recive_msg")
async def recive_msg(body: dict):
    print(body)
    return body
