from django.db import models


class Concierge(models.Model):

    user = models.OneToOneField(
        "users.User",
        verbose_name = "Usuario",
        on_delete = models.PROTECT
    )

    personal_name = models.CharField(
        verbose_name = 'Nome completo',
        max_length = 70
        )
    
    cpf = models.CharField(
        verbose_name = "CPF",
        max_length=11
    )

    phone = models.CharField(
        verbose_name = "Telefone de contato",
        max_length = 11
    )

    birth_date = models.DateField(
        verbose_name = "Data de nascimento",
        auto_now = False,
        auto_now_add = False
    )


    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self) -> str:
        return self.personal_name
