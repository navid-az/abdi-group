# Generated by Django 4.0.4 on 2022-05-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MrDr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
    ]
