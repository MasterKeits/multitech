# Generated by Django 2.0.4 on 2018-06-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_categorys',
            field=models.ManyToManyField(blank=True, to='sales.SubCategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='products',
            field=models.ManyToManyField(blank=True, to='sales.Product'),
        ),
    ]
