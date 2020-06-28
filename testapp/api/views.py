from testapp.models import Product
from testapp.api.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ProductApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_class = [IsAuthenticated,]

