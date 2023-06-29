from fastapi import FastAPI, Request

import requests

from .utils import get_incoming_webhook

app = FastAPI()


@app.get("/")
async def health_check():
    return {"message": "Server is up and running!"}


@app.get("/slack")
async def slack(code: str = None):
    if code is not None:
        response = get_incoming_webhook(code)
        
        # check if webhook works
        if "webhook_url" in response:
            webhook_url = response.get("webhook_url")
            requests.post(webhook_url, json={"text": "Test succeeded!"}, headers={"Content-Type": "application/json"})
            return {"message": "Test succeeded!"}
        
        return response
    
    return {"error": "No authtoken provided!"}