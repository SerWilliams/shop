from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shop_app.settings import settings


engine = create_engine(
    settings.database_url,
    client_encoding='utf8'
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()