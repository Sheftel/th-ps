from django.urls import path

from .views import ItemBuyView, ItemDetailView

urlpatterns = [
    path('buy/<int:pk>/', ItemBuyView.as_view(), name='item_buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
