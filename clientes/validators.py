from rest_framework import serializers
import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

        
def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def nome_valido(nome):
    return nome.isalpha()

def celular_valido(numero_do_celular):
    """verifica se o celular é valido"""
    modelo = r"[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, numero_do_celular)
    return resposta

