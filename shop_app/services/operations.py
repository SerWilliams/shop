from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from shop_app.base import tables
from shop_app.base.database import get_session
from shop_app.models.operations import *


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_shop(self) -> List[tables.Shop]:
        query = (
            self.session
            .query(tables.Shop)
        )
        shops = query.all()
        return shops

    def get_art(self) -> List[tables.Article]:
        query = (
            self.session
            .query(tables.Article)
        )
        articles = query.all()
        return articles

    def create_shop(self, shop_data: ShopBase) -> tables.Shop:
        data = tables.Shop(
            **shop_data.dict()
        )
        self.session.add(data)
        self.session.commit()
        return data

    def update_shop(self):
        pass

    def create_art(self, art_data: ArticleBase) -> tables.Article:
        data = tables.Article(
            **art_data.dict()
        )
        self.session.add(data)
        self.session.commit()
        return data

    def update_art(self):
        pass

    def delete_art(self):
        pass

    def update_art_rest(self):
        pass

