from django import forms
from applications.jobs.models import Jobs


class JobRegisterForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = (
            'description',
            'recipient_care',
            'start_date',
            'end_date',
            'patient_gender',
            'patient_phone',
            'patient_address',
            'patient_age',
            'location_id',
            'care_category',
            'service_category',
            'salary_min',
        )
        labels = {
            'description': 'Descripción / Titulo',
            'recipient_care': 'Paciente',
            'start_date': 'Fecha comienzo del trabajo',
            'end_date': 'Fecha final del trabajo',
            'patient_age': 'Edad del Paciente',
            'patient_gender': 'Sexo del Paciente',
            'patient_phone': 'Teléfono del Paciente',
            'patient_address': 'Dirección del Paciente',
            'salary_min': 'Tarifa/Hora Ofrecida',
            'location_id': 'Ciudad',
            'care_category': 'Tipo de cuidado para Paciente:',
            'service_category': 'Servicios requeridos',
        }
        widgets = {
            'start_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',

                }
            ),
            'end_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',

                }
            ),
            'salary_min': forms.NumberInput(
                attrs={

                }
            ),

        }
