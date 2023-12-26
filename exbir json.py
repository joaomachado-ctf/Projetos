import requests
import json
import os

if os.path.isfile('res.json'):
    os.remove('res.json')
else:
    ...

url = "https://cotefacilbr.myuc2b.com/app/dialer_dashboard/dialer_view.php"
dados_acesso = {"username": "Joao.Machado", "password": "#@Alpha1046", "path": ""}
link='https://cotefacilbr.myuc2b.com/app/dialer_dashboard/dialer_state.php?mailing_uuid='
# Tentando logar para inicar sessão e poder acessar os recursos que dependem de login
with requests.Session() as s:
    # Here's where we actually make the POST request to the login form
    login = s.post(url, data=dados_acesso)

    # Verificar se o login foi bem sucedido
    if login.status_code == 200:
        print("Sessão estabelecida com sucesso!")
        with open('NomeId.txt','r') as arquivo_id:
            with open('ids.txt','w') as arquivo_json:
             with open('situacao.txt','w') as arquivo_sit:
              print(f'Agente, Ligações a fazer, ligações agendadas, Contas finalizadas, Em andamento')
              for linhas in arquivo_id:
               id = linhas.split(',')[1].replace('\n','')
               nome = linhas.split(',')[0].replace('\n','')
               sol_json = s.get(link+id)
               res_json = sol_json.json()
               print(f'{nome},{res_json["virgin"]},{res_json["scheduled"]}, {res_json["ended"]}, {res_json["mini_dialer_use"]}',file=arquivo_sit)
               print(f'{nome}: {res_json["virgin"]}')
    else:
     print(f"Falha ao tentar iniciar sessão, verifique se as informações estão corretas!")