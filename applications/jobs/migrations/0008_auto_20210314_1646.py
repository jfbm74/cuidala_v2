# Generated by Django 3.1.7 on 2021-03-14 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_school'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['-id'], 'verbose_name': 'Estudio', 'verbose_name_plural': 'Estudios'},
        ),
    ]
