# Generated by Django 5.0.6 on 2024-08-12 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0005_alter_news_options_alter_servers_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='servers',
            options={'verbose_name': 'Сервер', 'verbose_name_plural': 'Серверы'},
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='media/MinecraftLogo.png', upload_to='media/news/%Y/%m/%d/', verbose_name='Изображение новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='serv', to='minecraft.servers', verbose_name='Наименование сервера'),
        ),
    ]
