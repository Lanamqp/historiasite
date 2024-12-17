from django.urls import path
from django.contrib import admin
from .views import QuizView  # Certifique-se de que existe uma QuizView no views.py
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Usa a função index diretamente
    path('pagina/<str:pagina_nome>/', views.pagina_view, name='pagina'),  # Página selecionada
    path('admin/', admin.site.urls),
    path('religiao/', views.ReligiaoView.as_view(), name='religiao'),
    path('ambiente/', views.AmbienteView.as_view(), name='ambiente'),
    path('tecnologia/', views.TecnologiaView.as_view(), name='tecnologia'),  # Corrigido o nome do path
    path('esportes/', views.EsportesView.as_view(), name='esportes'),
    path('arte/', views.ArteView.as_view(), name='arte'),
    path('direitos/', views.DireitosView.as_view(), name='direitos'),
    path('movimentos/', views.MovimentosView.as_view(), name='movimentos'),
    path('economia/', views.EconomiaView.as_view(), name='economia'),  # Corrigido para letra minúscula
    path('politica/', views.PoliticaView.as_view(), name='politica'),
    path('quiz/', QuizView.as_view(), name='quiz'), 
    path('imagens/', views.imagens, name='imagens'),
    path('videoaulas/', views.videoaulas, name='videoaulas'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)