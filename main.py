import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import funcoes
#import dados_live

# links dos dados que deseja analisar(Site de referência para os dados: https://www.fctables.com)
casa = input('Insira o link dos dados sobre o time da CASA do site www.fctables.com: ')
visitante = input('Insira o link dos dados sobre o time da VISITANTE do site www.fctables.com: ')

link_time_casa = f'{casa}'
link_time_visitante = f'{visitante}'

headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"}

############################  Casa ####################################

# passando o que queremos do site:

site = requests.get(link_time_casa, headers=headers)

# recebedno o objeto do soup
# parser - informa o tipo de dados que irá receber

soup = BeautifulSoup(site.content, 'html.parser')

##### DADOS Gerais #####

# puxando todos os dados da página

filtro_time = soup.find_all('span', itemprop="name")
nome_time_casa = filtro_time[0].get_text()


#### Outros Dados Gerais ####

outros_dados_totais = soup.find_all('div', "text-success")
# print(outros_dados_totais)


#### Todos os jogos ####

jogos_totais = soup.find_all('div', "text-primary")[1].get_text()

# outrosdados

# <div class="text-success ">100</div>
gols_totais = soup.find_all('div', "text-success")[7].get_text()
media_totais = soup.find_all('div', "text-success")[8].get_text()
win_totais = soup.find_all('div', "text-success")[9].get_text()
empates_totais = soup.find_all('div', "text-warning")[1].get_text()
loser_totais = soup.find_all('div', "text-danger")[1].get_text()
over15_totais = soup.find_all('div', "text-success")[11].get_text()
over25_totais = soup.find_all('div', "text-success")[10].get_text()

#funções

odds_wins_geral = funcoes.oddWinCasaTotal(jogos_totais,win_totais)
ev_positivo_punter = funcoes.evPositivoPunter(jogos_totais,win_totais,'1.00', odds_wins_geral) #imputar o valor mais na frente

#### ultimos 6 jogos #####

gols_ultimos6jogos = outros_dados_totais[0].get_text()
media_ultimos6jogos = outros_dados_totais[1].get_text()
win_ultimos6jogos = outros_dados_totais[2].get_text()
empates_ultimos6jogos = soup.find_all('div', "text-warning")[0].get_text()
loser_ultimos6jogos = soup.find_all('div', "text-danger")[0].get_text()
over15_ultimos6jogos = outros_dados_totais[4].get_text()
over25_ultimos6jogos = outros_dados_totais[3].get_text()



# dados do momento e validades:

# < label class ="label label-primary" > 46.21 % < / label >
# <label class="label label-primary">12.04</label>
# < label class ="label label-primary" > 12.04 < / label >
# div class=col-sm-6
# "div", "team_stats_box"
estatisticas = soup.find_all("td", "text-center")

# print(estatisticas)


########################################  Visitante ########################################

# passando o que queremos do site:

site_visitante = requests.get(link_time_visitante, headers=headers)

# recebedno o objeto do soup
# parser - informa o tipo de dados que irá receber

soup = BeautifulSoup(site_visitante.content, 'html.parser')

##### DADOS Gerais #####

# puxando todos os dados da página

#<td align="center">12</td>
#<td align="center" bgcolor="#c6ecc6"><b>10</b></td>
#<td class="text-center">80.95%</td>
#'table', "table")

#dados_all = soup.find_all('div', "text-primary")
#print(dados_all)


# TIME
# <strong>Manchester City (England - Premier League) statistics</strong>
# <span itemprop="name">Manchester City</span>
filtro_time_visitante = soup.find_all('span', itemprop="name")
nome_time_visitante = filtro_time_visitante[0].get_text()
#print('\n')
#print(f"Informações e estatísticas do {nome_time_visitante}")
#print("_" * 50)
#print('\n\n')

#### Outros Dados Gerais ####

outros_dados_totais_visitante = soup.find_all('div', "text-success")
# print(outros_dados_totais)


#### Todos os jogos ####

jogos_totais_visitante = soup.find_all('div', "text-primary")[1].get_text()

# outrosdados

# <div class="text-success ">100</div>
gols_totais_visitante = soup.find_all('div', "text-success")[7].get_text()
media_totais_visitante = soup.find_all('div', "text-success")[8].get_text()
win_totais_visitante = soup.find_all('div', "text-success")[9].get_text()
empates_totais_visitante = soup.find_all('div', "text-warning")[1].get_text()
loser_totais_visitante = soup.find_all('div', "text-danger")[1].get_text()
over15_totais_visitante = soup.find_all('div', "text-success")[11].get_text()
over25_totais_visitante = soup.find_all('div', "text-success")[10].get_text()


#funções

odds_wins_geral_visitante = funcoes.oddWinCasaTotal(jogos_totais_visitante,win_totais_visitante)
ev_positivo_punter_visitante = funcoes.evPositivoPunter(jogos_totais_visitante,win_totais_visitante,'1.00', odds_wins_geral_visitante) #imputar o valor mais na frente


#### ultimos 6 jogos #####

gols_ultimos6jogos_visitante = outros_dados_totais_visitante[0].get_text()
media_ultimos6jogos_visitante = outros_dados_totais_visitante[1].get_text()
win_ultimos6jogos_visitante = outros_dados_totais_visitante[2].get_text()
empates_ultimos6jogos_visitante = soup.find_all('div', "text-warning")[0].get_text()
loser_ultimos6jogos_visitante = soup.find_all('div', "text-danger")[0].get_text()
over15_ultimos6jogos_visitante = outros_dados_totais_visitante[4].get_text()
over25_ultimos6jogos_visitante = outros_dados_totais_visitante[3].get_text()

