# Generated by Django 3.2.8 on 2021-10-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leilao_fbv_user', '0008_alter_lote_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoteDAO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]