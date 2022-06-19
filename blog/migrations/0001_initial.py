# Generated by Django 3.2.13 on 2022-06-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('job', models.CharField(max_length=250)),
                ('salary', models.IntegerField(null=True)),
            ],
        ),
    ]