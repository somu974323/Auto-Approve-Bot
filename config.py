import os
from typing import List

API_ID = os.environ.get("API_ID", "23416113")
API_HASH = os.environ.get("API_HASH", "5f66046e7129c9bf6e2b3da943ae2993")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6662808885"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/svdv1VLq/photo-2025-07-15-11-45-09-7527273414256492548.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002778873953"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://vinod974323:mjaWnkUGHgteBwIo@cluster0.kb5ajhl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Goodmorning")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002778873953").split())) # Add Multiple channel ids
