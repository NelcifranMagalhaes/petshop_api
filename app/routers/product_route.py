from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_session
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import ProductService
from sqlmodel import Session

router = APIRouter(prefix="/products", tags=["Products"])


def get_product_service(
    session: Annotated[Session, Depends(get_session)],
) -> ProductService:
    repository = ProductRepository(session)
    return ProductService(repository)


ProductServiceDep = Annotated[
    ProductService,
    Depends(get_product_service),
]


@router.post(
    "/",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    data: ProductCreate,
    service: ProductServiceDep,
):
    return service.create_product(data)


@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, data: ProductCreate, service: ProductServiceDep):
    product = service.get_product(product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )

    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.stock_quantity = data.stock_quantity

    return service.update_product(product)


@router.get("/", response_model=list[ProductRead])
def list_products(service: ProductServiceDep):
    return service.list_products()


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, service: ProductServiceDep):
    product = service.get_product(product_id)

    if product is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )                                   
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, service: ProductServiceDep):
    if service.get_product(product_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )
    service.delete_product(product_id)