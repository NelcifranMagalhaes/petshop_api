from sqlmodel import Session, select
from app.models.customer import Customer

class CustomerRepository:

  def __init__(self, session: Session):
      self.session = session

  def get_by_id(self, customer_id: int) -> Customer | None:
      return self.session.get(Customer, customer_id)

  def get_all(self, offset: int = 0, limit: int = 100) -> list[Customer]:
      statement = select(Customer).offset(offset).limit(limit)
      return list(self.session.exec(statement).all())

  def create(self, customer: Customer) -> Customer:
      self.session.add(customer)
      self.session.commit()
      self.session.refresh(customer)
      return customer

  def delete(self, customer: Customer) -> None:
      self.session.delete(customer)
      self.session.commit()
      
  def update(self, customer: Customer) -> Customer:
    self.session.add(customer)
    self.session.commit()
    self.session.refresh(customer)
    return customer
