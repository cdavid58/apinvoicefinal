# Generated by Django 3.2.8 on 2023-02-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventory_quanty'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='metro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inventory',
            name='und',
            field=models.IntegerField(default=0),
        ),
    ]