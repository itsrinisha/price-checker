from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('update/', views.update_prices, name="update-prices"),
    path('delete/<int:pk>/', views.LinkDeleteView.as_view(), name="delete-link"),
]
