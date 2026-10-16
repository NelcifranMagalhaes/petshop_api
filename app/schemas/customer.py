
from sqlmodel import SQLModel

class CustomerCreate(SQLModel):
    name: str
    phone: str | None = None
    pets: str | None = None


class CustomerRead(SQLModel):
    id: int
    name: str
    phone: str | None
    pets: str | None