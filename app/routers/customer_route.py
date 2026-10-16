from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_session
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerCreate, CustomerRead
from app.services.customer_service import CustomerService
from sqlmodel import Session

router = APIRouter(prefix="/customers", tags=["Customers"])



def get_customer_service(
    session: Annotated[Session, Depends(get_session)],
) -> CustomerService:
    repository = CustomerRepository(session)
    return CustomerService(repository)


CustomerServiceDep = Annotated[
    CustomerService,
    Depends(get_customer_service),
]


@router.post(
    "/",
    response_model=CustomerRead,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(
    data: CustomerCreate,
    service: CustomerServiceDep,
):
    return service.create_customer(data)



@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: int, data: CustomerCreate, service: CustomerServiceDep):
    customer = service.get_customer(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado",
        )

    customer.name = data.name
    customer.phone = data.phone
    customer.pets = data.pets

    return service.update_customer(customer)



@router.get("/", response_model=list[CustomerRead])
def list_customers(service: CustomerServiceDep):
    return service.list_customers()



@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int, service: CustomerServiceDep):
    customer = service.get_customer(customer_id)

    if customer is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado",
        )                                   
    return customer



@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, service: CustomerServiceDep):
    if service.get_customer(customer_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado",
        )
    service.delete_customer(customer_id)