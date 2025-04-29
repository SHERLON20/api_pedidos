from rest_framework import viewsets
from .models import Pedidos
from .serializers import PedidosSerializer

class Pedidosviewset(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
    
