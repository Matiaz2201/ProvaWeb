from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    titulo_dis = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo_dis


class Professor(models.Model):
    nome_prof = models.CharField(max_length=40)
    end = models.CharField(max_length=100)
    titulacao = models.CharField(max_length=52)
    fone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome_prof

class Matricula(models.Model):
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    titulo_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano = models.IntegerField()
    faltas = models.IntegerField()
    nota_final = models.FloatField()

    def __str__(self):
        return self.nome_aluno.nome


class Alocacao(models.Model):
    nome_prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
    titulo_disc = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    ano_letivo = models.DateField()
    carga = models.IntegerField()


    def __str__(self):
        retorno = self.nome_prof.nome_prof + ',' + self.titulo_disc.titulo_dis
        return retorno