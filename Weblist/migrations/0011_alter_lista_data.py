# Generated by Django 4.1.7 on 2023-06-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblist', '0010_lista_idproduto_delete_listaproduto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='data',
            field=models.DateTimeField(auto_created=True, default='11/06/2023 11:10'),
        ),
    ]