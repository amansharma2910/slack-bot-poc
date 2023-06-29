import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # slack envs
        self.SLACK_CLIENT_ID = os.environ.get("SLACK_CLIENT_ID")
        self.SLACK_CLIENT_SECRET = os.environ.get("SLACK_CLIENT_SECRET")
        
        # postgres envs
        self.POSTGRES_USER = os.environ.get("POSTGRES_USER")
        self.POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
        self.POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER", "localhost")
        self.POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
        self.POSTGRES_DB = os.environ.get("POSTGRES_DB")
        self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

config = Config()