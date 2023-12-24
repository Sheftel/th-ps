from django.db.models import Model, CharField, TextField, IntegerField

__all__ = [
    'Item',
]


class Item(Model):
    name = CharField(max_length=85)
    description = TextField(blank=True)
    price = IntegerField(default=0)
