# Pandas write excel
## Visão geral:
Esse é um aplicativo que gera uma lista completa de nomes fictícios e gera uma planilha com os dados.

## Detalhes do programa:
O intuito principal aqui é ter a possibilidade de gerar uma lista considerável de dados em uma planilha de excel de uma forma automatizada, e usando pandas juntamente com python isso é possível.
Isso certamente é bem útil para simulações, mas o foco principal desse app é simplesmente a construção dessa funcionalidade.
Se você, assim como eu gosta muito de programação e de python, te convido para dar uma estudada nesse conteúdo que tentarei deixar o mais esclarecido possível.

## Bibliotecas necessárias:

> ### Observação importante: Estou usando linux (Pop_OS) para programar, e por padrão ele vem com o Python na versão 3.10, e no linux(Pelo menos no que eu uso) precisa informar a versão do python na hora de executar comandos, então, quando eu usar **pip3** ou **python3** nos comando, quem usa windows pode usar somente **pip** ou **python**.
> ### Outro fato é que estou usando o **Visual Studio Code**, e por isso fiz a configuração do ambiente virtual manualmente, caso esteja utilizando uma IDE que já faz a virtualização como o **PyCharm** faça somente a instalação do pandas.


- ## **Pandas (Para manipular a(s) planilha(s))**

   - ```pip3 install pandas```

- ## **Openpyxl (Para manipular a(s) planilha(s))**
     - provavelmente irá precisar desse pacote se tiver usando Linux.
     - ```pip3 install openpyxl```

- ## **Python venv enviroment (Para criar o ambiente virtual)**
> Pode ser usado sem problemas qualquer outro recurso para virtualização como o **Virtualenv**, irei utilizar o **python venv** somente por preferência.

- AMBIENTE VIRTUAL PYTHON3 NO LINUX:

    - Linux terminal: ```sudo apt install python3.x-venv```

> **Manual para instalação e uso em outros sistemas** [**clique aqui.**](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

- CRIANDO VIRTUALIZAÇÃO PELO TERMINAL:

    - Linux terminal: ```cd caminho/do/projeto```

    - ```python3 -m venv venv```   |   _(Também pode ser `python -m venv outro_nome`)_

    - Windous cmd: ```cd caminho\do\projeto```

    - ```py -m venv venv```

- ABRINDO O AMBIENTE VIRTUAL:

    - ```source venv/bin/activate```

- FECHANDO O AMBIENTE VIRTUAL:

    - ```deactivate```
