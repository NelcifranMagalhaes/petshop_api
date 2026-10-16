from sqlmodel import Field, Relationship, text
from typing import TYPE_CHECKING
from app.models.timestamp_model import TimestampModel

if TYPE_CHECKING:
    from app.models.sale import Sale

class Customer(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    phone: str | None = None
    pets: str | None = None

    sales: list["Sale"] = Relationship(back_populates="customer")