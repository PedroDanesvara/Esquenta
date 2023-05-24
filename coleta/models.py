from django.db import models
from produtor.models import Pessoa

class Oferta(models.Model):
    tipo_material = models.CharField(max_length=50, help_text='Tipo de Material')
    estado = models.CharField(max_length=50, help_text='Condições do Produto')
    peso = models.FloatField(max_length=20, help_text='Peso do produto')
    valor = models.DecimalField(decimal_places=10, max_digits=10, help_text='Valor calculado pelo app')
    produtor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, help_text="Nome do Ofertante", related_name='ofertas')

