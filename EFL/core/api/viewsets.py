from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import *
from .serializers import *
from validate_docbr import CNPJ


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['codigo', 'descricao', 'dimensao', 'categoria', 'fornecedor__cnpj', 'fornecedor__razao_social']


class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['codigo', 'razao_social', 'cnpj']

    def post_(self, request, serializer):
        serial = serializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response(serial.data)

    def create(self, request, *args, **kwargs):
        cnpj = CNPJ()
        if not cnpj.validate(cnpj.mask(request.data.get('cnpj'))):
            return Response({'Erro': 'O CNPJ informádo não é válido.'})
        else:
            if self.queryset.filter(cnpj=request.data.get('cnpj')):
                return Response({'Erro': 'O CNPJ informado já está cadastrado. Fornecedor: %s' % self.queryset.get(cnpj=request.query_params['cnpj'])})
            else:
                return self.post_(request, FornecedorSerializer)


class UnidadeMedidaViewSet(ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['descricao']


class CategoriaItemViewSet(ModelViewSet):
    queryset = CategoriaItem.objects.all()
    serializer_class = CategoriaItemSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['descricao']


class LoteViewSet(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter,)
    search_fields = ['codigo', 'data',  'fornecedor__razao_social']
