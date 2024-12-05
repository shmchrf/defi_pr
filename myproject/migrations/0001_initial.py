# Generated by Django 5.1.3 on 2024-12-05 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HumanSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OceanSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarities', models.TextField()),
                ('consequences_of_dysfunction', models.TextField()),
                ('human_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.humansystem')),
                ('ocean_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.oceansystem')),
            ],
        ),
    ]
