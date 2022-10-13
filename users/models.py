from email.policy import default
from statistics import mode
from tabnanny import verbose

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True
    )

    is_active = models.BooleanField(
        verbose_name ="Usuário está ativo",
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_NAME="Usuário é um superusuario",
        default=False
    )

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name= "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuário"

    def __str__(self) -> str:
        return self.email
