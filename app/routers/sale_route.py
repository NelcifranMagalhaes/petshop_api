from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.repositories.customer_repository import CustomerRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.sale_item_repository import SaleItemRepository
from app.repositories.sale_repository import SaleRepository
from app.schemas.sale import SaleCreate, SaleRead
from app.services.sale_service import SaleService

router = APIRouter(prefix="/sales", tags=["Sales"])


def get_sale_service(
    session: Annotated[Session, Depends(get_session)],
) -> SaleService:
    return SaleService(
        SaleRepository(session),
        ProductRepository(session),
        SaleItemRepository(session),
        CustomerRepository(session)
    )


SaleServiceDep = Annotated[SaleService, Depends(get_sale_service)]


@router.post(
    "/",
    response_model=SaleRead,
    status_code=status.HTTP_201_CREATED,
)
def create_sale(payload: SaleCreate, service: SaleServiceDep):
    return service.create_sale(payload)


@router.get("/", response_model=list[SaleRead])
def list_sales(service: SaleServiceDep):
    return service.list_sales()