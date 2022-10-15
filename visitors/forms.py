from django import forms

from visitors.models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ["personal_name", "cpf", "birth_date", "house_number", "vehicle_plate"]
        error_messages = {
            "personal_name": {
                "required": "Nome completo é obrigatório para registro"
            },
            "cpf": {
                "required": "CPF é obrigatório para registro"
            },
            "birth_date": {
                "required": "Data de nascimento é obrigatória para registro",
                "invalid": "Por favor, informe uma data válida (DD/MM/AAAA)"
            },
            "house_number": {
                "required": "Informe o número da casa"
            }
        }
