base_m_first_name: list = [
    'adamastor',
    'ademar',
    'adonis',
    'adriano',
    'adão',
    'angelo',
    'antônio',
    'armando',
    'benício',
    'bernardo',
    'carlos',
    'celio',
    'chico',
    'cloves',
    'damião',
    'daniel',
    'danilo',
    'diego',
    'dorival',
    'eberton',
    'edezio',
    'edicarlos',
    'edimar',
    'edivaldo',
    'elias',
    'emerson',
    'esmael',
    'fabiano',
    'fabrício',
    'felipe',
    'felix',
    'flávio',
    'gecinei',
    'gilberto',
    'gilmar',
    'gladson',
    'gleismar',
    'gleison',
    'henrique',
    'hermínio',
    'ícaro',
    'idemar',
    'igor',
    'indiano',
    'inácio',
    'italo',
    'jacinto',
    'jacó',
    'jhonatan',
    'jonas',
    'jonatan',
    'jorge',
    'josé',
    'joão',
    'jucelino',
    'juvencio',
    'kelson',
    'kelvin',
    'klayton',
    'laucir',
    'lourenço',
    'lourival',
    'lucas',
    'lucio',
    'madson',
    'maelson',
    'manoel',
    'marcelo',
    'marcos',
    'miqueias',
    'moizes',
    'naelson',
    'naldo',
    'nando',
    'naníbes',
    'neimar',
    'nelson',
    'nemias',
    'nene',
    'neymar',
    'nilton',
    'norberto',
    'obadias',
    'odair',
    'olinpio',
    'onorio',
    'osmar',
    'osvaldo',
    'oswaldo',
    'otávio',
    'paulo',
    'pedro',
    'petruquio',
    'quelvin',
    'querlyon',
    'queving',
    'rafael',
    'ralisson',
    'raphael',
    'reginaldo',
    'reinaldo',
    'renato',
    'rodrigo',
    'rogério',
    'roneide',
    'sandro',
    'sergio',
    'sidney',
    'silas',
    'silvio',
    'simão',
    'tavwelker',
    'tiago',
    'tião',
    'tonhão',
    'uelington',
    'ugo',
    'ulisses',
    'umberto',
    'vagner',
    'valdemar',
    'valdir',
    'vanderlei',
    'vando',
    'victor',
    'welington',
    'wilian',
    'willyan',
    'xico',
    'ytamar',
    'ytamiro',
    'yágo',
    'zenildo',
    'zeno',
    'zélio',
]

if __name__ == '__main__':
    # Testar se tem nomes tepetidos
    tirar_repetidos: set = set(base_m_first_name)

    print('[')
    for i in sorted(base_m_first_name):
        print(f"\t'{i}',")
    print(']')
    print(len(base_m_first_name))
    print(len(tirar_repetidos))
