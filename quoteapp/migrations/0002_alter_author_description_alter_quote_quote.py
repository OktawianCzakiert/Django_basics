# Generated by Django 5.0.1 on 2024-01-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(),
        ),
    ]
