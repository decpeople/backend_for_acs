
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'flight', views.FlightViewSet)
router.register(r'aircompany', views.AirCompanyViewSet)
router.register(r'rotation', views.RotatingViewSet)
router.register(r'command', views.CommandViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'image', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]   