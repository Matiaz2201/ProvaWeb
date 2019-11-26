from django.contrib import admin
from .models import Aluno, Disciplina, Professor, Matricula, Alocacao

# Register your models here.

@admin.register(Aluno)
class lista_aluno(admin.ModelAdmin):
    list_display = ['id', 'nome']


@admin.register(Disciplina)
class lista_disciplina(admin.ModelAdmin):
    list_display = ['id', 'titulo_dis']


@admin.register(Professor)
class lista_professor(admin.ModelAdmin):
    list_display = ['id', 'nome_prof', 'end', 'titulacao', 'fone']

@admin.register(Matricula)
class lista_disciplina(admin.ModelAdmin):
    list_display = ['id', 'nome_aluno', 'titulo_disciplina', 'faltas', 'ano', 'nota_final']

@admin.register(Alocacao)
class lista_disciplina(admin.ModelAdmin):
    list_display = ['id', 'nome_prof', 'titulo_disc', 'horario', 'ano_letivo', 'carga']



