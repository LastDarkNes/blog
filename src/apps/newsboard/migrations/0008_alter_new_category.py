# Generated by Django 3.2.13 on 2022-06-29 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsboard', '0007_auto_20210417_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsboard.category', verbose_name='Категория'),
        ),
    ]
