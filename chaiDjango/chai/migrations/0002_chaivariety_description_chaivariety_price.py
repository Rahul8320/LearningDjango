# Generated by Django 4.2.13 on 2024-06-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.IntegerField(default=10),
        ),
    ]
