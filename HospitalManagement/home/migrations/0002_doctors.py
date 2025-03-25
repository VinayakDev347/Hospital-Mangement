# Generated by Django 5.1.7 on 2025-03-25 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('doc_spec', models.CharField(max_length=255)),
                ('doct_image', models.ImageField(upload_to='doctors')),
                ('dop_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]
