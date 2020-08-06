import twint
from datetime import datetime
import time

data = datetime.now()
timestr = time.strftime("%Y%m%d")

parametro = input('Busca por termo (1) ou por usuário (2) ou ambos (3)? ')
c = twint.Config()
if parametro == '1':
    busca = input('Digite o termo da busca: ')
    c.Search = "'"+busca+"'"
    c.Username = None
    c.Output = 's_'+busca+'_'+timestr
elif parametro == '2':
    busca = input('Digite o nome do usuário: ')
    c.Search = None
    c.Username = busca
    c.Output = 'u_'+c.Username+'_'+timestr
else:
    buscaUser = input('Digite o nome do usuário: ')
    buscaTermo = input('Digite o termo da busca: ')
    c.Search = "'"+buscaTermo+"'"
    c.Username= buscaUser
    c.Output = 'u_s_'+c.Username+'_'+c.Search+'_'+timestr

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

c.Store_csv = True
c.Hide_output = True

print('\n'
      '-Raspagem do Twitter-\n'
      'Termo da busca: {};\n'
      'Usuário buscado: {};\n'
      'Data e hora da busca: {}; \n'
      'Idioma da busca: {};\n'
      'Data do início da busca: {};\n'
      'Nome da pasta: {}.'.format(c.Search, c.Username, data, c.Lang, c.Since, c.Output))

time.sleep(1)

runScript = input('Tudo ok? (s/n): ').strip().lower()
if runScript == 's':    
    relatório = open('relatório_{}.txt'.format(c.Output), 'w')
    relatório.write(
    '-Raspagem do Twitter-\n'
    'Termo da busca: {};\n'
    'Usuário buscado: {};\n'
    'Data e hora da busca: {}; \n'
    'Idioma da busca: {};\n'
    'Data do início da busca: {};\n'
    'Nome da pasta: {}.'.format(c.Search, c.Username, data, c.Lang, c.Since, c.Output)    
    )
    relatório.close
    twint.run.Search(c)
else:
    print('Reinicie o script.')
    exit()
    