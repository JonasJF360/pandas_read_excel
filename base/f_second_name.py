""" Importação da função que verifira duplicidades. """
import verificar_duplicidades as vd

base_f_second_name: list = [
    'claudia',
    'fernanda',
    'gisela',
    'iasmyn',
    'jaqueline',
    'lorena',
    'maria',
    'nicóly',
    'paula',
    'renata',
    'vitória',
    'yasmin',
]

if __name__ == '__main__':
    # Testar se tem nomes tepetidos
    print(vd.valores_duplicados(base_f_second_name))