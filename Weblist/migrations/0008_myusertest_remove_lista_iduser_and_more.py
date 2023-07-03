# Generated by Django 4.1.7 on 2023-06-04 20:54

import Weblist.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Weblist', '0007_alter_receita_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='myusertest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.TextField(max_length=257)),
            ],
        ),
        migrations.RemoveField(
            model_name='lista',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='listaproduto',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='mercado',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='idUser',
        ),
        migrations.AlterField(
            model_name='receita',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Weblist.models.upload_image_receita),
        ),
        migrations.DeleteModel(
            name='ReceitaProduto',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='lista',
            name='idmyusertest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Weblist.myusertest'),
        ),
        migrations.AddField(
            model_name='listaproduto',
            name='idmyusertest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Weblist.myusertest'),
        ),
        migrations.AddField(
            model_name='mercado',
            name='idmyusertest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Weblist.myusertest'),
        ),
        migrations.AddField(
            model_name='produto',
            name='idmyusertest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Weblist.myusertest'),
        ),
        migrations.AddField(
            model_name='receita',
            name='idmyusertest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Weblist.myusertest'),
        ),
    ]