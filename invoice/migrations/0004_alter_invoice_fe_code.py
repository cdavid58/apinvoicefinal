# Generated by Django 3.2.8 on 2022-12-15 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_fe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_fe',
            name='code',
            field=models.IntegerField(),
        ),
    ]