from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf" : "CPF invalido"})
        if not rg_valido(data["rg"]):
            raise serializers.ValidationError({"rg" : "O Rg deve ter 9 digitos"})
        if not nome_valido(data["nome"]):
            raise serializers.ValidationError({"nome" : "Não pode incluir numeros neste campo"})
        if not celular_valido(data["celular"]):
            raise serializers.ValidationError({"celular" : "O número de celular deve estar formatado corretamente: xx 9xxxx-xxxx"})
        return data
        
    

