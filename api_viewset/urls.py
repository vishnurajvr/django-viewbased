from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.UserViewSet, basename = 'UserViewSet')
router.register('modelviewset', views.UserModelViewSet, basename = 'UserModelViewSet')

urlpatterns = [
]
urlpatterns += router.urls