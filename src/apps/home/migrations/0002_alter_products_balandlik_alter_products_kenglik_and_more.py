# Generated by Django 5.1.4 on 2025-01-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='balandlik',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='kenglik',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='products',
            name='uzunlik',
            field=models.IntegerField(),
        ),
    ]
