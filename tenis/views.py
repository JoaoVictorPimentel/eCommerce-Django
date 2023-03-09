from django.shortcuts import render

listaTenis = [
    {
        'id': 1,
        'titulo': 'Tênis 1'
    },
    {
        'id': 2,
        'titulo': 'Tênis 2'
    },
    {
        'id': 3,
        'titulo': 'Tênis 3'
    }
]

def listar_tenis(request):
    context = {
        'listaTenis': listaTenis
    }
    return render(request, 'listar_tenis.html', context)

def detalhar_tenis(request, id):
    tenis = listaTenis[id-1]
    return render(request, 'detalhar_tenis.html', {'tenis': tenis})