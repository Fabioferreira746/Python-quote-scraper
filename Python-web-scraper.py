import requests
from bs4 import BeautifulSoup
import csv


dados = []


url_base = 'https://quotes.toscrape.com/page/{}/'

for pagina in range(1, 11):
    print(f"Raspando página {pagina}...")
    url = url_base.format(pagina)
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Página {pagina} não encontrada.")
        break

    soup = BeautifulSoup(resposta.text, 'html.parser')
    frases_div = soup.find_all('div', class_='quote')

    for div in frases_div:
        frase = div.find('span', class_='text').get_text(strip=True)
        autor = div.find('small', class_='author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in div.find_all('a', class_='tag')]
        dados.append([frase, autor, ', '.join(tags)])

with open('frases_scrapeadas.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Frase', 'Autor', 'Tags'])
    escritor.writerows(dados)

print("Scraping concluído e CSV salvo como 'frases_scrapeadas.csv'.")
