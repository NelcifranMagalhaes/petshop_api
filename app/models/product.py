from sqlmodel import Field, Relationship
from decimal import Decimal
from app.models.timestamp_model import TimestampModel

class Product(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    description: str | None = None
    price: Decimal = Field(max_digits=10, decimal_places=2)
    stock_quantity: int = 0

    sale_items: list["SaleItem"] = Relationship(
        back_populates="product"
    )