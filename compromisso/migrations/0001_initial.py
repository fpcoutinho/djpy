# Generated by Django 4.0.4 on 2022-05-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('obs', models.TextField(blank=True)),
                ('status', models.CharField(default='Agendado', max_length=20)),
                ('data_inicial', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
            ],
        ),
    ]
