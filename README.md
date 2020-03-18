# API não oficial do site http://fundamentus.com.br
> Autor: Lucas da Silva dos Santos

>Dependências:   [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), [Requests](https://pypi.org/project/requests/), [lxml](https://pypi.org/project/lxml/), [flask-restful](https://flask-restful.readthedocs.io/en/latest/)



## Instalação das dependências:

>Para criar esse projeto, usei a versão do Python 3.8.1.

>As versão de cada dependência está contida nos links acima. 

```
pip install beautifulsoup4

pip install requests

pip install flask-restful

pip install lxml
```


## Como usar:

Iniciar o servidor executando o script _"fundamentus_api.py"_

Com o servidor funcionando acesse-o passando o código do papel que deseja pesquisar como parametro. e.g.
```
127.0.0.1/bbas3
```

Inicialmente possui a funcionalidade de trazer ao usuário, os dados das empresas de maneira organizada. Porém pode ser aplicada para várias outras funções, como atualização automática de planilhas no Excel ou Google Sheets.

## Resultado:

Como resultado a API exportará um arquivo no formato _.csv_ com todos os principais indicadores fundamentalistas das ações pré-selecionadas pelo usuário, direto do site _Fundamentus_. 



