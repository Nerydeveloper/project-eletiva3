# Generated by Django 4.1.7 on 2023-06-13 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Weblist', '0015_alter_lista_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]