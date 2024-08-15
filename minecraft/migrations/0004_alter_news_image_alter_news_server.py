# Generated by Django 5.0.8 on 2024-08-09 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0003_alter_news_options_alter_servers_options_and_more'),
    ]

    operations = [
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