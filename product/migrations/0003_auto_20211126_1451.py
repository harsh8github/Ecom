# Generated by Django 2.1.5 on 2021-11-26 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211125_1751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='categorie',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.categorie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
