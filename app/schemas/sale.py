from datetime import datetime
from decimal import Decimal

from sqlmodel import Field, SQLModel


class SaleItemCreate(SQLModel):
    product_id: int
    quantity: int


class SaleCreate(SQLModel):
    customer_id: int
    sale: list[SaleItemCreate] = Field(..., min_length=1)


class SaleItemRead(SQLModel):
    id: int
    sale_id: int
    product_id: int
    quantity: int
    unit_price: Decimal
    subtotal: Decimal


class SaleRead(SQLModel):
    id: int
    customer_id: int
    sale_date: datetime
    total_amount: Decimal
    items: list[SaleItemRead] = Field(default_factory=list)