from dataclasses import field

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

class VisitorFormAuthorized(forms.ModelForm):
    resident_who_authorized = forms.CharField(required=True)

    class Meta:
        model = Visitor
        fields = ["resident_who_authorized"]
        error_messages = {
            "resident_who_authorized": {
                "required": "Por favor, informe o nome do morador resnponsável"
            }
        }

