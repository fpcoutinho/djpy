# Generated by Django 4.0.4 on 2022-05-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compromisso', '0003_alter_compromisso_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compromisso',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
