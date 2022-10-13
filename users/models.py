from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.model(
            email = self.normalize_email(email)
        )

        user.is_active    = True
        user.is_staff     = False
        user.is_superuser = False 

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password):
        superuser = self.create_user(
            email = self.normalize_email(email),
            password = password
        )

        superuser.is_active    = True
        superuser.is_staff     = True
        superuser.is_superuser = True 

        superuser.set_password(password)
        superuser.save()
        return superuser


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name = "E-mail do usuário",
        max_length = 194,
        unique = True
    )

    is_active = models.BooleanField(
        verbose_name = "Usuário está ativo",
        default = True
    )

    is_staff = models.BooleanField(
        verbose_name = "Usuário é da equipe de desenvolvimento",
        default = False
    )

    is_superuser = models.BooleanField(
        verbose_name = "Usuário é um superusuario",
        default = False
    )

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name        = "Usuário"
        verbose_name_plural = "Usuários"
        db_table            = "usuario"

    def __str__(self) -> str:
        return self.email
