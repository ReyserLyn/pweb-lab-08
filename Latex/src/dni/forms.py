from django import forms

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.setdefault('autocomplete', 'off')

class LoginForm(BaseForm):
    dni = forms.CharField(label="DNI", max_length=8, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu DNI',
        'data-lpignore': 'true',
    }))
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Introduce tu contraseña',
        'data-lpignore': 'true',
    }))
    
class RegisterForm(BaseForm):
    dni = forms.CharField(label="DNI", max_length=8, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu DNI',
    }))
    nombres = forms.CharField(label="Nombres", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tus nombres',
    }))
    apellido_paterno = forms.CharField(label="Apellido Paterno", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu apellido paterno',
    }))
    apellido_materno = forms.CharField(label="Apellido Materno", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu apellido materno',
    }))
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Crea tu contraseña',
    }))