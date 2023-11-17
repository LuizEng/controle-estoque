# Generated by Django 3.0.5 on 2020-04-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivoSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'MOTIVO_SAIDA',
            },
        ),
        migrations.CreateModel(
            name='OperacaoFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('descricao', models.CharField(max_length=32)),
                ('tipo', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'OPERACAO_FISCAL',
            },
        ),
        migrations.CreateModel(
            name='OperacaoInventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('descricao', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'OPERACAO_INVENTARIO',
            },
        ),
        migrations.CreateModel(
            name='MovimentacaoSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lote')),
                ('motivo_saida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.MotivoSaida')),
            ],
            options={
                'db_table': 'MOVIMENTACAO_SAIDA',
            },
        ),
        migrations.CreateModel(
            name='MovimentacaoEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('serie', models.CharField(max_length=20)),
                ('nfe', models.CharField(max_length=64)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lote')),
                ('operacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.OperacaoFiscal')),
            ],
            options={
                'db_table': 'MOVIMENTACAO_ENTRADA',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimentacao', models.CharField(max_length=1)),
                ('data', models.DateField()),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('serie', models.CharField(max_length=20)),
                ('nfe', models.CharField(max_length=64)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Fornecedor')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Item')),
                ('operacao_fiscal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.OperacaoFiscal')),
                ('operacao_inventario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.OperacaoInventario')),
            ],
            options={
                'db_table': 'INVENTARIO',
            },
        ),
    ]
