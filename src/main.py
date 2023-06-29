import requests
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


from src.db import create_tables, get_db
from src.models import UserSlackInfo
from src.utils import verify_auth_token, get_user_info

app = FastAPI()
create_tables()


@app.get("/")
async def health_check():
    return {"message": "Server is up and running!"}


@app.get("/slack")
async def slack(code: str = None, db: Session = Depends(get_db)):
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
            # save user_email and webhook_url to db as a new row in user_slack_info table
            try:    
                new_user_slack_info = UserSlackInfo(email=user_email, slack_webhook_url=webhook_url)
                user_slack_info_objs = db.query(UserSlackInfo).where(UserSlackInfo.email == new_user_slack_info.email)

                if user_slack_info_objs.first() is None:
                    db.add(new_user_slack_info)
                else:
                    db.update(new_user_slack_info)
                db.commit()
                db.refresh(new_user_slack_info)
                return {"message": "Success!"}
            except Exception as e:
                return {"error": e.__str__()}
            finally:
                db.rollback()
                db.close()
        return auth_response
    
    return {"error": "No authtoken provided!"}