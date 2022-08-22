from redis_om import JsonModel, Migrator, Field

class Issue(JsonModel):
    subject: str = Field(index=True)
    description: str = Field(index=True)
    issue_status: str = Field(index=True)
    sender: str = Field(index=True)
    created_at: str = Field(index=True)
    record_status: str = Field(index=True)

    def __new__(cls, subject, description, issue_status, sender, created_at, record_status, pk="ID", db_write=None):
        if db_write:
            return super().__new__(cls)

        else:
            return {
                "pk": pk,
                "subject": subject,
                "description": description,
                "issue_status": issue_status,
                "sender": sender,
                "created_at": created_at,
                "record_status": record_status
            }

Migrator().run()