# Generated by Django 5.1.2 on 2024-10-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_category_name_alter_category_cdd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]