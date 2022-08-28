from redis_om import JsonModel, Migrator, Field
from typing import Optional

from models.users import User
from models.issues import Issue

class Message(JsonModel):
    issue: Optional[Optional[str]] = Field(index=True)
    sender: Optional[str] = Field(index=True)
    sender_data: User
    issue_data: Issue
    message_body: Optional[str] = Field(index=True)
    message_status: Optional[str] = Field(index=True)
    created_at: Optional[str] = Field(index=True)
    record_status: Optional[str] = Field(index=True)

Migrator().run()