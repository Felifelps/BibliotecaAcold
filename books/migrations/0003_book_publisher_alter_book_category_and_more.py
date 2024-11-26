# Generated by Django 5.1.2 on 2024-11-26 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_quantity'),
        ('categories', '0005_alter_category_description'),
        ('locations', '0001_initial'),
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publishers', to='publishers.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='locations.location'),
        ),
    ]