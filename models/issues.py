import datetime

from redis_om import HashModel

class Issue(HashModel):
    subject: str
    description: str
    handlers: str
    issue_status: str
    created_at: str