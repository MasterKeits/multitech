# Generated by Django 2.0.4 on 2018-06-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='sales.Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_categorys',
            field=models.ManyToManyField(blank=True, null=True, to='sales.SubCategory'),
        ),
    ]
