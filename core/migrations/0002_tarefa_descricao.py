# Generated by Django 5.0.1 on 2024-01-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(default='descricao', max_length=5000),
            preserve_default=False,
        ),
    ]
