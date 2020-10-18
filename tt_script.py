import twint
from datetime import datetime
import time
import os 

data = datetime.now()
timestr = time.strftime("%Y%m%d")

#Definir a lista de termos para busca:
searchList = ['história digital', 'sociologia digital', 'humanidades digitais'] 

#Loop de raspagem de cada termo: 
for search in searchList:
    c = twint.Config() #configurar os parâmatros de busca do twint
    c.Search = "'"+search+"'" #aqui podemos substituir por c.Username
    name = search+'_'+timestr
    c.Output = os.path.join('DATA', name) #pasta de saída
    if not os.path.exists(c.Output): #se a pasta não existe, cria a pasta DATA
        os.makedirs(c.Output)
    c.Lang = None #definir o idioma da search
    c.Since = None #definir o período inicial da search
    c.Until = None #definir até quando a search deve ser feita
    c.Store_csv = True #define o arquivo final como CSV
    c.Tabs = True #define que a separação das colunas do CSV serão através de tabulação
    c.Hide_output = True #esconde a raspagem em tempo real

    #imprime o resumo dos parâmetros 
    print(f'-Raspagem do Twitter-\nTermo da busca: {c.Search};\nData e hora da busca: {data}; \nIdioma da busca: {c.Lang};\nData do início da busca: {c.Since};\nData do final da busca: {c.Until};\nNome da pasta: {name}.')
       
    #criação do relatório com os dados da search:
    reportPath = os.path.join(c.Output, 'report')
    report = open(f'{reportPath}_{name}.txt', 'w')
    report.write(f'-Raspagem do Twitter-\nTermo da busca: {c.Search};\nData e hora da busca: {data}; \nIdioma da busca: {c.Lang};\nData do início da busca: {c.Since};\nData do final da busca: {c.Until};\nNome da pasta: {name}.')
    report.close

    #inicia o script com o twint
    twint.run.Search(c)
    print('Passando para termo de busca seguinte...')

print('Fim da raspagem.')
