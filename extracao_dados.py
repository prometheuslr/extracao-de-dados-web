import requests
from bs4 import BeautifulSoup


#Capturara dos links atraves da pagina inicial
url = 'https://www.ingressoprime.com'
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

divs = soup.find_all('div', class_='evento')

links = []
for div in divs:
    a_tag = div.find('a')
    if a_tag:
        link = a_tag.get('href')
        links.append(link)

urls = []

# Adicione um esquema (https://) às URLs ausentes
for link in links:
    if link.startswith('//'):
        url_corrigida = 'https:' + link
        urls.append(url_corrigida)
    else:
        urls.append(link)

quan_urls = len(urls)

dados_sites = []

#Captura dos dados em cada link
for i in range(0,quan_urls):
    if urls:
        url_dos_sites = urls[i]
        response_sites = requests.get(url_dos_sites)
        content_sites = response_sites.text

        soup_sites = BeautifulSoup(content_sites, 'html.parser')

        h2_element = soup_sites.find('header', class_='header-evento-titulo').find('h2')

        # Verifique se o elemento <h2> foi encontrado
        if h2_element:
            # Obtenha o texto do <h2>
            h2_text = h2_element.get_text()

        else:
            print("Elemento <h2> não encontrado.")

    li_element = soup_sites.find('div', class_='local-atracoes').ul.find('li')

    # Verifique se o elemento <li> foi encontrado
    if li_element:
        # Obtenha o texto dentro do <li>
        info_text = li_element.get_text(strip=True)
      
    else:
        print("Elemento <li> não encontrado.")


    data = soup_sites.find('div', class_='local-atracoes').ul.find_all('li')[1]

    # Verifique se o elemento <li> foi encontrado
    if data:
        # Obtenha o texto dentro do <li>
        n_data = data.get_text(strip=True)
    else:
        print("Elemento <li> não encontrado.")

    dados_sites.append([h2_text,info_text, n_data])

print(dados_sites)


