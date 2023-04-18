from django.shortcuts import render
from .forms import TenisForm
from .models import NovoTenis

def cadastrar_tenis(request):
    if request.method == 'POST':
        form = TenisForm(request.POST)
        if form.is_valid():
            NovoTenis.objects.create(
                nome = form.cleaned_data['nome'],
                valor = form.cleaned_data['valor']
        )
    else:
        form = TenisForm()
    return render(request, 'cadastrar_tenis.html', {'form':form})

def listar_tenis(request):
    context = {
        'listaTenis': listaTenis
    }
    return render(request, 'listar_tenis.html', context)

def detalhar_tenis(request, id):
    tenis = listaTenis[id-1]
    return render(request, 'detalhar_tenis.html', {'tenis': tenis})