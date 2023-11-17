from rest_framework.serializers import ModelSerializer
from core.models import *


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['codigo', 'razao_social', 'cnpj']


class UnidadeMedidaSerializer(ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = ['descricao']


class CategoriaItemSerializer(ModelSerializer):
    class Meta:
        model = CategoriaItem
        fields = ['descricao']


class LoteSerializer(ModelSerializer):
    fornecedor = FornecedorSerializer()

    class Meta:
        model = Lote
        fields = ['codigo', 'data', 'fornecedor']


class ItemSerializer(ModelSerializer):
    fornecedor = FornecedorSerializer()
    unidade = UnidadeMedidaSerializer()
    categoria = CategoriaItemSerializer()

    class Meta:
        model = Item
        fields = ['codigo', 'descricao', 'dimensao', 'unidade', 'categoria', 'fornecedor']