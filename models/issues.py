from redis_om import JsonModel, Migrator, Field, EmbeddedJsonModel
from typing import Optional

class Issue(EmbeddedJsonModel, JsonModel):
    subject: Optional[Optional[str]] = Field(index=True)
    description: Optional[str] = Field(index=True)
    issue_status: Optional[str] = Field(index=True)
    sender: Optional[str] = Field(index=True)
    created_at: Optional[str] = Field(index=True)
    record_status: Optional[str] = Field(index=True)

    # def __new__(cls, subject, description, issue_status, sender, created_at, record_status, pk="ID", db_write=None):
    #     if db_write:
    #         return super().__new__(cls)

    #     else:
    #         return {
    #             "pk": pk,
    #             "subject": subject,
    #             "description": description,
    #             "issue_status": issue_status,
    #             "sender": sender,
    #             "created_at": created_at,
    #             "record_status": record_status
    #         }

Migrator().run()