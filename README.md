# Web Scraping dos indicadores fundamentalistas do site http://fundamentus.com.br
> Autor: Lucas da Silva dos Santos

>Dependências:   [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), 
[Requests](https://pypi.org/project/requests/), [Tqdm](https://pypi.org/project/tqdm/), 
[lxml](https://pypi.org/project/lxml/)



## Instalação das dependências:

>Para criar esse projeto, usei a versão do Python 3.8.1.

>As versão de cada dependência está contida nos links acima. 

```
pip install beautifulsoup4

pip install requests

pip install tqdm

pip install lxml
```


## Como usar:

Basta colocar todos os códigos das ações que pretende analisar no arquivo _"papeis.txt"_ (**um por linha**), e em seguida rodar o script _"fundamentus_api.py"_

Inicialmente possui a funcionalidade de trazer ao usuário, os dados das empresas de maneira organizada. Porém pode ser aplicada para várias outras funções, como atualização automática de planilhas no Excel ou Google Sheets.

## Resultado:

Como resultado o script exportará um arquivo no formato _.csv_ com todos os principais indicadores fundamentalistas das ações pré-selecionadas pelo usuário, direto do site _Fundamentus_. 



