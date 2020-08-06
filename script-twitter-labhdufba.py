import twint
from datetime import datetime
import time
import os 

data = datetime.now()
timestr = time.strftime("%Y%m%d")

#Definir a lista de termos para busca:
lista = ['sociologia digital', '#sociologiadigital'] 

#Loop de raspagem de cada termo: 
for busca in lista:
    c = twint.Config() #configurar os parâmatros de busca do twint
    c.Search = "'"+busca+"'" #aqui podemos substituir por c.Username
    nome = busca+'_'+timestr
    c.Output = os.path.join('DATA', nome) #pasta de saída
    if not os.path.exists(c.Output): #se a pasta não existe, cria a pasta DATA
        os.makedirs(c.Output)
    c.Lang = None #definir o idioma da busca
    c.Since = None #definir o período inicial da busca
    c.Until = None #definir até quando a busca deve ser feita
    c.Store_csv = True #define o arquivo final como csv
    c.Hide_output = True #esconde a raspagem em tempo real

    #imprime o resumo dos parâmetros 
    print('\n'
          '-Raspagem do Twitter-\n'
          'Termo da busca: {};\n'          
          'Data e hora da busca: {}; \n'
          'Idioma da busca: {};\n'
          'Data do início da busca: {};\n'
          'Data do final da busca: {};\n'
          'Nome da pasta: {}.'.format(c.Search, data, c.Lang, c.Since, c.Until, nome)
          )
       
    #criação do relatório com os dados da busca:
    relatórioPath = os.path.join(c.Output, 'relatório')
    relatório = open('{}_{}.txt'.format(relatórioPath, nome), 'w')
    relatório.write('-Raspagem do Twitter-\n'
    'Termo da busca: {};\n'    
    'Data e hora da busca: {}; \n'
    'Idioma da busca: {};\n'
    'Data do início da busca: {};\n'
    'Data do final da busca: {};\n'
    'Data do final da busca: {};\n'
    'Nome da pasta: {}.'.format(c.Search, data, c.Lang, c.Since, c.Until, c.Until, nome)    
    )
    relatório.close

    #inicia o script com o twint
    twint.run.Search(c)
    print('Passando para termo de busca seguinte...')

print('Fim da raspagem.')
