# Generated by Django 2.0.3 on 2020-05-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200518_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='item_id',
            field=models.ManyToManyField(to='orders.Menu'),
        ),
    ]