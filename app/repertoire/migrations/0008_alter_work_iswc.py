# Generated by Django 4.0.3 on 2022-03-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0007_alter_proprietary_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='iswc',
            field=models.CharField(max_length=13),
        ),
    ]
