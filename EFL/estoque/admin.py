from django.contrib import admin
from .models import *

admin.site.register(OperacaoFiscal)
admin.site.register(OperacaoInventario)
admin.site.register(MotivoSaida)
admin.site.register(Inventario)
admin.site.register(MovimentacaoEntrada)
admin.site.register(MovimentacaoSaida)
