# Generated by Django 4.1.6 on 2023-04-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
