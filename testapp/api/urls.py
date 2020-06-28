from rest_framework import routers
from testapp.api import views
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
router = routers.DefaultRouter()
router.register('prod',views.ProductApi)


urlpatterns = [
   path('',include(router.urls) ), 
   path('jwt_obtain/',obtain_jwt_token),
   path('jwt_verify/',verify_jwt_token),
   path('jwt_refresh/',refresh_jwt_token),
]