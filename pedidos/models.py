from django.db import models

class Pedidos(models.Model):
    todos_pedidos = models.TextField(max_length=500)

    def __str__(self):
        return self.todos_pedidos
    
