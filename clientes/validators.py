import re
from validate_docbr import CPF

#Validar CPF
def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

#Validar Nome
def nome_valido(nome):
    return nome.isalpha()

#Validar RG
def rg_valido(rg):
    return len(rg) == 9

#Validar Celular
def celular_valido(celular):
    """Verifica se o celular é valido (19 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
