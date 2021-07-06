from django.urls import path
from .views import index,contato,produto

from django.conf import settings
from django.conf.urls.static import static
# imports feitos após criação do diretótio media no settings


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    # 'produto/' -> como vai ficar em http://127.0.0.1/produto/
    # produto -> nome da views
    # name='produto' -> como chamar essa rota no html
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  # usado para que seja possível fazer acesso nos templates dos arquivos de media que serão feitos os uploads
  # como se estivesse criando uma rota, mas ao invés de criar uma rota já utiliza uma rota existente do próprio static