########################################################################################################################
print('\n')
print(f"Premissas {nome_time_casa} x {nome_time_visitante}")
print('\n')

previsao = funcoes.tendenciaOverGeral(media_totais, media_totais_visitante, over15_totais, over15_totais_visitante) + funcoes.tendenciaOverUltimosJogos(media_ultimos6jogos,media_ultimos6jogos_visitante, funcoes.over15Total_6ultimos(over15_ultimos6jogos)[0], funcoes.over15Total_6ultimos(over15_ultimos6jogos_visitante)[1])
if previsao == 8:
    indicador = "Probabilidade ALTA de gols na partida"

elif previsao < 8 and previsao >= 6:
    indicador = "Probabilidade MODERADA de gols na partida"

else:
    indicador = "Probabilidade POUCOS de gols na partida"

tabelaIndicador = [['Indicadores', 'Provisões'],
                   ['Indicadores de Gols', indicador]]

print(tabulate(tabelaIndicador,  headers='firstrow', tablefmt="simple"))



print('\n')
print(f"Informações e estatísticas do {nome_time_casa} x {nome_time_visitante}")
print("_" * 60)
print('\n')

tabela = [['Mercado',nome_time_casa, 'Odds Mínimas','+EV','X',nome_time_visitante, 'Odds Mínimas','+EV'],
         ['Jogos Totais', jogos_totais,'','','',jogos_totais_visitante,''],
         ['Gols Totais', gols_totais,'','','',gols_totais_visitante,''],
          ['Gols por Partidas', media_totais,'','',funcoes.previssoesGols(media_totais,media_totais_visitante), media_totais_visitante,''],
          ['VITÓRIAS', win_totais, funcoes.oddWinCasaTotal(jogos_totais,win_totais),ev_positivo_punter,funcoes.medias(funcoes.oddWinCasaTotal(jogos_totais,win_totais),funcoes.oddWinCasaTotal(jogos_totais_visitante,win_totais_visitante)),win_totais_visitante,funcoes.oddWinCasaTotal(jogos_totais_visitante,win_totais_visitante),ev_positivo_punter_visitante],
          ['Empates', empates_totais,'','','', empates_totais_visitante,''],
          ['Derrotas', loser_totais,'','','',loser_totais_visitante,''],
          ['Over 1,5', over15_totais, funcoes.over15Total(over15_totais),'',funcoes.medias(funcoes.over15Total(over15_totais),funcoes.over15Total(over15_totais_visitante)),over15_totais_visitante,funcoes.over15Total(over15_totais_visitante),''],
           ['Over 2,5', over25_totais, funcoes.over25Total(over25_totais),'',funcoes.medias(funcoes.over25Total(over25_totais),funcoes.over25Total(over25_totais_visitante)),over25_totais_visitante ,funcoes.over25Total(over25_totais_visitante),'']]

print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

tabela_6jogos =[['Mercado no útimos 6 jogos',nome_time_casa,'Odds Mínimas','X',nome_time_visitante,'Odds Mínimas'],
                #['Jogos Totais', jogos_totais,'',jogos_totais_visitante],
                ['Gols ', gols_ultimos6jogos,'','',gols_ultimos6jogos_visitante],
                ['Gols por Partidas', media_ultimos6jogos,'',funcoes.previssoesGols(media_ultimos6jogos, media_ultimos6jogos_visitante),media_ultimos6jogos_visitante],
                ['VITÓRIAS', win_ultimos6jogos, funcoes.oddWinCasaTotal('6',win_ultimos6jogos),funcoes.medias(funcoes.oddWinCasaTotal('6',win_ultimos6jogos),funcoes.oddWinCasaTotal('6',win_ultimos6jogos_visitante)),win_ultimos6jogos_visitante,funcoes.oddWinCasaTotal('6',win_ultimos6jogos_visitante)],
                ['Empates', empates_ultimos6jogos,'','', empates_ultimos6jogos_visitante],
                ['Derrotas', loser_ultimos6jogos,'','', loser_ultimos6jogos_visitante],
                ['Over 1,5', funcoes.over15Total_6ultimos(over15_ultimos6jogos)[0], funcoes.over15Total_6ultimos(over15_ultimos6jogos)[1],funcoes.medias(funcoes.over15Total_6ultimos(over15_ultimos6jogos)[1],funcoes.over15Total_6ultimos(over15_ultimos6jogos_visitante)[1]),funcoes.over15Total_6ultimos(over15_ultimos6jogos_visitante)[0],funcoes.over15Total_6ultimos(over15_ultimos6jogos_visitante)[1]],
                ['Over 2,5', funcoes.over25Total_6ultimos(over25_ultimos6jogos)[0], funcoes.over25Total_6ultimos(over25_ultimos6jogos)[1],funcoes.medias(funcoes.over25Total_6ultimos(over25_ultimos6jogos)[1],funcoes.over25Total_6ultimos(over25_ultimos6jogos_visitante)[1]),funcoes.over25Total_6ultimos(over25_ultimos6jogos_visitante)[0],funcoes.over25Total_6ultimos(over25_ultimos6jogos_visitante)[1]]]

print(tabulate(tabela_6jogos, headers='firstrow', tablefmt='fancy_grid'))

#tabela_live = [['Tempo de jogo']
#                 ['contagem do tempo']],


#print(tabulate(tabela_live, headers='firstrow', tablefmt='fancy_grid'))
