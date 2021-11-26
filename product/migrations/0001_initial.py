# Generated by Django 2.1.5 on 2021-11-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=1)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
