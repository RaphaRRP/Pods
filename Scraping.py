import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_primaria = []
response = requests.get('https://rapharrp.github.io/Pods/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'produtos'})

for produto in produtos:

    nome = produto.find('h3', attrs={'class': 'grafitepurple'}).text
    valor = produto.find('button', attrs={'class': 'btn'}).text

    print(nome, valor)

    lista_secundaria = []
    lista_secundaria.append(nome)
    lista_secundaria.append(valor)
    lista_primaria.append(lista_secundaria)


    dados = lista_primaria

    dados_com_cabecalho = [["nome", "Preço"]] + dados

    df = pd.DataFrame(dados_com_cabecalho[1:], columns=dados_com_cabecalho[0])

    arquivo_excel = "dados.xlsx"
    writer = pd.ExcelWriter(arquivo_excel, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for column_cells in worksheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        worksheet.column_dimensions[column_cells[0].column_letter].width = length + 2

    writer._save()

print("Tabela exportada para o arquivo:", arquivo_excel)