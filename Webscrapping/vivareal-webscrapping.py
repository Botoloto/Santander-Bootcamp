import os
import cloudscraper    
from bs4 import BeautifulSoup
import pandas as pd
import time

scraper = cloudscraper.create_scraper()
rua, bairro, estado, tipo, quartos, bannheiros, vagas, preço, metragem, condominio = [], [], [], [], [], [], [], [], [], []
paginas = 200

os.system('cls')
check = True
count = 0
while count <= 10:
    for index in range(1,paginas):
        url = f'https://www.vivareal.com.br/venda/sp/ribeirao-preto/apartamento_residencial/?pagina={index}#onde=Brasil,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,,,'
        req = scraper.get(url)
        time.sleep(3)
        print(f'Página) {index}')
        if req.status_code == 200:
            pagina = req.text
            soup = BeautifulSoup(pagina, 'html.parser')
        else:
            print('Erro ao acessar a página')
            count += 1
        
        elementos = soup.find_all()
        for line in soup.findAll(class_ = 'js-card-selector'):
        
            adress = line.find('span', attrs={'class': 'property-card__address'}).text.replace(', Ribeirão Preto','').strip().split('-')
            if adress[0][:3] == 'Rua' or adress[0][:3] == 'Ave':  
                rua.append(adress[0].strip())
                bairro.append(adress[1].strip())
                estado.append(adress[2].strip())
            else:
                rua.append('N/A')
                bairro.append(adress[0].strip())
                estado.append(adress[1].strip())

            description = line.find('span', attrs={'class': 'property-card__title js-cardLink js-card-title'}).text.strip().split(' ')[0]
            tipo.append(description)
        
            area = line.find('span', attrs={'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'}).text.strip() + 'm²'
            metragem.append(area)
        
            room = line.find(class_='property-card__detail-item property-card__detail-room js-property-detail-rooms').text.strip().split(' ')[0]
            quartos.append(room)
        
            bath = line.find(class_='property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom').text.strip().split(' ')[0]
            bannheiros.append(bath)
        
            garage = line.find(class_='property-card__detail-item property-card__detail-garage js-property-detail-garages').text.strip().split(' ')[0]
            vagas.append(garage)

            try:
                cond = line.find(class_='property-card__price-details--condo js-condo-price').text.replace('R$','').strip().split(' ')[0]
                condominio.append(cond)
            except:
                condominio.append('0')
        
            price = line.find(class_='property-card__price js-property-card-prices js-property-card__price-small').text.replace('R$', '').replace(',','').strip()
            preço.append(price)

df = pd.DataFrame({'Rua': rua, 'Bairro': bairro, 'Estado': estado,'Tipo': tipo, 'Preço': preço, 'Metragem': metragem, 'Quartos': quartos, 'Banheiros': bannheiros, 'Vagas': vagas,  'Condomínio': condominio})
df = df[df['Tipo'].isin(['Apartamento', 'Casa', 'Terreno'])]
df.to_excel('vivareal.xlsx', index=False)
