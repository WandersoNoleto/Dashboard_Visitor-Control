from django.db import models


class Visitor(models.Model):

    personal_name = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length = 11
    )

    birth_date = models.DateField(
        verbose_name = "Data de nascimento",
        auto_now = False,
        auto_now_add = False
    )

    house_number = models.PositiveSmallIntegerField(
        verbose_name = "Número da casa a ser visitado"
    )

    vehicle_plate = models.CharField(
        verbose_name = "Placa de veiculo",
        max_length = 7,
        blank = True,
        null = True
    )


    arrival_time = models.DateTimeField(
        verbose_name = "Horário de chegada", 
        auto_now = False, 
        auto_now_add = False
    )

    departure_time = models.DateTimeField(
        verbose_name = "Horário de saída",
        auto_now = False,
        blank = True,
        null = True
    )

    autorization_time = models.DateTimeField(
        verbose_name = "Horário de autorização de entrada",
        auto_now = False, 
        blank = True,
        null = True
    )

    resident_who_authorized = models.CharField(
        verbose_name = "Morador responsável pela entrada do visitante",
        max_length = 194,
        blank = True
    )

    concierge = models.ForeignKey(
        'concierges.Concierge',
        verbose_name = "Porteiro que registrou",
        on_delete = models.PROTECT
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self) -> str:
        return self.personal_name
