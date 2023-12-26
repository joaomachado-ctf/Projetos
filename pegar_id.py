from bs4 import BeautifulSoup
import requests

def scrape_data(url, username, password, path):
    dados_acesso = {"username": username, "password": password, "path": path}

    with requests.Session() as s:
        login = s.post(url, data=dados_acesso)

        if login.status_code == 200:
            mailing= BeautifulSoup(login.text,'html.parser')
            req_id = mailing.find_all('a', {'alt': 'Editar'})
            ids = set()

            for req_id in req_id:
                id = req_id['href'].split('=')[-1]
                ids.add(id)

            with open ('ids.txt', 'w') as salvar_id:
                for id in ids:
                    print(id,file=salvar_id)

# Chamar a função com os valores desejados
scrape_data("https://cotefacilbr.myuc2b.com/app/dialer_importer/importer.php",
             "Joao.Machado",
             "#@Alpha1046",
             "")