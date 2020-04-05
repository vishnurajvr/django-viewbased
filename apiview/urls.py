from django.urls import path
from . import views

urlpatterns = [
	path(r'', views.crud_apiview.as_view()),
	path(r'<int:pk>/', views.crud_apiview.as_view()),
]