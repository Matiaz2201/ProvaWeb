from django.db import models

# Create your models here.


class Alunos(models.Model):
    nome = models.CharField(max_length=40)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Disciplinas(models.Model):
    disciplina = models.CharField(max_length=50)

    def __str__(self):
        return self.disciplina


class Professores(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=100)
    titulacao = models.CharField(max_length=52)
    fone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome

class Matriculas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    ano = models.IntegerField()
    faltas = models.IntegerField()
    nota_final = models.FloatField()

    def __str__(self):
        return self.aluno.nome


class Alocacao(models.Model):
    professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    ano_letivo = models.DateField()
    carga = models.IntegerField()


    def __str__(self):
        retorno = self.professor.nome + ',' + self.disciplina.disciplina
        return retorno
