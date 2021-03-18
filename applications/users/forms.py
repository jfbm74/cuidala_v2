from django import forms
from .models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.CharField(
        label='email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'email'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Error: El usuario o contraseña no son validos')
        return self.cleaned_data


class PatientRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )
    class Meta:
        """Meta definition for PatientRegisterForm"""
        model = User
        fields = (
            'first_name',
            'last_name',
            'legal_id',
            'email',
            'phone',
            'location_id',
        )
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'legal_id': 'Número de Identificación',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono de Contacto',
            'location_id': 'Ciudad',
        }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')


class CaregiverRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )
    class Meta:
        """Meta definition for PatientRegisterForm"""
        model = User
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'legal_id',
            'title',
            'description_profile',
            'email',
            'address',
            'phone',
            'location_id',
            # 'skills',
            # 'services',
        )
        labels = {
            'avatar': 'Foto',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'legal_id': 'Número de Identificación',
            'title': 'Tu Profesión u Ocupación',
            'description_profile': 'Descríbete a ti mismo(a)',
            'email': 'Correo Electrónico',
            'address': 'Dirección',
            'phone': 'Teléfono de Contacto',
            'location_id': 'Ciudad',
            # 'skills': 'Selecciona tus Habilidades o Esperiencia con Pacientes',
            # 'services': 'Selecciona los servicios en los que pueden contratarte',

        }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
