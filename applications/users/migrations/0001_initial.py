# Generated by Django 3.1.7 on 2021-03-17 21:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Apellidos')),
                ('legal_id', models.CharField(blank=True, max_length=10, unique=True, verbose_name='No Id')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Profesión')),
                ('description_profile', models.TextField(blank=True, null=True, verbose_name='Sobre mi')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Genero')),
                ('caregiver', models.BooleanField(default=False, verbose_name='Is_Caregiver')),
                ('patient', models.BooleanField(default=False, verbose_name='Is_Patient')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Dirección')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Numero Telefonico')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Updated at')),
                ('is_staff', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='caregiver')),
                ('completed_profile', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=30, verbose_name='Empleador')),
                ('work_title', models.CharField(max_length=30, verbose_name='Cargo')),
                ('start_date', models.DateField(verbose_name='Fecha Inicio')),
                ('end_date', models.DateField(verbose_name='Fecha Finalización')),
                ('job_description', models.TextField(verbose_name='Descripción del Cargo')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trabajo',
                'verbose_name_plural': 'Trabajos',
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField(auto_created=True)),
                ('start_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('study', models.CharField(max_length=30)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
                'ordering': ['-end_date'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='location_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
        migrations.AddField(
            model_name='user',
            name='services',
            field=models.ManyToManyField(to='users.Service'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(to='users.Skill'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
