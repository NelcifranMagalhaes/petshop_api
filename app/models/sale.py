
from sqlmodel import SQLModel, Field, Relationship, text
from datetime import datetime
from decimal import Decimal
from app.models.timestamp_model import TimestampModel
from app.models.customer import Customer


class Sale(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    customer_id: int = Field(foreign_key="customer.id")
    sale_date: datetime = Field(default_factory=datetime.astimezone)

    total_amount: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    customer: Customer = Relationship(back_populates="sales")

    items: list["SaleItem"] = Relationship(
        back_populates="sale"
    )