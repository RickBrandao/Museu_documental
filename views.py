from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def documentos(request):
    assuntos = [
        {
            'slug': 'paroquia-neves',
            'nome': 'Paróquia: Nossa Senhora das Neves',
            'desc': 'Registros da paróquia mais antiga da região.'
        },
        {
            'slug': 'paroquia-neves',
            'nome': 'Paróquia: Nossa Senhora das Neves',
            'desc': 'Registros da paróquia mais antiga da região.'
        },
        {
            'slug': 'paroquia-neves',
            'nome': 'Paróquia: Nossa Senhora das Neves',
            'desc': 'Registros da paróquia mais antiga da região.'
        },

    ]
    return render(request, 'documentos.html', {'assuntos': assuntos})

def sobre(request):
    return render(request, 'sobre.html')

def paroquia_neves(request):
    return render(request, 'documentos/paroquia_neves.html')