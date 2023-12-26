import requests

from bs4 import BeautifulSoup
import os

#apagando arquivo antigo, pois para salvar todos os nomes é necessário arbir o arquivo no modo append
if os.path.isfile('teste.txt'):
    os.remove('teste.txt')
else:
    ...

#dados necessários para logar
link= 'https://cotefacilbr.myuc2b.com/app/dialer/dialer_edit.php?id='
dados_acesso = {"username": "Joao.Machado", "password": "#@Alpha1046", "path": ""}

#Rquisitando sessão
with requests.Session() as s:
    login = s.post(url=link, data=dados_acesso) 
    if login.status_code == 200:
        print('Login efetuado com suceso')
        with open('ids.txt','r') as file_id:
          for linhas in file_id:
            id=(linhas).replace('\n','')
            pegar_nomes = BeautifulSoup(login.text,'html.parser')
            lista= pegar_nomes.find_all('option', {'value':id})
            for nomes in lista:
               with open('NomeId.txt','a') as aquivo:
                resultados = nomes.text,nomes['value']
                salvar = resultados[0]+','+resultados[1]
                print
                print(salvar,file=aquivo)
           
    else:
     print('Falha ao tentar logar, verifique os dados de acesso')

