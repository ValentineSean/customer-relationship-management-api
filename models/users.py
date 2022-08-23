from redis_om import JsonModel, Migrator, Field
from typing import Optional

class User(JsonModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    role: str = Field(index=True)
    created_at: str = Field(index=True)
    record_status: str = Field(index=True)

    # def __new__(cls, first_name=None, last_name="LASTNAME", role="ROLE", created_at="CREATEDAT", record_status="RECORDSTATUS", pk="ID", db_write=None):
    #     if db_write:
    #         return super().__new__(cls)

    #     else:
    #         return {
    #             "pk": pk,
    #             "first_name": first_name,
    #             "last_name": last_name,
    #             "role": role,
    #             "created_at": created_at,
    #             "record_status": record_status
    #         }

Migrator().run()