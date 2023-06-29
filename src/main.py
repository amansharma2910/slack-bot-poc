from fastapi import FastAPI, Request

import requests

from .utils import verify_auth_token, get_user_info

app = FastAPI()


@app.get("/")
async def health_check():
    return {"message": "Server is up and running!"}


@app.get("/slack")
async def slack(code: str = None):
    if code is not None:
        auth_response = verify_auth_token(code)
        if "error" not in auth_response:
            if "incoming_webhook" in auth_response:
                webhook_url = auth_response.get("incoming_webhook").get("url")
                requests.post(webhook_url, json={"text": "Test succeeded!"}, headers={"Content-Type": "application/json"})

            if "authed_user" in auth_response:
                user = auth_response.get("authed_user")
                user_id = user.get("id")
                user_token = user.get("access_token")
                user_info = get_user_info(user_token, user_id)
                user_email = user_info.get("user").get("profile").get("email")
            return {"message": "Success!"}
        return auth_response
    
    return {"error": "No authtoken provided!"}