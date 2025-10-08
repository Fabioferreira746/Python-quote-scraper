# Python-quote-scraper

# 🕷️ Web Scraper de Frases - Projeto Python

Este projeto é um scraper simples desenvolvido em Python que coleta **frases inspiradoras**, seus **autores** e as **tags associadas** do site [Quotes to Scrape](https://quotes.toscrape.com/), e exporta os dados para um arquivo CSV.

# 📌 Objetivo

- Aprender a fazer requisições HTTP com `requests`
- Praticar raspagem de dados com `BeautifulSoup`
- Organizar e exportar dados estruturados em CSV


## ⚙️ Tecnologias usadas

- Python 3
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- Módulo `csv` da biblioteca padrão


#  🗂️ O que o scraper faz?

1. Acessa automaticamente as 10 primeiras páginas do site.
2. Para cada citação, extrai:
   - A **frase**
   - O **autor**
   - As **tags** associadas
3. Salva os dados no arquivo `frases_scrapeadas.csv`

