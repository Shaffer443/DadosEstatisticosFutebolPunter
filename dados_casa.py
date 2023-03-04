import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import math
import funcoes

# link dos dados que deseja analisar.
link_time_casa = 'https://www.fctables.com/teams/fiorentina-185391/'

headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"}

# passando o que queremos do site:

site = requests.get(link_time_casa, headers=headers)

# recebedno o objeto do soup
# parser - informa o tipo de dados que irá receber

soup = BeautifulSoup(site.content, 'html.parser')

##### DADOS Gerais #####

# puxando todos os dados da página

#<td align="center">12</td>
#<td align="center" bgcolor="#c6ecc6"><b>10</b></td>
#<td class="text-center">80.95%</td>
#'table', "table")

#dados_all = soup.find_all('div', "text-primary")
#print(dados_all)

def timeCasa():

    # TIME
    #<strong>Manchester City (England - Premier League) statistics</strong>
    #<span itemprop="name">Manchester City</span>
    filtro_time = soup.find_all('span',itemprop="name")
    nome_time = filtro_time[0].get_text()
    print('\n')
    print(f"Informações e estatísticas do {nome_time}")
    print("_"*50)
    print('\n\n')

    #### Outros Dados Gerais ####

    outros_dados_totais = soup.find_all('div', "text-success")
    #print(outros_dados_totais)



    #### Todos os jogos ####

    jogos_totais = soup.find_all('div', "text-primary")[1].get_text()

    # outrosdados

    #<div class="text-success ">100</div>
    gols_totais = soup.find_all('div', "text-success")[7].get_text()
    media_totais = soup.find_all('div', "text-success")[8].get_text()
    win_totais = soup.find_all('div', "text-success")[9].get_text()
    empates_totais = soup.find_all('div', "text-warning")[1].get_text()
    loser_totais = soup.find_all('div', "text-danger")[1].get_text()
    over15_totais = soup.find_all('div', "text-success")[11].get_text()
    over25_totais = soup.find_all('div', "text-success")[10].get_text()



    print(f"- Jogos totais do {nome_time} na temporada: {jogos_totais}")
    print(f"- GOLS TOTAIS do {nome_time} na temporada: {gols_totais}")
    print(f"- MÉDIA geral de GOLS do {nome_time} na temporada: {media_totais}")
    print(f"- VITÓRIAS TOTAIS do {nome_time} na temporada: {win_totais}")
    print(f"{funcoes.oddWinCasaTotal(jogos_totais,win_totais)}")
    print(f"- EMPATES TOTAIS do {nome_time} na temporada: {empates_totais}")
    print(f"- DERROTAS TOTAIS do {nome_time} na temporada: {loser_totais}")
    print(f"- Probabilidades de OVER 1,5 FT TOTAIS do {nome_time} na temporada: {over15_totais}")
    print(f"{funcoes.over15CasaTotal(over15_totais)}")
    print(f"- Probabilidades de OVER 2,5 FT TOTAIS do {nome_time} na temporada: {over25_totais}")
    print(f"{funcoes.over15CasaTotal(over25_totais)}")

    ### teste de tabulação ###

    tabela = [[nome_time],
              ['Jogos Totais', jogos_totais],
              ['Gols Totais', gols_totais]]
    print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

    #### ultimos 6 jogos #####

    gols_ultimos6jogos = outros_dados_totais[0].get_text()
    media_ultimos6jogos = outros_dados_totais[1].get_text()
    win_ultimos6jogos = outros_dados_totais[2].get_text()
    empates_ultimos6jogos = soup.find_all('div', "text-warning")[0].get_text()
    loser_ultimos6jogos = soup.find_all('div', "text-danger")[0].get_text()


    #print("-"*100)
    print('\n')

    print(f"Dados dos últimos 6 jogos do {nome_time} :\n")

    print(f"TOTAL de Gols marcados do {nome_time}  nos ultimos 6 jogos: {gols_ultimos6jogos}")
    print(f"MÉDIA de Gols marcados do {nome_time}  nos ultimos 6 jogos: {media_ultimos6jogos}")
    print(f"ViTÓRIAS do {nome_time}  nos ultimos 6 jogos: {win_ultimos6jogos}")
    print(f"EMPATES do {nome_time}  nos ultimos 6 jogos: {empates_ultimos6jogos}")
    print(f"DERROTAS do {nome_time}  nos ultimos 6 jogos: {loser_ultimos6jogos}")

    # dados do momento e validades:

    #< label class ="label label-primary" > 46.21 % < / label >
    #<label class="label label-primary">12.04</label>
    #< label class ="label label-primary" > 12.04 < / label >
    # div class=col-sm-6
    #"div", "team_stats_box"
    estatisticas = soup.find_all("td", "text-center")

    #print(estatisticas)



timeCasa()