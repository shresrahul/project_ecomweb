from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns= [
    path("dashboard/", views.dashboard_index, name="dashboard"),

    # Categories
    path('category/add/', views.category_add, name='add-category'),

    # Products
    path('product/add/', views.product_add, name='add-product'),
    path('products/', views.product_index, name='list-product'),
    path('products/update/', views.product_update, name='update-product'),
    path('product/view/<int:id>', views.product_view, name='view-product'),
    path('product/edit/<int:id>', views.product_edit, name='edit-product'),
    path('product/delete/<int:id>', views.product_delete, name='delete-product'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
