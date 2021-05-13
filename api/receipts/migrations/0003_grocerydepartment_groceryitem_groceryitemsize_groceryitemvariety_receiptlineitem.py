# Generated by Django 3.2.2 on 2021-05-13 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_auto_20210511_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.marketlocation')),
            ],
            options={
                'ordering': ['location', 'name'],
            },
        ),
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryItemSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=32, verbose_name='description of size (incl. unit of measure where appropriate)')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitem')),
            ],
            options={
                'ordering': ['item', 'desc'],
            },
        ),
        migrations.CreateModel(
            name='GroceryItemVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=64, verbose_name='description')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitem')),
            ],
            options={
                'ordering': ['item', 'desc'],
            },
        ),
        migrations.CreateModel(
            name='ReceiptLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.DecimalField(decimal_places=3, default=1.0, max_digits=6)),
                ('units', models.CharField(default='ct', max_length=2, verbose_name='unit of measure')),
                ('tax_code', models.CharField(max_length=2, verbose_name='character printed next to item name/price, if any')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.grocerydepartment')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitem')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.receipt')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitemsize')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitemvariety')),
            ],
            options={
                'ordering': ['receipt', 'item'],
            },
        ),
    ]
