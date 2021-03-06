# Generated by Django 2.0.4 on 2018-07-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50, null=True)),
                ('contact_position', models.CharField(max_length=50, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=24, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_image', models.ImageField(blank=True, null=True, upload_to='contact/images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ssss', models.DateTimeField(auto_now_add=True)),
                ('shit', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
