import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    service_host: str = '0.0.0.0'
    service_port: int = os.getenv('PORT', 5000)
    database_url: str = os.getenv('DATABASE_URL', "postgresql://user:user_pw@127.0.0.1:5432/shop_db")


settings = Settings()