from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerCreate


class CustomerService:
  def __init__(self, repository: CustomerRepository):
    self.repository = repository

  def get_customer(self, customer_id: int) -> Customer | None:
    return self.repository.get_by_id(customer_id)

  def list_customers(self) -> list[Customer]:
    return self.repository.get_all()

  def update_customer(self, customer: Customer) -> Customer:
    return self.repository.update(customer)

  def create_customer(self, data: CustomerCreate) -> Customer:
    customer = Customer.model_validate(data)
    return self.repository.create(customer)

  def delete_customer(self, customer_id: int) -> None:
    customer = self.repository.get_by_id(customer_id)
    if customer is None:
      raise ValueError("Cliente não encontrado")
    self.repository.delete(customer)