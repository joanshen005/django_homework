# Generated by Django 5.2.4 on 2025-07-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='kind',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
