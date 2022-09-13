# Generated by Django 3.2.12 on 2022-09-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=100)),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]
