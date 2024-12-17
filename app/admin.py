from django.contrib import admin
from .models import Categoria, Subcategoria, Conteudo, Quiz, Pagina, Topico, Imagem, VideoAula

# Definindo o Inline de Tópicos para adicionar aos conteúdos
class TopicoInline(admin.TabularInline):
    model = Topico
    extra = 1  # Número de tópicos em branco que aparecerão para adicionar

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "categoria"]
    search_fields = ["nome"]

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "data_publicacao", "categoria", "subcategoria", "pagina"]
    search_fields = ["titulo"]
    list_filter = ["pagina", "categoria", "subcategoria"]
    inlines = [TopicoInline]  # Adiciona os tópicos ao conteúdo

class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "pergunta", "conteudo"]
    search_fields = ["pergunta"]

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Não tem mais o inline de tópicos
    search_fields = ['nome', 'descricao']

# Registrando os modelos com as classes de admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Topico)
admin.site.register(Imagem)
admin.site.register(VideoAula)
