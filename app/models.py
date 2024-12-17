from django.db import models
import yt_dlp
import re

class Pagina(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(default="")
    texto = models.TextField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subcategorias"

    def __str__(self):
        return f"{self.categoria} - {self.nome}"

class Conteudo(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='conteudos', null=True)
    titulo = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_DEFAULT, default=1)
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='conteudos_imagens/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Conteúdos"

class Topico(models.Model):
    conteudo = models.ForeignKey(Conteudo, related_name='topicos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()

    def __str__(self):
        return self.titulo

class Quiz(models.Model):
    pergunta = models.CharField(max_length=300)
    alternativa_a = models.CharField(max_length=200, default="Alternativa A padrão")
    alternativa_b = models.CharField(max_length=200, default="Alternativa B padrão")
    alternativa_c = models.CharField(max_length=200, default="Alternativa C padrão")
    alternativa_d = models.CharField(max_length=200, default="Alternativa D padrão")
    resposta_correta = models.CharField(
        max_length=1,
        choices=[('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')]
    )
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return f"Quiz: {self.pergunta[:50]}..."
class VideoAula(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField()
    capa_video = models.URLField(blank=True, null=True)  # A URL da capa será gerada automaticamente
    descricao = models.TextField()

    def save(self, *args, **kwargs):
        # Se o link for do YouTube, gerar a capa automaticamente
        if 'youtube.com' in self.link:
            video_id = self.extract_youtube_video_id(self.link)
            if video_id:
                self.capa_video = f'https://img.youtube.com/vi/{video_id}/0.jpg'
        super().save(*args, **kwargs)

    def extract_youtube_video_id(self, url):
        """
        Função para extrair o ID do vídeo do YouTube a partir da URL.
        """
        match = re.search(r'(?:v=|\/)([a-zA-Z0-9_-]{11})', url)
        if match:
            return match.group(1)
        return None

    def __str__(self):
        return self.titulo
    
class Imagem(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField()

    def __str__(self):
        return self.titulo  