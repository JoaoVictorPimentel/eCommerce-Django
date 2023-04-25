from django.db import models

class Tenis(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='uploads/', null=True)
    def __str__(self) -> str:
        return self.nome
