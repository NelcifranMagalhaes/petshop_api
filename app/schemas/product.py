from decimal import Decimal

from sqlmodel import Field, SQLModel


class ProductCreate(SQLModel):
    name: str = Field(..., min_length=1)
    description: str | None = None
    price: Decimal = Field(..., ge=0)
    stock_quantity: int = Field(..., ge=0)


class ProductRead(SQLModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int