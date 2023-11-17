from django.db import models
from core.models import Item, Fornecedor, Lote


class OperacaoFiscal(models.Model):

    class Meta:
        db_table = 'OPERACAO_FISCAL'
    codigo = models.CharField(max_length=8)
    descricao = models.CharField(max_length=32)
    #S-Saída E-Entrada
    tipo = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao


class OperacaoInventario(models.Model):

    class Meta:
        db_table = 'OPERACAO_INVENTARIO'
    codigo = models.CharField(max_length=8)
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class MotivoSaida(models.Model):

    class Meta:
        db_table = 'MOTIVO_SAIDA'
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class Inventario(models.Model):

    class Meta:
        db_table = 'INVENTARIO'
    #S-Saída E-Entrada
    tipo_movimentacao = models.CharField(max_length=1)
    data = models.DateField(auto_now=False)
    quantidade = models.DecimalField(max_digits=9, decimal_places=2)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    serie = models.CharField(max_length=20)
    nfe = models.CharField(max_length=64)

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    operacao_fiscal = models.ForeignKey(OperacaoFiscal, on_delete=models.DO_NOTHING)
    operacao_inventario = models.ForeignKey(OperacaoInventario, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.valor


class MovimentacaoEntrada(models.Model):

    class Meta:
        db_table = 'MOVIMENTACAO_ENTRADA'
    data = models.DateField(auto_now=True)
    quantidade = models.DecimalField(max_digits=9, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    serie = models.CharField(max_length=20)
    nfe = models.CharField(max_length=64)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    operacao = models.ForeignKey(OperacaoFiscal, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)

    def __str__(self):
        return self.data


class MovimentacaoSaida(models.Model):

    class Meta:
        db_table = 'MOVIMENTACAO_SAIDA'

    data = models.DateField(auto_now=True)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    motivo_saida = models.ForeignKey(MotivoSaida, on_delete=models.CASCADE)

    def __str__(self):
        return self.data






