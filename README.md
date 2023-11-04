# extracao-de-dados-web


## Documentação

Web Scraper feito por João Nunes, João Lucas e Lucas Vinínicios

O script pode ser configurado para varrer qualquer site, mas por padrão está configurado para o ```ingressoprime.com```

Ele vasculha o site, salva os dados em planilhas e depois passa todo os dados para as tabelas no banco de dados ```eventos.db```

Banco de dados utilizado foi o SQLITE3

### Como baixar dependencias
#### Abra um terminal na pasta do projeto e crie um ambiente virtual

    $ python -m venv venv

#### Ative ele usando:

Linux:

    $ source venv/bin/activate

Windows: 

    $ venv\Scripts\activate.bat

#### Instale o pip: 

ArchLinux:

    $ sudo pacman -S python-pip

Ubuntu: 

    $ sudo apt install python-pip

#### Agora é só instalar as dependências usando pip: 

    $ pip install pandas requests openpyxl bs4

#### Para iniciar o script:

    python3 main.py