# Generated by Django 5.1.6 on 2025-02-16 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='publication_year',
        ),
    ]
