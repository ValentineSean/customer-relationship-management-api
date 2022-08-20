from redis_om import JsonModel, Migrator

class Issue(JsonModel):
    subject: str
    description: str
    handlers: list
    issue_status: str
    created_at: str

Migrator().run()