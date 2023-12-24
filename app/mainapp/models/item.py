from django.db.models import Model, CharField, DateTimeField, ImageField, TextField, DecimalField

__all__ = [
    'Item',
]


class Item(Model):
    name = CharField(max_length=85)
    description = TextField(blank=True)
    price = DecimalField(max_digits=6, decimal_places=2)
