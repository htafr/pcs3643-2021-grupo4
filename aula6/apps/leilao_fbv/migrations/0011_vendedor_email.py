# Generated by Django 3.2.8 on 2021-10-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leilao_fbv', '0010_auto_20211008_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='email',
            field=models.CharField(default='', max_length=256),
        ),
    ]