# Generated by Django 4.2.11 on 2024-04-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='symptom',
            unique_together={('name',)},
        ),
    ]
