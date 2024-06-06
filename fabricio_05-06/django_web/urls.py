from django.urls import path, include  # Adicione 'include' aqui
from eventos.views import lista_eventos  # Importe a view lista_eventos do seu aplicativo eventos

urlpatterns = [
    path('', lista_eventos, name='lista_eventos'),  # Defina uma rota vazia para a view lista_eventos
    path('eventos/', include('eventos.urls')),  # Inclua as URLs do aplicativo eventos
    # Outras URLs do seu projeto principal podem estar aqui
]
