import os

from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")


HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}


