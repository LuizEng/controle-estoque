from django.db import models


class Fornecedor(models.Model):

    class Meta:
        db_table = 'FORNECEDOR'
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=64)
    codigo = models.CharField(max_length=12)

    def __str__(self):
        return self.codigo


class UnidadeMedida(models.Model):

    class Meta:
        db_table = 'UNIDADE_MEDIDA'

    descricao = models.CharField(max_length=8)

    def __str__(self):
        return self.descricao


class CategoriaItem(models.Model):

    class Meta:
        db_table = 'CATEGORIA_ITEM'
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class Lote(models.Model):

    class Meta:
        db_table = 'LOTE'
    codigo = models.CharField(max_length=16)
    data = models.DateField(auto_now=True)
    #Não utilizei o Cascade, pois não faz sentido nesse caso
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.data


class Item(models.Model):

    class Meta:
        db_table = 'ITEM'
    codigo = models.CharField(max_length=16)
    descricao = models.CharField(max_length=128)
    dimensao = models.CharField(max_length=16)
    ativo = models.BooleanField(default=True)

    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaItem, on_delete=models.CASCADE)
    fornecedor = models.ManyToManyField(Fornecedor)

    def __str__(self):
        return self.descricao
