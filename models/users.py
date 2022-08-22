from ast import alias
from redis_om import JsonModel, Migrator, Field

class User(JsonModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    role: str = Field(index=True)
    created_at: str = Field(index=True)

    # def __init__(self, first_name, last_name, role, created_at):
        # super().__init__()
        # pass
        # return self
        # self.first_name = first_name
        # self.last_name = last_name
        # self.role = role
        # self.created_at = created_at

    def __new__(cls, first_name, last_name, role, created_at, pk="ID", db_write=None):
        if db_write:
            return super().__new__(cls)

        else:
            return {
                "pk": pk,
                "first_name": first_name,
                "last_name": last_name,
                "role": role,
                "created_at": created_at
            }

Migrator().run()