from sqlmodel import Field, Relationship
from decimal import Decimal
from app.models.timestamp_model import TimestampModel
from app.models.product import Product
from app.models.sale import Sale

class SaleItem(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    sale_id: int = Field(foreign_key="sale.id")
    product_id: int = Field(foreign_key="product.id")

    quantity: int
    unit_price: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    subtotal: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    sale: Sale = Relationship(back_populates="items")
    product: Product = Relationship(back_populates="sale_items")