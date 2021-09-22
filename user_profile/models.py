from django.db import models
from django.contrib.auth.models import AbstractBaseUser #
from django.contrib.auth.models import PermissionsMixin #overwrite django models
from django.contrib.auth.models import BaseUserManager

from rest_framework.authtoken.models import Token



class UserProfileManager(BaseUserManager):
    
    """Manager for user profiles"""




    def create_user(self,email:str, password:str=None):
        """Create new user profile"""

        

        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email)


        user.set_password(password)
        user.save(using=self.db)

        token, created = Token.objects.get_or_create(user=user)
        print(f'Token desde el modelo: {token}')
        return user

    def create_superuser(self, email,password):
        user=self.create_user(email,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email=models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects= UserProfileManager()#when the client create user in Django CLI

    USERNAME_FIELD='email' #overwrite USERNAME_FIELD by default

    is_authenticated:bool = False
    
    
    ## NEW FIELDS
    
    
    """
    tipodocumentopersona = models.CharField(db_column='tipoDocumentoPersona',  max_length=70, blank=True, null=True)  # Field name made lowercase.
    numerodocumentopersona = models.IntegerField(db_column='numeroDocumentoPersona', blank=True, null=True)  # Field name made lowercase.
    nombrespersona = models.CharField(db_column='nombresPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    apellidospersona = models.CharField(db_column='apellidosPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    fechanacimientopersona = models.DateField(db_column='fechaNacimientoPersona', blank=True, null=True)  # Field name made lowercase.
    direccionpersona = models.CharField(db_column='direccionPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    generopersona = models.CharField(db_column='generoPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    lugarexpedicioncedulapersona = models.IntegerField(db_column='lugarExpedicionCedulaPersona', blank=True, null=True)  # Field name made lowercase.
    """

    class Meta:
        permissions = [('can_eat_pizzas', 'Can eat pizzas'), ('can_view_passagers','can view passagers')]


    def get_full_name(self):
        """Retrieve return full name user
        """
        return self.name

    def set_permissions_(self,perms:list):
        """setting  the permissions"""
        self.has_perms=perms 
    
    def __str__(self):
        """Return string representation of user"""
        return self.email