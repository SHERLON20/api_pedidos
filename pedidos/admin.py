from django.contrib import admin
from .models import Pedidos

class pedidos_admin(admin.ModelAdmin):
    list_display=('id','todos_pedidos')
    list_display_links = ('id','todos_pedidos')
    list_per_page = 20
    search_fields = ('id',)

admin.site.register(Pedidos,pedidos_admin)

