from redis_om import JsonModel, Migrator

class User(JsonModel):
    first_name: str
    last_name: str
    role: str
    created_at: str

Migrator().run()