from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UsuarioManager(BaseUserManager):
  def _create_user(self,username,email,nombres,apellidos,password,is_staff,is_superuser,**extra_fields):
    usuario = Usuario(username=username,email=self.normalize_email(email),nombres=nombres,apellidos=apellidos,password=password,is_staff=is_staff,is_superuser=is_superuser,**extra_fields)
    usuario.set_password(password)
    usuario.save()
    return usuario
  
  def create_user(self,username,email,nombres,apellidos,password=None,**extra_fields):
    return self._create_user(username,email,nombres,apellidos,password,False,False,**extra_fields)
  def create_superuser(self,username,email,nombres,apellidos,password=None,**extra_fields):
    return self._create_user(username,email,nombres,apellidos,password,True,True,**extra_fields)

ROLES = [
  ('Secretaría', 'Secretaría'),
  ('Profesional médico', 'Profesional médico'),
  ('Ventas', 'Ventas'),
  ('Técnico', 'Técnico'),
  ('Gerencia', 'Gerencia'),
]

class Usuario(AbstractBaseUser,PermissionsMixin):
  username = models.CharField("nombre de usuario", unique=True, max_length=50)
  email = models.EmailField("correo electronico", unique=True)
  nombres = models.CharField("nombres",max_length=150, blank=True )
  apellidos = models.CharField("apellidos",max_length=150, blank=True,null=True )
  rol = models.CharField(max_length=30 ,choices=ROLES, default='Secretaría')
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  objects = UsuarioManager()


  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email','nombres','apellidos']

  def __str__(self):
    return f'usuarios: {self.username}'







 