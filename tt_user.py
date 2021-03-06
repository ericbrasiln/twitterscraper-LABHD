import twint
from datetime import datetime
import time
import os

data = datetime.now()
timestr = time.strftime("%Y%m%d")

print('-'*70)
print('-Script para raspagem de dados do Twitter-\n'
      'Defina os parâmetros para sua busca.\n'
      'A saída gera um relatório da busca e um arquivo CSV com os dados.\n')
print('-'*70)

parametro = input('Busca por termo (1) ou por usuário (2)? ')
c = twint.Config() #configurar os parâmatros de busca do twint
if parametro == '1':
    busca = input('Digite o termo da busca: ')
    c.Search = "'"+busca+"'"
    c.Username = None
    nome = busca+'_'+timestr    
    c.Output = os.path.join('DATA', nome) #pasta de saída
    if not os.path.exists(c.Output): #se a pasta não existe, cria a pasta DATA
        os.makedirs(c.Output)
    
elif parametro == '2':
    busca = input('Digite o nome do usuário: ')
    c.Search = None
    c.Username = busca
    nome = 'user_'+c.Username+'_'+timestr
    c.Output = os.path.join('DATA', nome)
    if not os.path.exists(c.Output):
        os.makedirs(c.Output)
else:
    print('Reinicie o script e escolha a opção da busca.')
    exit()

lang = input('Digite o idioma da busca (pt, en, es, fr, todos): ')
if lang == 'todos':
    c.Lang = None
else:
    c.Lang = lang

período = input('Digite a data e hora de início da busca (AAAA-MM-DD HH:MM:SS)'
                ' ou deixe em branco para ignorar esse parâmetro: ')
if período == '':
    c.Since = None
else:
    c.Since = período

períodoFinal = input('Digite a data e hora de final da busca (AAAA-MM-DD HH:MM:SS)'
                ' ou deixe em branco para ignorar esse parâmetro: ')
if períodoFinal == '':
    c.Until = None
else:
    c.Until = períodoFinal

c.Store_csv = True #define o arquivo final como csv
c.Tabs = True #define que a separação das colunas do CSV serão através de tabulação
c.Hide_output = True #esconde a raspagem em tempo real

 #imprime o resumo dos parâmetros
print('-'*70)
print('\n'
      '-Raspagem do Twitter-\n'
      f'Termo da busca: {c.Search};\n'
      f'Usuário buscado: {c.Username};\n'
      f'Data e hora da busca: {data}; \n'
      f'Idioma da busca: {c.Lang};\n'
      f'Data do início da busca: {c.Since};\n'
      f'Data do final da busca: {c.Until};\n'
      f'Nome da pasta: {nome}.')  
print('-'*70)
time.sleep(1)

runScript = input('Tudo ok? (s/n): ').strip().lower()

#criação do relatório com os dados da busca:
reportPath = os.path.join(c.Output, 'relatório')
if runScript == 's':    
    relatório = open(f'{reportPath}_{nome}.txt', 'w')
    relatório.write(
    '-Raspagem do Twitter-\n'
    f'Termo da busca: {c.Search};\n'
    f'Usuário buscado: {c.Username};\n'
    f'Data e hora da busca: {data}; \n'
    f'Idioma da busca: {c.Lang};\n'
    f'Data do início da busca: {c.Since};\n'
    f'Data do final da busca: {c.Until};\n'
    f'Nome da pasta: {nome}.')
    relatório.close
    twint.run.Search(c)
else:
    print('Reinicie o script e redefina os parâmetros corretamente.')
    exit()
    