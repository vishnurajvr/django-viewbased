from django.urls import path
from . import views

urlpatterns = [
	path('', views.crud_api_view),
	path('<int:pk>/', views.crud_api_view_udpate)
]