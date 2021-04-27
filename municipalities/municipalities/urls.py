from django.contrib import admin
from django.urls import path, include
from municipalities_nl import urls
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
	)

# URL paths to the django app.
# admin is not configured for this project. We will be working with api path.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/', include(urls))

]

