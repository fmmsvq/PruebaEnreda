from django.contrib import admin
from .models import Factura, Contrato, Liquidacion

# Register your models here.


admin.site.register(Factura)
admin.site.register(Contrato)
admin.site.register(Liquidacion)

