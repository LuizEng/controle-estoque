"""EFL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import *
from estoque.api.viewsets import *
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('fornecedor', FornecedorViewSet)
router.register('unidademedida', UnidadeMedidaViewSet)
router.register('categoriaitem', CategoriaItemViewSet)
router.register('lote', LoteViewSet)
router.register('item', ItemViewSet)

router.register('operacaofiscal', OperacaoFiscalViewSet)
router.register('operacaoinventario', OperacaoInventarioViewSet)
router.register('motivosaida', MotivoSaidaViewSet)
router.register('inventario', InventarioViewSet)
router.register('movimentacaoentrada', MovimentacaoEntradaViewSet)
router.register('movimentacaosaida', MovimentacaoSaidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),

]
