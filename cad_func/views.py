from django.shortcuts import render, redirect

from .forms import SetorForm
from .models import Setor


def home(request):
    return render(request, 'cad_func/home.html')


def setor_list(request):
    setores = Setor.objects.all().values()
    context = {
        'setores': setores,
    }
    return render(request, 'cad_func/setores.html', context)


def setor_create(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('cad_func:setores')
            except Exception as e:
                pass
    else:
        form = SetorForm()

    context = {
        'form': form,
    }
    return render(request, 'cad_func/setor_create.html', context)


def setor_update(request, id):
    setor = Setor.objects.get(pk=id)
    form = SetorForm(
        initial={
            'nome': setor.nome,
            'data_criacao': setor.data_criacao,
        },
    )

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)

        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('cad_func:setores')
            except Exception as e:
                pass

    context = {
        'form': form,
    }
    return render(request, 'cad_func/setor_update.html', context)


def setor_delete(request, id):
    setor = Setor.objects.get(pk=id)

    try:
        setor.delete()
    except Exception as e:
        pass

    return redirect('cad_func:setores')
