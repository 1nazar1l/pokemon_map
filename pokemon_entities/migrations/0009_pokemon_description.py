# Generated by Django 3.1.14 on 2024-10-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20241005_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
