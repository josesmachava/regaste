# Generated by Django 3.0.1 on 2020-01-09 00:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='payment',
            name='número_de_telefone',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="O número de telefone deve ser digitado no formato: '849394995'. São permitidos até 13 dígitos.", regex='^\\+?84?\\d{8,8}$')]),
        ),
    ]
