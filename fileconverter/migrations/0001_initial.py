# Generated by Django 2.1.1 on 2019-07-07 22:45

import converter.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(storage=converter.storage_backends.CsvStorage(), upload_to='')),
            ],
        ),
    ]
