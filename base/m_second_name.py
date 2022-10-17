""" Importação da função que verifira duplicidades. """
import verificar_duplicidades as vd

base_m_second_name: list = [
    'alonsso',
    'carlos',
    'daniel',
    'gabriel',
    'henrique',
    'iury',
    'junior',
    'otávio',
    'vinicius',
    'yuri',
]

if __name__ == '__main__':
    ## Testar se tem nomes tepetidos
    print(vd.valores_duplicados(base_m_second_name))