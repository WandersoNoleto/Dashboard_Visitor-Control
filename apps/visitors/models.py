from django.db import models


class Visitor(models.Model):

    VISITOR_STATUS = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada")
    ]

    status = models.CharField(
        verbose_name = "Status",
        max_length = 10,
        choices = VISITOR_STATUS,
        default = "AGUARDANDO"
    )


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
        auto_now_add = True
    )

    departure_time = models.DateTimeField(
        verbose_name = "Horário de saída",
        auto_now = False,
        blank = True,
        null = True
    )

    authorization_time = models.DateTimeField(
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

    def get_departure_time(self):
        if self.departure_time:
            return self.departure_time
        
        return "Não registrado"
    
    def get_authorization_time(self):
        if self.authorization_time:
            return self.authorization_time
        
        return "Aguardando autorização"
    
    def get_resident_who_authorized(self):
        if self.resident_who_authorized:
            return self.resident_who_authorized
        
        return "Aguardando autorização"
    
    def get_vehicle_plate(self):
        if self.vehicle_plate:
            return self.vehicle_plate
        
        return "Não registrado"

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_part_1 = cpf[0:3]
            cpf_part_2 = cpf[3:6]
            cpf_part_3 = cpf[6:9]
            cpf_part_4 = cpf[9:11]

            cpf_format = f"{cpf_part_1}.{cpf_part_2}.{cpf_part_3}-{cpf_part_4}"
            
            return cpf_format

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self) -> str:
        return self.personal_name
