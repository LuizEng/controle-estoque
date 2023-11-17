from rest_framework.serializers import ModelSerializer

from core.api.serializers import FornecedorSerializer
from estoque.models import *
from core.api.serializers import *


class OperacaoFiscalSerializer(ModelSerializer):
    class Meta:
        model = OperacaoFiscal
        fields = ['codigo', 'descricao', 'tipo']


class OperacaoInventarioSerializer(ModelSerializer):
    class Meta:
        model = OperacaoInventario
        fields = ['codigo', 'descricao']


class MotivoSaidaSerializer(ModelSerializer):
    class Meta:
        model = MotivoSaida
        fields = ['descricao']


class InventarioSerializer(ModelSerializer):

    fornecedor = FornecedorSerializer()
    operacao_fiscal = OperacaoFiscalSerializer()
    operacao_inventario = OperacaoInventarioSerializer()
    item = ItemSerializer()

    class Meta:
        model = Inventario
        fields = ['data', 'tipo_movimentacao', 'quantidade',
                  'valor', 'serie', 'nfe', 'fornecedor',
                  'operacao_fiscal', 'operacao_inventario','item']


class MovimentacaoEntradaSerializer(ModelSerializer):

    item = ItemSerializer()
    operacao = OperacaoFiscalSerializer()
    lote = LoteSerializer()

    class Meta:
        model = MovimentacaoEntrada
        fields = ['data', 'quantidade', 'valor_unitario',
                  'valor_total', 'serie', 'nfe',
                  'item', 'operacao', 'lote']


class MovimentacaoSaidaSerializer(ModelSerializer):

    item = ItemSerializer()
    lote = LoteSerializer()
    motivo_saida = MotivoSaidaSerializer()

    class Meta:
        model = MovimentacaoSaida
        fields = ['data', 'item', 'lote', 'motivo_saida']

