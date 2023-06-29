import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()


def get_web_client(token: str):
    return WebClient(token=token)


def get_incoming_webhook(token: str):
    try:
        client = get_web_client(token)
        client_id = os.environ.get("SLACK_CLIENT_ID")
        client_secret = os.environ.get("SLACK_CLIENT_SECRET")
        response = client.oauth_v2_access(
            client_id=client_id,
            client_secret=client_secret,
            code=token,
        )
        webhook_url = response.get("incoming_webhook").get("url")
        return {"webhook_url": webhook_url}
    except SlackApiError as e:
        return {"error": e}
    