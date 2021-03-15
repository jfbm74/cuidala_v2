from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .managers import UserManager


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Descripción', max_length=30)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['-id']

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    email = models.EmailField('Correo electrónico', unique=True)
    first_name = models.CharField('Nombres', max_length=50, blank=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True)
    legal_id = models.CharField('No Id', unique=True, max_length=10, blank=True)
    title = models.CharField('Profesión', max_length=100, null=True, blank=True)
    description_profile = models.TextField('Sobre mi', null=True, blank=True)
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES, null=True)
    caregiver = models.BooleanField('Is_Caregiver', default=False)
    patient = models.BooleanField('Is_Patient', default=False)
    address = models.CharField('Dirección', max_length=100, blank=True)
    phone = models.CharField('Numero Telefonico', max_length=15, blank=True)
    created_at = models.DateTimeField('Create at', default=datetime.now, blank=True)
    updated_at = models.DateTimeField('Updated at', default=datetime.now, blank=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='caregiver', blank=True, null=True)
    completed_profile = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill)
    services = models.ManyToManyField(Service)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-id']

    def __str__(self):
        return self.first_name


class School(models.Model):
    name = models.CharField(max_length=50)
    study = models.CharField(max_length=30)
    start_date = models.DateField(auto_created=True)
    end_date = models.DateField(auto_created=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        ordering = ['-end_date']

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Work(models.Model):
    employer = models.CharField("Empleador", max_length=30)
    work_title = models.CharField("Cargo", max_length=30)
    start_date = models.DateField("Fecha Inicio", )
    end_date = models.DateField("Fecha Finalización", )
    job_description = models.TextField("Descripción del Cargo",)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"
        ordering = ['-end_date']

    def __str__(self):
        return str(self.id) + ' ' + self.work_title
