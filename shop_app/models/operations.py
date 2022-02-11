from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MyBase(BaseModel):
    class Config:
        orm_mode = True


class ShopBase(MyBase):
    name: str
    code: int
    address: Optional[str]
    active: bool


class ArticleBase(MyBase):
    name: str
    code: int
    price: float
    # category: CategoryBase
    active: bool


class CategoryBase(MyBase):
    name: str
    description: Optional[str]


class ShopCreate(ShopBase):
    id: int
    last_date: datetime


class ArticleCreate(ArticleBase):
    id: int
    last_date: datetime
