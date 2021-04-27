from django.urls import path, include
from . import views
from rest_framework import routers



# Default router performs all the basic operations.
router = routers.DefaultRouter()

# Include Location View to the default router.
router.register(r'locations', views.LocationView,basename='locations')

# Add router to the api path.
urlpatterns = [
path('', include(router.urls)),
]


