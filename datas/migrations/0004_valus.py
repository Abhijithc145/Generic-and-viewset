# Generated by Django 3.2.12 on 2022-09-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1', models.PositiveIntegerField(max_length=100)),
                ('value2', models.PositiveIntegerField(max_length=20)),
                ('value3', models.PositiveIntegerField(max_length=100)),
            ],
        ),
    ]
