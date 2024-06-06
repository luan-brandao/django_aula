from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('<int:evento_id>/excluir/', views.excluir_evento, name='excluir_evento'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('todos/', views.todos_eventos, name='todos_eventos'),
]
