import requests
from bs4 import BeautifulSoup
import openpyxl


def webScrap():
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
    dados_ingressos = []
    id_show = 0
    #Captura dos dados em cada link
    for i in range(0,quan_urls):
        id_show= id_show+1
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

        # h2_text = "Título", info_text = "Informação", n_data = "Data"
        dados_sites.append([id_show,h2_text,info_text, n_data])
        
        #Ingressos
        lote = None
        tipo_ingreeso = None
        valor_ingresso = None
        disponibilidade = None

        class_ingressos = soup_sites.find_all('div',class_='opcao-ingresso')
        class_ingressos_g = soup_sites.find('div',class_='opcao-ingresso')
        quan_class_ingressos = len(class_ingressos)
        #Verifica se o ingresso é gratis

        if class_ingressos_g == None:
            ingresso = "Gratis"
            dados_ingressos.append([id_show,ingresso,lote,tipo_ingreeso,valor_ingresso,disponibilidade])
        else:
            x=[]
            for i in range(0,quan_class_ingressos):
                
                ingresso = "Pago"
                #Lote
                lote = class_ingressos[i].find('span', class_="info-lft").get_text()
                #Tipo de ingresso
                tipo_ingreeso = class_ingressos[i].find('span', class_="caps").get_text()
                #Valor
                valor_ingresso = class_ingressos[i].find('div', class_="valor-ingresso-unid left-comp").get_text().strip()[2:].strip()
                #Disponibilidade
                disponibilidade = class_ingressos[i].find('span', class_="badge")

                if disponibilidade == None:
                    disponibilidade = "Disponivel"
                else:
                    disponibilidade = disponibilidade.get_text()

                dados_ingressos.append([id_show,ingresso,lote, tipo_ingreeso,valor_ingresso, disponibilidade])
                
            
        

        
    wb = openpyxl.Workbook()
    ws = wb.active  # Obtenha a planilha ativa

    # Cabeçalhos das colunas
    ws.append(["Id","Titulo", "Informacao", "Data"])

    # Adicione os dados coletados às linhas
    for dados in dados_sites:
        ws.append(dados)

    # Salve o arquivo Excel com um nome específico
    excel_filename = 'dados_site_shows.xlsx'
    wb.save(excel_filename)

    #print(f'Dados salvos em {excel_filename}')
        

    #print(dados_sites)

    #print(dados_ingressos)


    wi = openpyxl.Workbook()
    wa = wi.active 
    # Cabeçalhos das colunas
    wa.append(["Id", "Ingresso", "Lote", "Tipo_do_ingresso", "Valor_do_ingresso", "Disponibilidade"])

    # Adicione os dados coletados às linhas
    for ingresso_info in dados_ingressos:
        wa.append(ingresso_info)

    # Salve o arquivo Excel com um nome específico
    excel_name = 'dodos_ingresso_show.xlsx'
    wi.save(excel_name)


