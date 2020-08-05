import twint
import time

busca01 = input('Digite o termo da primeira busca: ')
idioma = input('Defina o idioma da busca (para buscar todos os idiomas, digite todos): ').strip().lower()
if idioma == 'portugues':
    idioma = '\'' + 'pt' + '\''
elif idioma == 'inglês':
    idioima = '\'' + 'en' + '\''
elif idioma == 'espanhol':
    idioma = '\'' + 'es' + '\''
elif idioma == 'francês':
    idioma = '\'' + 'fr' + '\''
elif idioma == 'todos':
    idioma = None
else:
    idioma = None

nomeDoArquivo = busca01.replace('\'', '')
c = twint.Config()

c.Search = '\'' + busca01 + '\''
c.Lang = idioma
c.Store_csv = True
c.Output = nomeDoArquivo
print('Termo da busca: {};\n'
      'Idioma da busca: {};\n'
      'Nome da pasta: {}.'.format(c.Search, c.Lang, c.Output))
time.sleep(5)
runScript = input('Tudo ok? (s/n): ').strip().lower()
if runScript == 's':
    twint.run.Search(c)
else:
    print('Reinicie o script.')
    exit()
