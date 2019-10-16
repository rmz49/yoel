from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # ex: /encuestas/2/
    path('<int:id_pregunta>/', views.detalle, name='detalle'),

    # ex: /encuestas/5/resultados/
    path('<int:total>/resultados/', views.resultados, name='resultados'),

    #ex: /encuestas/agregar_preguntas/
    path('agregar_preguntas/', views.agregar_preguntas,name='agregar_preguntas'),

    #ex: /encuestas/validar_formulario/
    path('validar_formulario/', views.validar_formulario,name='validar_formulario'),
]