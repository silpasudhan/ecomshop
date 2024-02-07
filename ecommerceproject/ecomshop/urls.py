from . import views
from django.urls import path, include
app_name='ecomshop'
urlpatterns = [

    path('', views.allProductCat, name='allProductCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdDetails, name='prod_cat_detail'),

]
