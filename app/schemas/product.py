from decimal import Decimal

from sqlmodel import SQLModel


class ProductCreate(SQLModel):
    name: str
    description: str | None = None
    price: Decimal
    stock_quantity: int


class ProductRead(SQLModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int