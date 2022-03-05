import csv

from shop_app.base.database import Session
from shop_app.base import tables
from shop_app.models import operations

session = Session()

for csv_file, table_name in (
        ('Shops.csv', 'Shop'),
        ('Articles.csv', 'Article'),
        ('Category.csv', 'Category')
):

    with open(csv_file, 'r') as f:
        csv_obj = csv.reader(f, delimiter=';')
        fielders = csv_obj.__next__()
        model_class = getattr(operations, table_name + 'Base')
        data = [model_class(**dict(zip(fielders, item))) for item in csv_obj]
        table = getattr(tables, table_name)
        session.query(table).delete()
        items = [
            table(
                **item.dict()
            )
            for item in data
        ]
        session.add_all(items)

session.commit()
session.close()
