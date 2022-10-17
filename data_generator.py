""" importação das bibliotecas nescessárias """
import os
from random import randint, uniform
import platform
import pandas as pd
import name_genertor as ng
import base.cpf_generator as cpf

# Esse programa irá criar um arquivo de excel'.xlsx'
# que conterá uma quantidade x de nome de acordo com
# a especificaçõa enviada no paramento da função
# 'gerar_planilha_dados' e salva na pasta 'src'

# Configuracão do caminho completo para Windows e Linux
local_path: str = str(__file__).replace('data_generator.py', '')
DIRETORIO:str = local_path + 'src/' if str(platform.system()) == 'Linux' else local_path + 'src\\'

# Cria o diretório caso ainda não exista
if not os.path.exists(DIRETORIO):
    os.makedirs(DIRETORIO)


def my_uniform(valor_x: float, valor_y: float) -> float:
    """ Gera um número aleatório de ponto flutuante com 2 casas decimais """
    return round(uniform(valor_x, valor_y), 2)


def validar_nome(nome: str) -> str:
    """ Função que faz a validação do nome para evitar erros e define
    um tamanho máximo de 40 caracteres para o nome. """
    permitido = 'abcdefghijklmnopqrstuvwxyzçãáàéèêíìôõóòúù'
    permitido += permitido.upper() + '._-+'
    for i, caractere in enumerate(nome):
        if not caractere in permitido:
            nome = nome.replace(caractere, '_')
        if i > 40:
            break

    return nome[:40] if len(nome) > 40 else nome


def gerar_planilha_dados( tamanho_lista: int = 1, nome_arquivo: str ="Dados_Gerados") -> None:
    """ Função responsável por criar a planilha de acordo com o desejado """

    nome_arquivo = validar_nome(nome_arquivo)
    database: dict = {
        'Nome': [],
        'Primeiro Nome': [],
        'CPF': [],
        'Idade': [],
        'Renda': [],
        'Patrimônio': [],
    }

    for _ in range(tamanho_lista):
        temp_name: list = ng.generate_complit_name()
        database['Nome'].append(' '.join(temp_name).title())
        database['Primeiro Nome'].append(temp_name[0].title())
        database['CPF'].append(cpf.new_cpf())
        idade = randint(1, 125)
        database['Idade'].append(idade)
        controle = bool(randint(0, 1))
        renda = patrimonio = 0.0
        if 14 < idade < 18:
            if controle:
                renda = my_uniform(0, 5_000)
                patrimonio = my_uniform(0, 250_000)
            else:
                renda = my_uniform(0, 2_000)
                patrimonio = my_uniform(0, 100_000)
        elif idade >= 18:
            if controle:
                renda = my_uniform(0, 30_000)
                patrimonio = my_uniform(renda, 1_000_000)
            else:
                renda = my_uniform(0, 10_000)
                patrimonio = my_uniform(renda, 500_000)

        database['Renda'].append(renda)
        database['Patrimônio'].append(patrimonio)

    dados_garados = pd.DataFrame(data=database)
    dados_garados.to_excel(f'{DIRETORIO}{nome_arquivo}.xlsx',sheet_name="Dados" , index=False)
    print(f'> O arquivo "{nome_arquivo}.xlsx" foi salvo na pasta "src".')    
      

if __name__ == '__main__':
    gerar_planilha_dados(5000)
    # gerar_planilha_dados()
    # gerar_planilha_dados(5, 'novo')
    # gerar_planilha_dados(nome_arquivo="apenas um")
    # gerar_planilha_dados(5, 'tentando/errar')