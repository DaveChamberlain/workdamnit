# Generated by Django 2.0.1 on 2018-04-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0009_subscribe_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]