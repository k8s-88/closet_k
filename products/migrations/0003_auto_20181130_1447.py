# Generated by Django 2.0.8 on 2018-11-30 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181129_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories', to='products.Category'),
        ),
    ]
