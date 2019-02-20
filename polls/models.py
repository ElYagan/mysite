import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def publicadarecientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class CL_CHASIS(models.Model):
    id = models.IntegerField
    Ano = models.IntegerField
    NumChasis = models.IntegerField
    CodArticulo = models.CharField(max_length=30)
    CodOT = models.CharField(max_length=30)
    CodSv = models.CharField(max_length=15)
    Usuario = models.CharField(max_length=50)
    FechaCreaChasis = models.DateField('Fecha Creado')
    Descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'CL_CHASIS'

    def __str__(self):
        return self.CodSv
