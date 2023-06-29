from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from src.config import config


def get_web_client(token: str):
    return WebClient(token=token)


def verify_auth_token(token: str):
    try:
        client = get_web_client(token)
        response = client.oauth_v2_access(
            client_id=config.SLACK_CLIENT_ID,
            client_secret=config.SLACK_CLIENT_SECRET,
            code=token,
        )
        return response
    
    except SlackApiError as e:
        return {"error": e}
    

def get_user_info(user_token: str, user_id: str):
    try:
        client = get_web_client(user_token)
        response = client.users_info(
            user=user_id,
        )
        return response
    
    except SlackApiError as e:
        return {"error": e}