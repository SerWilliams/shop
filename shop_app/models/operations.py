from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ShopBase(BaseModel):
    shop_name: str
    shop_code: int
    address: Optional[str]
    active: bool

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    art_name: str
    art_code: int
    price: float
    # category: CategoryBase
    active: bool

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    cat_name: str

    class Config:
        orm_mode = True


class ShopCreate(ShopBase):
    id: int
    last_date: datetime


class ArticleCreate(ArticleBase):
    id: int
    last_date: datetime
