
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from pedidos.views import Pedidosviewset

router = routers.DefaultRouter()
router.register("Pedidos",Pedidosviewset,basename="Pedidos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
