from pydantic import BaseModel , ConfigDict ,Field
from uuid import uuid4,UUID

class Account(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name:str
    parent_account_id:str
    category:str
    type:str
    adress_line_1:str
    adress_line_2:str
    contact_name:str
    contact_email:str
    contact_phone:str
    