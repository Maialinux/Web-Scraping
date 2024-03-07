import requests # Módulo para requisições
from bs4 import BeautifulSoup # Módulo possui ferramentas para coletar informação de algum site  
import re # Módulo para trabalhar com regex
import pandas as pd # Módulo para trabalhar com tabelas
import math # Módulo para trabalhar com funções matemáticas

# XlsxWriter - Módulo para salvar arquivo em .xlsx
# cx_Freeze - Módulo que possui recurso para mostrar as dependências utilizadas no programa

class Main():
    # Cosntrutor da classe Main
    def __init__(self) -> None:
        self.Pesquisar() # Função declarada dentro do construtor
        pass
    
    # Função Pesquisar
    def Pesquisar(self):
        self.Produto1_hardstore()
        self.Produto2_hardstore()
        self.Produto3_hardstore()
        pass
    

    # Função que busca no site dados para produto 1
    
    def Produto1_hardstore(self):
                
        url='https://www.hardstore.com.br/shop/hd'
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content,'html.parser')


        # Pega informação do número total de produtos da seção memória
        qtd_itens = soup.find('div', class_='view-options__legend').get_text().strip()[17:19].strip()

        #print(qtd_itens)

        ultima_pagina = math.ceil(int(qtd_itens) / 24)
        #print(ultima_pagina)

        dic_produtosSAS = {'marca':[], 'preco':[]}
        dic_produtosSATA = {'marca':[], 'preco':[]}
        dic_produtosHdExterno = {'marca':[], 'preco':[]}

        for i in range(1, ultima_pagina+1):
            url1='https://www.hardstore.com.br/shop/hd?filter_last=md_63&filter_md_63=SAS%2012Gb/s'
            url2='https://www.hardstore.com.br/shop/hd?filter_last=md_63&filter_md_63=SATA%20II%203.0Gb/s|SATA%20III%206.0Gb/s'
            url3='https://www.hardstore.com.br/shop/hd?filter_last=md_63&filter_md_63=USB%202.0|USB%203.0|USB%203.2'
            site1 = requests.get(url1, headers=headers)
            site2 = requests.get(url2, headers=headers)
            site3 = requests.get(url3, headers=headers)
            soup1 = BeautifulSoup(site1.content,'html.parser')
            soup2 = BeautifulSoup(site2.content,'html.parser')
            soup3 = BeautifulSoup(site3.content,'html.parser')
            produtos1 = soup1.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
            produtos2 = soup2.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
            produtos3 = soup3.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
            
            
            for produto in produtos1:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                dic_produtosSAS['marca'].append(marca)
                dic_produtosSAS['preco'].append(preco)
            
            for produto in produtos2:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                dic_produtosSATA['marca'].append(marca)
                dic_produtosSATA['preco'].append(preco)
                
            for produto in produtos3:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                dic_produtosHdExterno['marca'].append(marca)
                dic_produtosHdExterno['preco'].append(preco)
            
                
        df1 = pd.DataFrame(dic_produtosSAS) 
        df2 = pd.DataFrame(dic_produtosSATA) 
        df3 = pd.DataFrame(dic_produtosHdExterno)

        writer = pd.ExcelWriter('./planilhas/precos_dos_hds_1.xlsx', engine='xlsxwriter')
        df1.to_excel(writer, sheet_name='HD SAS')
        df2.to_excel(writer, sheet_name='HD SATA')
        df3.to_excel(writer, sheet_name='HD USB')
        writer.close()
        
                
        """SSD SATA"""
        url1="https://www.hardstore.com.br/shop/ssd?filter_last=md_63&filter_md_63=SATA%20III%206.0Gb/s"
        headers1 = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site1 = requests.get(url1, headers=headers1)
        soup1 = BeautifulSoup(site1.content,'html.parser')

        """SSD NVMe"""
        url2="https://www.hardstore.com.br/shop/ssd?filter_last=md_63&filter_md_63=NVMe%20PCIe%20Gen%203.0%20x4|NVMe%20PCIe%20Gen%204.0%20x4"
        headers2 = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site2 = requests.get(url2, headers=headers2)
        soup2 = BeautifulSoup(site2.content,'html.parser')

        """SSD USB EXTERNO"""
        url3="https://www.hardstore.com.br/shop/ssd?filter_last=md_63&filter_md_63=1%20x%20USB%203.2%20Tipo%20C"
        headers3 = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site3 = requests.get(url3, headers=headers2)
        soup3 = BeautifulSoup(site3.content,'html.parser')

        dic_produtosSATA = {'marca':[], 'preco':[]}
        dic_produtosNVMe = {'marca':[], 'preco':[]}
        dic_produtosUsbExterno = {'marca':[], 'preco':[]}

        listaSSDSata = soup1.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
        listaSSDNVMe = soup2.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
        listaSSDUsbExterno = soup3.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))

        for produto in listaSSDSata:
            marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
            preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
            print(marca, preco)
                
            dic_produtosSATA['marca'].append(marca)
            dic_produtosSATA['preco'].append(preco)


        for produto in listaSSDNVMe:
            marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
            preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
            print(marca, preco)
                
            dic_produtosNVMe['marca'].append(marca)
            dic_produtosNVMe['preco'].append(preco)


        for produto in listaSSDUsbExterno:
            marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
            preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
            print(marca, preco)
                
            dic_produtosUsbExterno['marca'].append(marca)
            dic_produtosUsbExterno['preco'].append(preco)


        df1 = pd.DataFrame(dic_produtosSATA)     
        df2 = pd.DataFrame(dic_produtosNVMe)  
        df3 = pd.DataFrame(dic_produtosUsbExterno)  
        writer = pd.ExcelWriter('./planilhas/preco_dos_ssds_1.xlsx', engine='xlsxwriter')   
        df1.to_excel(writer, sheet_name='SSD SATA')
        df2.to_excel(writer, sheet_name='SSD NVMe')
        df3.to_excel(writer, sheet_name='SSD Externo')
        writer.close()
        pass

    
    # Função que busca no site dados para produto 2
    
    def Produto2_hardstore(self):
        url="https://www.hardstore.com.br/shop/memoria?filter_brand=31&filter_last=brand"
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content,'html.parser')

        # Pega informação do número total de produtos da seção memória
        qtd_itens = soup.find('div', class_='view-options__legend').get_text().strip()[17:21].strip()

        ultima_pagina = math.ceil(int(qtd_itens) / 50)

        dic_produtos = {'marca':[], 'preco':[]}
        dic_produtos2 = {'marca':[], 'preco':[]}

        # Pega informação de forma dinâmica da página.
        # URL Filtrando memória DDR3 -> https://www.hardstore.com.br/shop/memoria?filter_brand=31&filter_last=md_270&filter_md_270=DDR3

        for i in range(1, ultima_pagina+1):
            pagina_url = f'https://www.hardstore.com.br/shop/memoria?page={i}&filter_brand=31&filter_last=md_270&filter_md_270=DDR3'
            pagina_url2 = f'https://www.hardstore.com.br/shop/memoria?page={i}&filter_brand=31&filter_last=md_270&filter_md_270=DDR4'
            site = requests.get(pagina_url, headers=headers)
            site2 = requests.get(pagina_url2, headers=headers)
            soup = BeautifulSoup(site.content,'html.parser')
            soup2 = BeautifulSoup(site2.content,'html.parser')
            produtos = soup.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
            produtos2 = soup2.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
                
            for produto in produtos:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                
                dic_produtos['marca'].append(marca)
                dic_produtos['preco'].append(preco)
                
            for produto in produtos2:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                
                dic_produtos2['marca'].append(marca)
                dic_produtos2['preco'].append(preco)

        df1 = pd.DataFrame(dic_produtos)     
        df2 = pd.DataFrame(dic_produtos2)
        writer = pd.ExcelWriter('./planilhas/preco_das_memorias_1.xlsx', engine='xlsxwriter')
        
        df1.to_excel(writer, sheet_name='DDR 3')
        df2.to_excel(writer, sheet_name='DDR 4')

        writer.close()
        pass

    
    # Função que busca no site dados para produto 3
    
    def Produto3_hardstore(self):
        url="https://www.hardstore.com.br/shop/placa-video"
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content,'html.parser')

        # Pega informação do número total de produtos da seção memória
        qtd_itens = soup.find('div', class_='view-options__legend').get_text().strip()[17:21].strip()

        ultima_pagina = math.ceil(int(qtd_itens) / 60)

        dic_produtos = {'marca':[], 'preco':[]}
        
        for i in range(1, ultima_pagina+1):
            pagina_url = f'https://www.hardstore.com.br/shop/placa-video?page={i}&sort=price_asc'
            site = requests.get(pagina_url, headers=headers)
            soup = BeautifulSoup(site.content,'html.parser')
            produtos = soup.find_all('div', class_ =re.compile('product-card product-card--hidden-actions'))
                
            for produto in produtos:
                marca = produto.find('div',class_=re.compile('product-card__name')).get_text().strip()
                preco = produto.find('div',class_=re.compile('product-card__prices')).get_text().strip()
                print(marca, preco)
                
                dic_produtos['marca'].append(marca)
                dic_produtos['preco'].append(preco)
                
        df1 = pd.DataFrame(dic_produtos)     
        writer = pd.ExcelWriter('./planilhas/preco_das_placas_de_videos_1.xlsx', engine='xlsxwriter')
        
        df1.to_excel(writer, sheet_name='videos')

        writer.close()
        pass
    
    
    
if __name__ == "__main__":
    Main()
