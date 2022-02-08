from typing import List
from fastapi import APIRouter, Depends

from shop_app.models.operations import *
from shop_app.services.operations import OperationService


router = APIRouter(
    tags=['operations']
)


@router.get('/shops', response_model=List[ShopBase])
async def get_shop(
        service: OperationService = Depends()
):
    return service.get_shop()


@router.get('/articles', response_model=List[ArticleBase])
async def get_article(
        service: OperationService = Depends()
):
    return service.get_art()


@router.post('/shops', response_model=ShopCreate)
async def create_shop(
        shop_data: ShopBase,
        service: OperationService = Depends()
):
    return service.create_shop(shop_data=shop_data)


@router.post('/articles', response_model=ArticleCreate)
async def create_article(
        art_data: ArticleBase,
        service: OperationService = Depends()
):
    return service.create_art(art_data=art_data)

