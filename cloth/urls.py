from django.urls import path
from .views import OrderCreateView
from .views import AllClothingListView, UpperClothingListView,CustomerCreateView, HeadwearClothingListView, LowerClothingListView, FootwearClothingListView

urlpatterns = [
    path('all-clothing/', AllClothingListView.as_view(), name='all-clothing-list'),
    path('upper-clothing/', UpperClothingListView.as_view(), name='upper-clothing-list'),
    path('headwear-clothing/', HeadwearClothingListView.as_view(), name='headwear-clothing-list'),
    path('lower-clothing/', LowerClothingListView.as_view(), name='lower-clothing-list'),
    path('footwear-clothing/', FootwearClothingListView.as_view(), name='footwear-clothing-list'),
    path('create-order/', OrderCreateView.as_view(), name='order-create'),
    path('customer-create/', CustomerCreateView.as_view(), name='customer-create'),
]
