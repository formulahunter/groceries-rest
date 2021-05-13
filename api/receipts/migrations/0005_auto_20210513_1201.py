# Generated by Django 3.2.2 on 2021-05-13 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0004_auto_20210513_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groceryitem',
            options={'ordering': ['brand', 'name']},
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='receipts.groceryitembrand'),
            preserve_default=False,
        ),
    ]