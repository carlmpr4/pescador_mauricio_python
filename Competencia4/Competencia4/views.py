from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):

    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = "index.html"

    def post(self, request):
        return render(request)
    
    def get(self, request):
        datos = {'nombres':'Carlos Mauricio', 'primer_apellido':'Pescador', 'segundo_apellido':'Rosas', 'fecha_nacimiento':'30-Dic-1987', 'celular': 3314395799, 'correo':'carlmpr4@gmail.com', 'domicilio':'Mazatlan', 'genero':'Masculino', 'objetivo': 'Aprender Python', 'salario_esperado': 1000000}
        skills = list(('SQL', 'PLSQL','OBIEE','Python Basico' ))
        trabajo = {'lugar_trabajo': ['TCS','Oracle'], 'anio_inicio': [2010, 2012], 'anio_fin': [2012, 'Presente'], 'puesto': ['Trainee','Developer'] }
        return render(request,self.template_name, {
            'nombre': datos["nombres"],
            'primer_apellido': datos["primer_apellido"],
            'segundo_apellido': datos["segundo_apellido"],
            'fecha_nacimiento': datos["fecha_nacimiento"],
            'celular': datos["celular"],
            'correo': datos["correo"],
            'domicilio': datos["domicilio"],
            'genero': datos["genero"],
            'objetivo': datos["objetivo"],
            'salario_esperado': datos["salario_esperado"],
            'habilidades' : skills,
            'trabajo1_lugar' : trabajo["lugar_trabajo"][0],
            'trabajo1_fecinicio' : trabajo["anio_inicio"][0],
            'trabajo1_fecfin' : trabajo["anio_fin"][0],
            'trabajo1_puesto' : trabajo["puesto"][0],
            'trabajo2_lugar' : trabajo["lugar_trabajo"][1],
            'trabajo2_fecinicio' : trabajo["anio_inicio"][1],
            'trabajo2_fecfin' : trabajo["anio_fin"][1],
            'trabajo2_puesto' : trabajo["puesto"][1]



        })