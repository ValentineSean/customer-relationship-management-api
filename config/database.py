import os
import redis
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# Environment Variables
load_dotenv()

# MONGO
username = os.getenv("AZURE_USERNAME")
password = os.getenv("AZURE_PASSWORD")
host = os.getenv("AZURE_HOST")
port = os.getenv("AZURE_PORT")
database_name = os.getenv("AZURE_DATABASE_NAME")


database_credentials = {
    "username": username,
    "password": password,
    "host": host,
    "port": port,
    "database_name": database_name,
}

mongo = PyMongo()

# REDIS
username = os.getenv("AZURE_USERNAME")
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

redis_om_url = f"{username}:{password}@{redis_host}:{redis_port}/{redis_db}"