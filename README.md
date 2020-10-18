<p align="center"><img height="%30" width ="30%" src="labhd.png"/></p>

# Twitterscraper-LABHD

___

>**A ferramenta foi desenvolvida apenas para pesquisas acadêmicas, sem fins lucrativos.**

___

Esse script foi pensado como uma ferramenta metodológica da pesquisa em humanidades digitais. Sua criação é fruto das reflexões e experiências empíricas de historiadores e sociológos que têm enfrentado o [desafio de fazer ciências humanas no mundo digital](http://bibliotecadigital.fgv.br/ojs/index.php/reh/article/view/79933).
Defendemos a importância da apropriação, uso, desenvolvimento e aprimoramento de ferramentas digitais para as humanidades, assim como a urgência na sofisticação teórica, metodológica e epistemológica sobre as chamadas Humanidades Digitais.

----

Código em Python 3.8 para raspagem de dados do Twitter usando a biblioteca twint.

Neste repositório você encontra dois scripts: 

1. Script para raspagem de uma lista de termos ou usuários. Necessidade de configuração dos parâmetros no próprio código;

2. Script para busca de termo ou de usuário através de inserção dos parâmetros ao rodar o programa. Ideal para usuários iniciantes. 

## INSTALAÇÃO

Para executar o twitterscraper, vc precisa acessar a pasta da ferramenta no [Github](https://github.com/ericbrasiln/twitterscraper). Clone ou faça download do repositório e salve na pasta que deseja que os resultados e seus respectivos arquivos sejam armazenados. Antes de executar o script, é preciso preparar seu computador, como mostramos abaixo.

### PYTHON

A ferramenta consiste num script escrito em [Python 3.8](https://www.python.org/). Esta é uma linguagem de programação que te permite trabalhar rapidamente e integrar diferentes sistemas com maior eficiência.
Para executar o arquivo .py é preciso instalar o Python3 em seu computador.

[Clique aqui](https://python.org.br/instalacao-windows/) para um tutorial de instalação do Python no Windows, [clique aqui](https://python.org.br/instalacao-linux/) para Linux e [clique aqui](https://python.org.br/instalacao-mac/)
para Mac.

Após a instalação, vc pode executar o arquivo .py direto do prompt de comando do Windows ou pelo terminal do Linux, ou utilizar as diversas [IDE](https://pt.wikipedia.org/wiki/Ambiente_de_desenvolvimento_integrado) disponíveis.Exemplo de como executar utilizando o terminal do Linux, após instalar o Python3.8:

1. Acesse o diretório em que o arquivo .py está salvo:
   
   ```sh
   $ cd user/local
   ```
2. Instale as bibliotecas requeridas:
   
   ```sh
   $ pip3 install -r requirements.txt
   ```
3. Execute o arquivo usando Python3.8
   
   ```python
   $ python twitter-scraper.py
   ```

### Twint

O Twint é uma ferramenta de raspagem de tweets escrita em Python que não necessita usar o API do Twitter.

Seu uso é prático (podendo ser usado com linhas de comando no terminal) e também na criação de scripts com configurações mais complexas.

Para maiores informações, visite o [repositório do Twint no Github](https://github.com/twintproject/twint))

Para instalar o Twint ek seu computador (caso a isntalação via requirements.txt não tenha funcionado), execute o seguinte comando no terminal:

~~~
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
~~~

## Resultados

O script gera um arquivo **CSV** (*comma-separated values*) contendo os seguintes: 

- id

- conversation_id

- created_at

- date 

- time

-  timezone

-  user_id

-  username

-  name

-  place

- tweet 

- language 

- mentions 

- urls 

- photos 

- replies_count 

- retweets_count 

- likes_count 

- hashtags 

- cashtags

- link

- retweet 

- quote_url 

- video 

- thumbnail 

- near

- geo 

- source 

- user_rt_id 

- user_rt 

- retweet_id 

- reply_to 

- retweet_date 

- translate 

- trans_src 

- trans_dest

OBS: O modo de separação do CSV é `TAB`

Cada busca também gera um relatório em `txt` da pesquisa contendo todos os parêmtros definidos:

- Termo da busca;

- Usuário buscado; 

- Data e hora da busca;

- Idioma da busca;

- Data do início da busca;

- Data do final da busca;

- Nome da pasta

## Licença

MIT licensed

Copyright (C) 2020 [Eric Brasil](https://github.com/ericbrasiln), [LABHD-UFBA](http://labhd.ufba.br/)
