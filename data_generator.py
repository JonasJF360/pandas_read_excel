""" importação das bibliotecas nescessárias """
import platform
import name_genertor as ng
import base.cpf_generator as cpf
from random import randint, uniform
import pandas as pd

# Configuracões para Windows e Linux
if str(platform.system()) == 'Linux':
    DIRETORIO = str(__file__).replace('main.py', 'base/')
else:  # O contrário foi pensado no Windows
    DIRETORIO = str(__file__).replace('main.py', 'base\\')

def my_uniform(x:float, y:float) -> float:
    """ Gera um número aleatório de ponto flutuante com 2 casas decimais """
    return round(uniform(x, y), 2)


def gerar_dados(quantidade: int) -> None:
    """ Função inicial do programa """
    database: dict = {
        'Nome': [],
        'Primeiro Nome': [],
        'CPF': [],
        'Idade': [],
        'Renda': [],
        'Patrimônio': [],
    }

    for _ in range(quantidade):
        temp_name: list = ng.generate_complit_name()
        database['Nome'].append(' '.join(temp_name).title())
        database['Primeiro Nome'].append(temp_name[0].title())
        database['CPF'].append(cpf.new_cpf())
        idade = randint(1, 125)
        database['Idade'].append(idade)
        controle = bool(randint(0, 1))
        renda = patrimonio = 0.0
        if idade > 14 and idade < 18:
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
    dados_garados.to_excel('Dados_Gerados.xlsx',sheet_name="Dados" , index=False)
      

if __name__ == '__main__':
    gerar_dados(100_000)