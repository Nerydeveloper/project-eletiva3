# Generated by Django 4.1.7 on 2023-06-13 21:39

import Weblist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblist', '0017_alter_mercado_iduser_alter_produto_iduser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Weblist.models.upload_image_receita),
        ),
    ]
