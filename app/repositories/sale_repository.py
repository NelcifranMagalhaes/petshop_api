from sqlmodel import Session, select

from app.models.sale import Sale


class SaleRepository:
  def __init__(self, session: Session):
      self.session = session

  def get_by_id(self, sale_id: int) -> Sale | None:
      return self.session.get(Sale, sale_id)

  def get_all(self, offset: int = 0, limit: int = 100) -> list[Sale]:
      statement = select(Sale).offset(offset).limit(limit)
      return list(self.session.exec(statement).all())

  def create(self, sale: Sale) -> Sale:
      self.session.add(sale)
      self.session.commit()
      self.session.refresh(sale)
      return sale

  def delete(self, sale: Sale) -> None:
      self.session.delete(sale)
      self.session.commit()
      
  def update(self, sale: Sale) -> Sale:
        self.session.add(sale)
        self.session.commit()
        self.session.refresh(sale)
        return sale