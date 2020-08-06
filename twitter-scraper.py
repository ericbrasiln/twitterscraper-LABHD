import twint
from datetime import datetime
import time
import os

data = datetime.now()
timestr = time.strftime("%Y%m%d")

print('-Script para raspagem de dados do Twitter-\n'
      'Defina os parâmetros para sua busca.\n'
      'A saída gera um relatório da busca e um arquivo CSV com os dados.\n')

parametro = input('Busca por termo (1) ou por usuário (2) ou ambos (3)? ')
c = twint.Config() #configurar os parâmatros de busca do twint
if parametro == '1':
    busca = input('Digite o termo da busca: ')
    c.Search = "'"+busca+"'"
    c.Username = None
    nome = 's_'+busca+'_'+timestr    
    c.Output = os.path.join('DATA', nome) #pasta de saída
    if not os.path.exists(c.Output): #se a pasta não existe, cria a pasta DATA
        os.makedirs(c.Output)
    
elif parametro == '2':
    busca = input('Digite o nome do usuário: ')
    c.Search = None
    c.Username = busca
    nome = 'u_'+c.Username+'_'+timestr
    c.Output = os.path.join('DATA', nome)
    if not os.path.exists(c.Output):
        os.makedirs(c.Output)
else:
    buscaUser = input('Digite o nome do usuário: ')
    buscaTermo = input('Digite o termo da busca: ')
    c.Search = "'"+buscaTermo+"'"
    c.Username= buscaUser
    nome = 'u_s_'+c.Username+'_'+c.Search+'_'+timestr
    c.Output = os.path.join('DATA', nome)
    if not os.path.exists(c.Output):
        os.makedirs(c.Output)

lang = input('Digite o idioma da busca (pt, en, es, fr, todos): ')
if lang == 'todos':
    c.Lang = None
else:
    c.Lang = lang

período = input('Digite a data e hora de início da busca (AAAA-MM-DD HH:MM:SS'
                ' ou deixe em branco para ignorar esse parâmetro: ')
if período == '':
    c.Since = None
else:
    c.Since = período

períodoFinal = input('Digite a data e hora de final da busca (AAAA-MM-DD HH:MM:SS'
                ' ou deixe em branco para ignorar esse parâmetro: ')
if períodoFinal == '':
    c.Until = None
else:
    c.Until = períodoFinal

c.Store_csv = True #define o arquivo final como csv
c.Hide_output = True #esconde a raspagem em tempo real

 #imprime o resumo dos parâmetros
print('\n'
      '-Raspagem do Twitter-\n'
      'Termo da busca: {};\n'
      'Usuário buscado: {};\n'
      'Data e hora da busca: {}; \n'
      'Idioma da busca: {};\n'
      'Data do início da busca: {};\n'
      'Data do final da busca: {};\n'
      'Nome da pasta: {}.'.format(c.Search, c.Username, data, c.Lang, c.Since,
                                  c.Until, nome))  

time.sleep(1)

runScript = input('Tudo ok? (s/n): ').strip().lower()

#criação do relatório com os dados da busca:
reportPath = os.path.join(c.Output, 'relatório')
if runScript == 's':    
    relatório = open('{}_{}.txt'.format(reportPath, nome), 'w')
    relatório.write(
    '-Raspagem do Twitter-\n'
    'Termo da busca: {};\n'
    'Usuário buscado: {};\n'
    'Data e hora da busca: {}; \n'
    'Idioma da busca: {};\n'
    'Data do início da busca: {};\n'
    'Data do final da busca: {};\n'
    'Nome da pasta: {}.'.format(c.Search, c.Username, data, c.Lang, c.Since,
                                c.Until, nome))
    relatório.close
    twint.run.Search(c)
else:
    print('Reinicie o script.')
    exit()
    