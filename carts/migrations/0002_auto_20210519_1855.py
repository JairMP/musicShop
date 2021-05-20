# Generated by Django 3.2.2 on 2021-05-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_brand'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
