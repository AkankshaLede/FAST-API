from pydantic import BaseModel , ConfigDict ,Field
from uuid import uuid4,UUID

class Application(BaseModel):
    display_name:str
    short_code:str
    description:str
    domain:str
    account_id:UUID= Field(default_factory=uuid4)
    icon_uri:str
    