import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.environ.get("MONGO_DETAILS")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")

try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
except ValueError:
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
