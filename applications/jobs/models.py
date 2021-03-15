from django.db import models
from applications.users.models import (
    Skill,
    Service,
    User,
    Location,
)


# Create your models here.
class Jobs(models.Model):
    RECIPIENT_CHOICES = (
        ('0', 'Para mi'),
        ('1', 'Abuelo'),
        ('2', 'Abuela'),
        ('3', 'Madre'),
        ('4', 'Padre'),
        ('5', 'Hijo'),
        ('6', 'Hija'),
        ('7', 'Familiar'),
        ('7', 'Conocido'),

    )
    STATUS_CHOICES = (
        ('0', 'Inactivo'),
        ('1', 'Activo'),
        ('2', 'Contratado'),
        ('5', 'Pendiente'),
    )

    GENDER_PATIENT_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    description = models.CharField('Descripción', max_length=50, null=True);
    recipient_care = models.CharField('Destinatario', max_length=50, choices=RECIPIENT_CHOICES, null=True)
    start_date = models.DateField('Fecha Inicio', auto_created=True, null=True)
    end_date = models.DateField('Fecha Fin', auto_created=True, null=True)
    patient_gender = models.CharField('Género de Paciente', max_length=20, choices=GENDER_PATIENT_CHOICES, null=True)
    patient_phone = models.CharField('Teféfono del Paciente', max_length=20, null=True)
    patient_address = models.CharField('Dirección del Paciente', max_length=15, null=True)
    patient_age = models.IntegerField('Edad del Paciente', null=True)
    salary_min = models.IntegerField('Salario Mínimo', null=True)
    salary_max = models.IntegerField('Salario Máximo', blank=True, null=True)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('Creado en', auto_created=True, null=True)
    updated_at = models.DateTimeField('Actualizado en', auto_now_add=True)
    care_category = models.ManyToManyField(Skill)
    service_category = models.ManyToManyField(Service)

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"
        ordering = ['description']

    def __str__(self):
        return str(self.id)



