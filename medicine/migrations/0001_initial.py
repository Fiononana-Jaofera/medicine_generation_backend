# Generated by Django 4.2.11 on 2024-04-03 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medicine', models.ManyToManyField(through='medicine.Effect', to='medicine.medicine')),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.AddField(
            model_name='effect',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine'),
        ),
        migrations.AddField(
            model_name='effect',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.symptom'),
        ),
        migrations.AlterUniqueTogether(
            name='effect',
            unique_together={('medicine', 'symptom')},
        ),
    ]
