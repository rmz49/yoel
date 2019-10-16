from django import forms

class NameForm(forms.Form):
    pregunta = forms.CharField(label='Pregunta', max_length=100)
    fecha = forms.DateField(label='Fecha',required=True)
    hora = forms.TimeField(label='Hora', requires=True)