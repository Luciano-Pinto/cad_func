from django.forms import ModelForm

from .models import Setor, Funcionario


class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'