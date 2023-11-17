from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from estoque.models import *
from .serializers import *


class OperacaoFiscalViewSet(ModelViewSet):
    queryset = OperacaoFiscal.objects.all()
    serializer_class = OperacaoFiscalSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['codigo', 'descricao', 'tipo']


class OperacaoInventarioViewSet(ModelViewSet):
    queryset = OperacaoInventario.objects.all()
    serializer_class = OperacaoInventarioSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['codigo', 'descricao']

class MotivoSaidaViewSet(ModelViewSet):
    queryset = MotivoSaida.objects.all()
    serializer_class = MotivoSaidaSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['descricao']


class InventarioViewSet(ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['data', 'tipo_movimentacao', 'quantidade', 'item']


class MovimentacaoEntradaViewSet(ModelViewSet):
    queryset = MovimentacaoEntrada.objects.all()
    serializer_class = MovimentacaoEntradaSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['data', 'item']


class MovimentacaoSaidaViewSet(ModelViewSet):
    queryset = MovimentacaoSaida.objects.all()
    serializer_class = MovimentacaoSaidaSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['data', 'item', 'lote']