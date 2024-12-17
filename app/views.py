# views.py

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Quiz, Pagina, Conteudo, Imagem,VideoAula  # Certifique-se de importar o modelo Quiz
def imagens(request):
    imagens = Imagem.objects.all()  # Pega todas as imagens
    return render(request, 'imagens.html', {'imagens': imagens})

def videoaulas(request):
    videos = VideoAula.objects.all()  # Pega todas as videoaulas
    return render(request, 'videoaulas.html', {'videos': videos})
def pagina_view(request, pagina_nome):
    pagina = get_object_or_404(Pagina, nome=pagina_nome)  # Obtém a página pelo nome
    conteudos = Conteudo.objects.filter(pagina=pagina)  # Obtém os conteúdos dessa página
    topicos = []  # Lista para armazenar os tópicos dos conteúdos
    
    # Iterar sobre os conteúdos para coletar seus tópicos
    for conteudo in conteudos:
        topicos.extend(conteudo.topicos.all())  # Adiciona os tópicos relacionados ao conteúdo
    
    # Passa a página, os conteúdos e os tópicos para o template
    return render(request, 'app/pagina.html', {
        'pagina': pagina,
        'conteudos': conteudos,
        'topicos': topicos,  # Adiciona os tópicos ao contexto
    })

def index(request):
    paginas = Pagina.objects.all()  # Busca todas as páginas no banco de dados
    return render(request, 'index.html', {'paginas': paginas})

class ReligiaoView(View):
    def get(self, request):
        return render(request, 'religiao.html')

class AmbienteView(View):
    def get(self, request):
        return render(request, 'ambiente.html')

class TecnologiaView(View):
    def get(self, request):
        return render(request, 'tecnologia.html')

class EsportesView(View):
    def get(self, request):
        return render(request, 'esportes.html')

class ArteView(View):
    def get(self, request):
        return render(request, 'arte.html')

class DireitosView(View):
    def get(self, request):
        return render(request, 'direitos.html')

class MovimentosView(View):
    def get(self, request):
        return render(request, 'movimentos.html')

class EconomiaView(View):
    def get(self, request):
        return render(request, 'economia.html')

class PoliticaView(View):
    def get(self, request):
        return render(request, 'politica.html')
class QuizView(View):
    # Método GET para exibir as perguntas
    def get(self, request):
        quizzes = Quiz.objects.all()  # Obtendo todas as perguntas do quiz
        return render(request, 'quiz.html', {'quizzes': quizzes, 'score': None, 'total': len(quizzes)})

    # Método POST para processar as respostas e exibir o resultado na mesma página
    def post(self, request):
        quizzes = Quiz.objects.all()  # Obtendo todas as perguntas do quiz
        score = 0
        
        # Iterando sobre todas as perguntas para verificar as respostas
        for quiz in quizzes:
            selected_answer = request.POST.get(f'question_{quiz.id}')  # Obtendo a resposta do usuário
            if selected_answer == quiz.resposta_correta:  # Verificando se a resposta está correta
                score += 1  # Incrementando a pontuação
            
        # Retornando o resultado na mesma página
        return render(request, 'quiz.html', {'quizzes': quizzes, 'score': score, 'total': len(quizzes)})
