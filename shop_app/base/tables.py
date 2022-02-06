import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Article(Base):
    __tablename__ = 'article'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    art_name = sa.Column(sa.Text)
    price = sa.Column(sa.Numeric(10, 2))
    category_id = sa.Column(sa.Integer, sa.ForeignKey('category.id'), nullable=True)
    active = sa.Column(sa.Boolean)
    last_date = sa.Column(sa.DateTime, default=datetime.utcnow)


class Shop(Base):
    __tablename__ = 'shop'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    shop_name = sa.Column(sa.Text)
    address = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean, default=False)
    last_date = sa.Column(sa.DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = 'category'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    cat_name = sa.Column(sa.Text)
    last_date = sa.Column(sa.DateTime, default=datetime.utcnow)


class ArtShop(Base):
    __tablename__ = 'art_shop'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id_art = sa.Column(sa.Integer, sa.ForeignKey('article.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
