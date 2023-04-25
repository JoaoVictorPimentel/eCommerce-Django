from django.shortcuts import render
from .forms import TenisForm
from .models import Tenis

def cadastrar_tenis(request):
    if request.method == 'POST':
        form = TenisForm(request.POST)
        if form.is_valid():
            Tenis.objects.create(
                nome = form.cleaned_data['nome'],
                valor = form.cleaned_data['valor']
        )
    else:
        form = TenisForm()
    return render(request, 'cadastrar_tenis.html', {'form':form})

def listar_tenis(request):
    listaTenis = Tenis.objects.all()
    context = {
        'listaTenis': listaTenis
    }
    return render(request, 'listar_tenis.html', context)

def detalhar_tenis(request, id):
    tenis = Tenis.objects.get(id=id)
    return render(request, 'detalhar_tenis.html', {'tenis': tenis})
