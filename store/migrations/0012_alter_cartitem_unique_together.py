# Generated by Django 4.0.5 on 2022-07-02 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_cart_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart',), ('product',)},
        ),
    ]
