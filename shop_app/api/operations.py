from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shop_app.models.operations import *
from shop_app.services.operations import OperationService


router = APIRouter(
    tags=['operations']
)


@router.get('/shops')
async def get_shop(
        code: Optional[int] = None,
        name: Optional[str] = None,
        service: OperationService = Depends()
):
    # content = jsonable_encoder({'shops': service.get_shops(code, name)})
    # return JSONResponse(content=content)
    data = service.get_shops(code, name)
    return {'shops': data}


@router.post('/shops', response_model=ShopCreate)
async def create_shop(
        shop_data: ShopBase,
        service: OperationService = Depends()
):
    return service.create_shop(shop_data=shop_data)


@router.put('/shops/', response_model=ShopCreate)
async def update_shop(
        code: int,
        shop_data: ShopBase,
        service: OperationService = Depends()
):
    return service.update_shop(code=code, shop_data=shop_data)


@router.get('/articles', response_model=List[ArticleBase])
async def get_article(
        code: Optional[int] = None,
        name: Optional[str] = None,
        service: OperationService = Depends()
):
    return service.get_arts(code, name)


@router.post('/articles', response_model=ArticleCreate)
async def create_article(
        art_data: ArticleBase,
        service: OperationService = Depends()
):
    return service.create_art(art_data=art_data)


@router.put('/articles', response_model=ArticleCreate)
async def update_article(
        code: int,
        art_data: ArticleBase,
        service: OperationService = Depends()
):
    return service.update_art(code=code, art_data=art_data)
