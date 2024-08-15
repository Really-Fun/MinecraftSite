# Generated by Django 5.0.8 on 2024-08-07 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Слаг')),
                ('max_online', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название новости')),
                ('text', models.TextField(max_length=10000, verbose_name='Содержание новости')),
                ('image', models.ImageField(upload_to='media/news/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='serv', to='minecraft.servers')),
            ],
        ),
    ]