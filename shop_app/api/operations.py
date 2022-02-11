from typing import List
from fastapi import APIRouter, Depends

from shop_app.models.operations import *
from shop_app.services.operations import OperationService


router = APIRouter(
    tags=['operations']
)


@router.get('/shops', response_model=List[ShopBase])
async def get_shop(
        shop_code: Optional[int] = None,
        shop_name: Optional[str] = None,
        service: OperationService = Depends()
):
    return service.get_shops(shop_code, shop_name)


@router.post('/shops', response_model=ShopCreate)
async def create_shop(
        shop_data: ShopBase,
        service: OperationService = Depends()
):
    return service.create_shop(shop_data=shop_data)


@router.put('/shops/', response_model=ShopCreate)
async def update_shop(
        shop_code: int,
        shop_data: ShopBase,
        service: OperationService = Depends()
):
    return service.update_shop(shop_code=shop_code, shop_data=shop_data)


@router.get('/articles', response_model=List[ArticleBase])
async def get_article(
        art_code: Optional[int] = None,
        art_name: Optional[str] = None,
        service: OperationService = Depends()
):
    return service.get_arts(art_code, art_name)


@router.post('/articles', response_model=ArticleCreate)
async def create_article(
        art_data: ArticleBase,
        service: OperationService = Depends()
):
    return service.create_art(art_data=art_data)


@router.put('/articles', response_model=ArticleCreate)
async def update_article(
        art_code: int,
        art_data: ArticleBase,
        service: OperationService = Depends()
):
    return service.update_art(art_code=art_code, art_data=art_data)
