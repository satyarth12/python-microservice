"""This file is for loading the env vars for the app
"""
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# AMPQ Broker
AMPQ_BROKER_URL = os.getenv("AMPQ_BROKER")

# DATABASE URI
DB_URI = os.getenv("DATABASE_URI")
