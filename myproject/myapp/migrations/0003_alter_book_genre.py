# Generated by Django 5.1.4 on 2025-01-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_genre_alter_book_id_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
