# Generated by Django 4.0.3 on 2022-03-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_tax_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.CharField(max_length=300),
        ),
    ]
