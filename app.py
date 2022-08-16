import os
import json
import redis

from flask import Flask
from dotenv import load_dotenv

# Environment Variables
load_dotenv()

app = Flask(__name__)

redis_host = os.getenv("AZURE_REDIS_HOST")
redis_port = os.getenv("AZURE_REDIS_PORT")
redis_db = os.getenv("AZURE_REDIS_DB")
redis_password = os.getenv("AZURE_REDIS_PASSWORD")
redis_ssl = os.getenv("AZURE_REDIS_SSL")

redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    db=redis_db,
    password=redis_password,
    ssl=redis_ssl
)

@app.route("/")
def home():
    return "this is CRM home"

@app.route("/test")
def test():
    redis_client.set("name", "tom")
    return "testing CRM"