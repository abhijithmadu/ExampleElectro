# Generated by Django 2.2.8 on 2021-05-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_auto_20210511_1208'),
        ('orders', '0004_auto_20210512_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='ecomapp.Variation'),
        ),
    ]
