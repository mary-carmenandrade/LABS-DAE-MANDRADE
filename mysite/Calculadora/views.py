from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<center><h1>Puede realizar sumas, restas, multiplicaciones y diviciones de dos numeros!<h1><center>")


def sumar(request, numero1, numero2):
    num1 = int(numero1)
    num2 = int(numero2)
    resultado = num1+num2
    return HttpResponse("La suma de %s " % numero1 +" + %s "  % numero2 + " = %s " % resultado)

def restar(request, numero1, numero2):
    num1 = int(numero1)
    num2 = int(numero2)
    resultado = num1-num2
    return HttpResponse("La resta de %s " % numero1 +" - %s "  % numero2 + " = %s " % resultado)

def multiplicar(request, numero1, numero2):
    num1 = int(numero1)
    num2 = int(numero2)
    resultado = num1*num2
    return HttpResponse("La multiplicación de %s " % numero1 +" * %s "  % numero2 + " = %s " % resultado)

def dividir(request, numero1, numero2):
   
    num1 = int(numero1)
    num2 = int(numero2)
    resultado = num1/num2
    return HttpResponse("La división de %s " % numero1 +" / %s "  % numero2 + " = %s " % resultado)
