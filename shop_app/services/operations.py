from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from shop_app.base import tables
from shop_app.base.database import get_session
from shop_app.models.operations import *


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_item(self, code: int, table_name: str) -> tables.Shop:
        table = getattr(tables, table_name)
        item = (
            self.session
                .query(table)
                .filter_by(code=code)
                .first()
        )
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={'detail': 'Not found code %s' % code}
            )
        return item

    def get_shops(
            self,
            code: Optional[int] = None,
            name: Optional[str] = None,
    ) -> List[tables.Shop]:
        query = (
            self.session
                .query(tables.Shop)
        )
        if code:
            query = query.filter_by(code=code)
        if name:
            query = query.filter_by(name=name)
        shops = query.all()
        return shops

    def get_arts(
            self,
            code: Optional[int] = None,
            name: Optional[str] = None,
    ) -> List[tables.Article]:
        query = (
            self.session
                .query(tables.Article)
        )
        if code:
            query = query.filter_by(code=code)
        if name:
            query = query.filter_by(name=name)
        articles = query.all()
        return articles

    def create_shop(self, shop_data: ShopBase) -> tables.Shop:
        shop = tables.Shop(
            **shop_data.dict()
        )
        self.session.add(shop)
        self.session.commit()
        return shop

    def update_shop(self, code: int, shop_data: ShopBase) -> tables.Shop:
        shop = self._get_shop(code=code)
        for field, value in shop_data:
            setattr(shop, field, value)
        self.session.commit()
        return shop

    def create_art(self, art_data: ArticleBase) -> tables.Article:
        data = tables.Article(
            **art_data.dict()
        )
        self.session.add(data)
        self.session.commit()
        return data

    def update_art(self, code: int, art_data: ArticleBase) -> tables.Article:
        article = self._get_artic

    def delete_art(self):
        pass

    def update_art_rest(self):
        pass

