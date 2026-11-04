
from sqlmodel import Field, SQLModel

class CustomerCreate(SQLModel):
    name: str = Field(..., min_length=1)
    phone: str | None = None
    pets: str | None = None


class CustomerRead(SQLModel):
    id: int
    name: str
    phone: str | None
    pets: str | None