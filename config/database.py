import os
import redis
from dotenv import load_dotenv

# Environment Variables
load_dotenv()

redis_host = os.getenv("AZURE_REDIS_HOST")
redis_port = os.getenv("AZURE_REDIS_PORT")
redis_db = os.getenv("AZURE_REDIS_DB")
redis_password = os.getenv("AZURE_REDIS_PASSWORD")
redis_ssl = os.getenv("AZURE_REDIS_SSL")


# redis_credentials = {
#     "host": redis_host,
#     "password": redis_password,
#     "port": redis_port,
#     "db": redis_db,
#     "ssl": redis_ssl,
# }

redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    db=redis_db,
    password=redis_password,
    ssl=redis_ssl
)