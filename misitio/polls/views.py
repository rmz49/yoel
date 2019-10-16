from django.http import HttpResponse

from polls.models import Pregunta

from django.template import loader

def agregar_preguntas(request):
	template=loader.get_template('polls/agregar_preguntas.html')
	context={}
	return HttpResponse(template.render(context,request))

def validar_formulario(request):
	c1=request.POST.get('campo1')
	c2=request.POST.get('campo2')
	if c1.strip() == "" or c2.strip()=="":
		return HttpResponse('debe llenar todos los campos')


def index(request):
	preguntas = Pregunta.objects.order_by('-fecha')[:5]
	template = loader.get_template('polls/index.html')
	context = { 'listado': preguntas,}
	return HttpResponse(template.render(context, request))

def detalle(request, id_pregunta):
	pregunta = Pregunta.objects.get(id=id_pregunta)
	template = loader.get_template('polls/detalle.html')
	context = { 'pregunta': pregunta }
	return HttpResponse(template.render(context, request))

def resultados(request, total):
    latest_question_list = Pregunta.objects.order_by('fecha')[:total]
    output = ', '.join([q.descripcion for q in latest_question_list])
    return HttpResponse(output)

"""
	-Construir una vista que retorne todas las opciones asociadas a una pregunta
	*FILTRAR POR ID DE PREGUNTA
"""