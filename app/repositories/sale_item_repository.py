from sqlmodel import Session, select

from app.models.sale_item import SaleItem

class SaleItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, sale_item_id: int) -> SaleItem | None:
        return self.session.get(SaleItem, sale_item_id)

    def get_all(self, offset: int = 0, limit: int = 100) -> list[SaleItem]:
        statement = select(SaleItem).offset(offset).limit(limit)
        return list(self.session.exec(statement).all())

    def create(self, sale_item: SaleItem) -> SaleItem:
        self.session.add(sale_item)
        self.session.commit()
        self.session.refresh(sale_item)
        return sale_item

    def delete(self, sale_item: SaleItem) -> None:
        self.session.delete(sale_item)
        self.session.commit()
        
    def update(self, sale_item: SaleItem) -> SaleItem:
        self.session.add(sale_item)
        self.session.commit()
        self.session.refresh(sale_item)
        return sale_item