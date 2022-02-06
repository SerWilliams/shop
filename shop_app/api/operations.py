from fastapi import APIRouter


router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/')
async def root():
    return 'Hello'

