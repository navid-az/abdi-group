# Generated by Django 4.0.4 on 2022-04-29 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mr_dr', '0003_alter_mrdr_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrdr',
            name='created',
        ),
    ]