from django.contrib import admin
from .models import Alunos, Disciplinas, Professores, Matriculas, Alocacao

# Register your models here.

@admin.register(Alunos)
class Alunos(admin.ModelAdmin):
    list_display = ['id', 'nome']


@admin.register(Disciplinas)
class Disciplinas(admin.ModelAdmin):
    list_display = ['id', 'disciplina']


@admin.register(Professores)
class Professores(admin.ModelAdmin):
    list_display = ['id', 'nome', 'endereco', 'titulacao', 'fone']

@admin.register(Matriculas)
class Matriculas(admin.ModelAdmin):
    list_display = ['id', 'aluno', 'disciplina', 'faltas', 'ano', 'nota_final']

@admin.register(Alocacao)
class Alocacao(admin.ModelAdmin):
    list_display = ['id', 'professor', 'disciplina', 'horario', 'ano_letivo', 'carga']
