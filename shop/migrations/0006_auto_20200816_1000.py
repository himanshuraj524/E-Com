# Generated by Django 3.0.6 on 2020-08-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200816_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
