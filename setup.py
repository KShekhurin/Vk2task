import os
from dotenv import load_dotenv

load_dotenv()

SECRET_PASS = os.getenv('SECRET_PASS')
CONFIRMATION_RESPONSE = os.getenv('CONFIRMATION_RESPONSE')
ACCESS_CODE = os.getenv('ACCESS_CODE')