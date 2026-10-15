from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate


class ProductService:
  def __init__(self, repository: ProductRepository):
    self.repository = repository

  def get_product(self, product_id: int) -> Product | None:
    return self.repository.get_by_id(product_id)

  def list_products(self) -> list[Product]:
    return self.repository.get_all()
  
  def update_product(self, product: Product) -> Product:
    return self.repository.update(product)

  def create_product(self, data: ProductCreate) -> Product:
    product = Product.model_validate(data)
    return self.repository.create(product)

  def delete_product(self, product_id: int) -> None:
    product = self.repository.get_by_id(product_id)
    if product is None:
      raise ValueError("Produto não encontrado")
    self.repository.delete(product)