from pydantic import BaseModel, EmailStr

class UserSlackInfoSchema(BaseModel):
    email: EmailStr
    slack_webhook_url: str

    class Config:
        orm_mode = True