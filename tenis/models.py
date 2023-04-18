from django.db import models

class NovoTenis(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.FloatField()
    def __str__(self) -> str:
        return self.nome
