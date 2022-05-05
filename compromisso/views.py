from django.shortcuts import render, redirect
from django import forms
from datetime import datetime
from .models import Compromisso
from . import forms as compr_forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def compromisso_list(request):
    usuario = request.user
    compromissos = Compromisso.objects.filter(autor=usuario).order_by('data_inicial')
    return render(request, 'compromisso/compromisso_list.html', {'compromissos': compromissos})


@login_required(login_url="/accounts/login/")
def compromisso_visualiza(request, comp_id):
    compromisso = Compromisso.objects.get(id=comp_id)
    return render(request, 'compromisso/compromisso_visualiza.html', {'compromisso': compromisso})


@login_required(login_url="/accounts/login/")
def compromisso_cria(request):
    if request.method == 'POST':
        form = compr_forms.CompromissoForm(request.POST)
        if form.is_valid():
            usuario = request.user

            # valida as datas do form
            dataini = datetime.strptime(request.POST['data_inicial'], '%d/%m/%Y %H:%M:%S')
            datafim = datetime.strptime(request.POST['data_final'], '%d/%m/%Y %H:%M:%S')
            if dataini < datetime.now():
                raise forms.ValidationError('Você está tentando criar um compromisso para uma data que já passou')
            if dataini > datafim:
                raise forms.ValidationError('A data final não pode ser anterior à data inicial')

            # checa se o compromisso dá choque com outros compromissos do usuário
            compromissos = Compromisso.objects.filter(autor=usuario)
            for compromisso in compromissos:
                if (dataini <= compromisso.data_inicial < datafim) or (dataini < compromisso.data_final <= datafim):
                    raise forms.ValidationError(
                        'As datas do compromisso atual se chocam com a do compromisso ' + compromisso.nome)

            # salva o compromisso na lista
            instance = form.save(commit=False)
            instance.autor = usuario
            instance.save()
            return redirect('compromisso:list')
    else:
        form = compr_forms.CompromissoForm()
    return render(request, 'compromisso/compromisso_cria.html', {'form': form})


@login_required(login_url="/accounts/login/")
def compromisso_deleta(request, comp_id):
    compromisso = Compromisso.objects.get(id=comp_id)
    compromisso.delete()
    messages.success(request, "Compromisso excluído!")
    return redirect('compromisso:list')

@login_required(login_url="/accounts/login/")
def compromisso_edita(request, comp_id):
    compromisso = Compromisso.objects.get(id=comp_id)
    form = compr_forms.CompromissoForm(request.POST or None, instance=compromisso)
    if form.is_valid():
        form.save()
        return redirect('compromisso:list')
    return render(request, 'compromisso/compromisso_edita.html', {'compromisso': compromisso,  'form':form})