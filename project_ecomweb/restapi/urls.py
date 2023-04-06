from django.urls import path
from .views import CategoryApiView, ProductApiView, ProductApiIdView, UserApiView, UserApiIdView

urlpatterns = [
    path('category/', CategoryApiView.as_view(), name='category'),
    path('product/', ProductApiView.as_view(), name='product'),
    path('product/<int:id>/', ProductApiIdView.as_view(), name='product-by-id'),
    path('user/', UserApiView.as_view(), name='user'),
    path('user/<int:id>/', UserApiIdView.as_view(), name='user-by-id'),

]