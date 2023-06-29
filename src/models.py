from sqlalchemy import String, Column

from src.db import Base

class UserSlackInfo(Base):
    __tablename__ = "user_slack_info"
    email = Column(String, unique=True, index=True, primary_key=True)
    slack_webhook_url = Column(String, nullable=True)