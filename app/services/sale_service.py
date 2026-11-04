

from datetime import datetime
from decimal import Decimal
from datetime import datetime, timezone

from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.repositories.product_repository import ProductRepository
from app.repositories.sale_item_repository import SaleItemRepository
from app.repositories.sale_repository import SaleRepository


class SaleService:
    def __init__(
        self,
        sale_repository: SaleRepository,
        product_repository: ProductRepository,
        sale_item_repository: SaleItemRepository,
    ):
        self.sale_repository = sale_repository
        self.product_repository = product_repository
        self.sale_item_repository = sale_item_repository

    def create_sale(self, sale_data):
        if not sale_data.sale:
            raise ValueError("A lista de itens da venda não pode estar vazia")

        total_amount = Decimal("0")
        products = []
        for item in sale_data.sale:
            product = self.product_repository.get_by_id(item["product_id"])
            if not product:
                raise ValueError(f"Produto com ID {item['product_id']} não encontrado")
            if product.stock_quantity < item["quantity"]:
                raise ValueError(f"Estoque insuficiente para o produto {product.name}")
            product.stock_quantity -= item["quantity"]
            total_amount += item["quantity"] * product.price
            products.append(product)

        sale = self.sale_repository.create(
            Sale(
                customer_id=sale_data.customer_id,
                sale_date=datetime.now(timezone.utc),
                total_amount=total_amount,
            )
        )

        for item, product in zip(sale_data.sale, products):
            self.product_repository.update(product)
            unit_price = product.price
            self.sale_item_repository.create(
                SaleItem(
                    sale_id=sale.id,
                    product_id=product.id,
                    quantity=item["quantity"],
                    unit_price=unit_price,
                    subtotal=item["quantity"] * unit_price,
                )
            )

        return sale

    def get_sale(self, sale_id):
        return self.sale_repository.get_by_id(sale_id)

    def update_sale(self, sale_id, sale_data):
        return self.sale_repository.update(sale_id, sale_data)

    def delete_sale(self, sale_id):
        return self.sale_repository.delete(sale_id)

    def list_sales(self):
        return self.sale_repository.get_all()