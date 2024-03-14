from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name="detail"),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_color/', views.AddColorToCar.as_view(), name='add_color'),
    path('cars/<int:car_id>/assoc_color/<int:color_id>/', views.assoc_color, name='assoc_color')
]