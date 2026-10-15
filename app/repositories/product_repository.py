from sqlmodel import Session, select

from app.models.product import Product


class ProductRepository:
  def __init__(self, session: Session):
      self.session = session

  def get_by_id(self, product_id: int) -> Product | None:
      return self.session.get(Product, product_id)

  def get_all(self, offset: int = 0, limit: int = 100) -> list[Product]:
      statement = select(Product).offset(offset).limit(limit)
      return list(self.session.exec(statement).all())

  def create(self, product: Product) -> Product:
      self.session.add(product)
      self.session.commit()
      self.session.refresh(product)
      return product

  def delete(self, product: Product) -> None:
      self.session.delete(product)
      self.session.commit()
      
  def update(self, product: Product) -> Product:
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product