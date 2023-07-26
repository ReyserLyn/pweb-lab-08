from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, dni, nombres, apellido_paterno, apellido_materno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)

        if not dni:
            raise ValueError('El DNI debe ser proporcionado.')

        user = self.model(
            dni=dni,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, nombres, apellido_paterno, apellido_materno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(dni, nombres, apellido_paterno, apellido_materno, password, **extra_fields)

    def authenticate_user(self, dni=None, password=None):
        try:
            user = self.get(dni=dni)
            if user.password == password:
                return user
            return None
        except self.model.DoesNotExist:
            return None

class userData(AbstractBaseUser, PermissionsMixin):
    dni = models.CharField(max_length=8, unique=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True)  

    objects = UserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno']

    def __str__(self):
        return self.dni
