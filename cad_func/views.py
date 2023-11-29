from django.shortcuts import render, redirect

from .forms import SetorForm, FuncionarioForm
from .models import Setor, Funcionario


def home(request):
    return render(request, 'cad_func/home.html')


def setor_list(request):
    setores = Setor.objects.all()
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


def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionarios': funcionarios,
    }
    return render(request, 'cad_func/funcionarios.html', context)


def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('cad_func:funcionarios')
            except Exception as e:
                pass
    else:
        form = FuncionarioForm()

    context = {
        'form': form,
    }
    return render(request, 'cad_func/funcionario_create.html', context)


def funcionario_update(request, id):
    funcionario = Funcionario.objects.get(pk=id)
    form = FuncionarioForm(
        initial={
            'nome': funcionario.nome,
            'cargo': funcionario.cargo,
            'data_contratacao': funcionario.data_contratacao,
            'setor': funcionario.setor,
        },
    )

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('cad_func:funcionarios')
            except Exception as e:
                pass

    context = {
        'form': form,
    }
    return render(request, 'cad_func/funcionario_update.html', context)


def funcionario_delete(request, id):
    funcionario = Funcionario.objects.get(pk=id)

    try:
        funcionario.delete()
    except Exception as e:
        pass

    return redirect('cad_func:funcionarios')
