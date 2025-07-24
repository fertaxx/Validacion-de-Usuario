from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del usuario
    correo = models.EmailField(unique=True)  # Correo electrónico único
    telefono = models.CharField(max_length=15)  # Teléfono del usuario
    contrasena = models.CharField(max_length=255)  # Contraseña encriptada

    def set_password(self, contrasena):
        """Encriptar la contraseña antes de guardarla"""
        self.contrasena = make_password(contrasena)
    
    def check_password(self, contrasena):
        """Verificar si la contraseña ingresada coincide con la almacenada"""
        return check_password(contrasena, self.contrasena)

    def __str__(self):
        return self.nombre