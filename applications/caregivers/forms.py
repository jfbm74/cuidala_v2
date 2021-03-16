from django import forms
from applications.users.models import Work, School, Skill


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = (
            'employer',
            'work_title',
            'start_date',
            'end_date',
            'job_description',
            'location_id',
        )
        labels = {
            'employer': 'Empresa',
            'work_title': 'Cargo',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Fin',
            'job_description': 'Funciones realizadas',
            'location_id': 'Ciudad',
        }
        widgets = {
            'employer': forms.TextInput(
                attrs={
                    'class': 'contact-box',
                    'placeholder': 'Empresa donde laboraste',
                }
            ),
            'work_title': forms.TextInput(
                attrs={
                    'placeholder': 'Cargo que desempeñaste',
                    'class': 'contact-box'
                }
            ),
            'start_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'contact-box',
                }
            ),
            'end_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'contact-box',
                }
            ),
            'job_description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe tus actividades',
                    'rows': '3',
                    'class': 'contact-box',
                }
            ),
            'location_id': forms.Select(
                attrs={
                    'class': 'contact-box',
                }
            ),
        }


class NewSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = (
            'name',
            'study',
            'start_date',
            'end_date',
            'location_id'
        )
        labels = {
            'name': 'Institución',
            'study': 'Nombre del estudio',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Fin',
            'location_id': 'Ciudad',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'contact-box',
                    'placeholder': 'Instituto donde estudiaste',
                }
            ),
            'study': forms.TextInput(
                attrs={
                    'placeholder': 'Programa que estudiaste',
                    'class': 'contact-box'
                }
            ),
            'start_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'contact-box',
                }
            ),
            'end_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'contact-box',
                }
            ),
            'location_id': forms.Select(
                attrs={
                    'class': 'contact-box',
                }
            ),
        }
