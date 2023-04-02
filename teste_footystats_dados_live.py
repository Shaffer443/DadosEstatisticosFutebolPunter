import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time
from datetime import datetime
import funcoes

# link dos dados que deseja analisar.
insert_link = input('Insira o link dos dados da live site www.footystats.org: ')
link_live = f"{insert_link}"

#headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"}

        # passando o que queremos do site:

#site = requests.get(link_live, headers=headers)

        # recebedno o objeto do soup
        # parser - informa o tipo de dados que irá receber

#soup = BeautifulSoup(site.content, 'html.parser')

#qtd_itens = soup.find_all("td", scope="row")

#print(len(qtd_itens))

while True:



    headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"}

        # passando o que queremos do site:

    site = requests.get(link_live, headers=headers)

        # recebedno o objeto do soup
        # parser - informa o tipo de dados que irá receber

    soup = BeautifulSoup(site.content, 'html.parser')

        # variável de dados - Pesquisa #

        #<div class="cf row"><div class="w50 rw100 fl" style="font-size:9.5pt;"><p class="ac fs2e bold">1 <span class="normal dark-gray">-</span> 0</p><p class="ac semi-bold mt05">35<span class="blinker-slow">'</span></p><div class="w100 pt1e cf"><div class="w100 cf"><div class="w45 bbox fl ar pr05e mb05e" style=""><a class="mild-small semi-bold" href="/players/brazil/gabriel-teodoro-martinelli-silva">Gabriel Teodoro Martinelli Silva</a><a href="/players/england/bukayo-saka" class="dark-gray dBlock w100 small pr rmt05e" style="top:-4px;"><i style="opacity:0.5;position:relative;top:0px;font-size:8px !important;" class="fs09e fas fa-share"></i> Bukayo Saka</a></div><div class="w10 fl"><p class="dark-gray mild-small dIBlock semi-bold ac w100"><i class="far fa-futbol pr o9" style="font-size:0.7em !important;"></i><br><span class="rt1 pr mild-small" style="top:-4px;left:1px;">35'</span></p></div></div></div></div><div class="fl w50 rw100 pl1e pr1e pb1e"><table class=" comparison-table-table w100"><thead><tr class="row header"><th class="item key al" scope="col"></th><th class="item stat" scope="col">Arsenal</th><th class="item stat" scope="col">Crystal Palace</th></tr></thead><tbody><tr class="row"><td class="item key" scope="row">Shots Total</td><td class="item stat null">4</td><td class="item stat null">2</td></tr><tr class="row"><td class="item key" scope="row">Shots On Target</td><td class="item stat null">2</td><td class="item stat null">0</td></tr><tr class="row"><td class="item key" scope="row">Shots Off Target</td><td class="item stat null">2</td><td class="item stat null">2</td></tr><tr class="row"><td class="item key" scope="row">Tackles</td><td class="item stat null">8</td><td class="item stat null">9</td></tr><tr class="row"><td class="item key" scope="row">Fouls</td><td class="item stat null">3</td><td class="item stat null">3</td></tr><tr class="row"><td class="item key" scope="row">Corners</td><td class="item stat null">1</td><td class="item stat null">1</td></tr><tr class="row"><td class="item key" scope="row">Penalties</td><td class="item stat null">0</td><td class="item stat null">0</td></tr><tr class="row"><td class="item key" scope="row">Offsides</td><td class="item stat null">2</td><td class="item stat null">1</td></tr><tr class="row"><td class="item key" scope="row">Substitution</td><td class="item stat null">0</td><td class="item stat null">0</td></tr><tr class="row"><td class="item key" scope="row">Possession</td><td class="item stat null">66</td><td class="item stat null">34</td></tr><tr class="row"><td class="item key" scope="row">Attacks</td><td class="item stat null">65</td><td class="item stat null">14</td></tr><tr class="row"><td class="item key" scope="row">Dangerous Attacks</td><td class="item stat null">35</td><td class="item stat null">4</td></tr></tbody></table></div></div>

    dados_live = soup.find_all("tr", "row")
    #print(dados_live)

    ##### Funções #####

    dadosDisponivel = []
    def qtdItens(dados):  # informa quais dadso estão disponíveis
        total = len(dados)
        #total = 16
        n = 0
        cont = 0
        #dadosDisponivel=[]
        while cont <= total:
            #linhas= dados_live[cont]
            res = soup.find_all("td", scope="row")[cont].get_text()
            #print("\n")
            #print(f"{res}")
            dadosDisponivel.append(res)
            if(dadosDisponivel[cont] =='Dangerous Attacks' ):
                break
            cont += 1
            #return dadosDisponivel.append(res)
        #print(dadosDisponivel)
        return dadosDisponivel

    dadosListaItens = qtdItens(dados_live)
    print(f"lista fora: {dadosListaItens}")
    totalItens = len(dadosListaItens)
    totalDePosicoes = int(totalItens)-1

    def buscaPosicao(nome):
        loc = 0
        while loc <= totalItens:
            if dadosListaItens[loc] == str(nome):
                break
            else:
                return nome, -1
            loc += 1
        #print(f"\nO item {nome} esta na posição {loc} da lista.")
        return nome, loc


        ######## Chamda de Funções ##########

    #qtdItens(dados_live)

    #buscaPosicao('Free Kicks')

    print(f"Posição fora: {buscaPosicao('Free Kicks')}")

    #teste_Corners_casa = soup.find_all("td", "item stat null")[(buscaPosicao('Attacks'))*2].get_text()
    #teste__casa = soup.find_all("td", "item stat null")[buscaPosicao('Attacks')].get_text()
    #print(f"----- {teste__casa}-----")

    #teste_Corners_visitante = soup.find_all("td", "item stat null")[(buscaPosicao('Attacks') * 2)+1].get_text()
    #print(f"----{teste_Corners_visitante}----")




    ################### Quais Dados #########################

    #shots_totais = soup.find_all("td", scope="row")[shots_totais_loc].get_text()  # 0- inicia
    #shots_on_target = soup.find_all("td", scope="row")[shots_on_target_loc].get_text() #inicia
    #shots_off_target = soup.find_all("td", scope="row")[shots_off_target_loc].get_text() #inicia
    #free_kicks = soup.find_all("td", scope="row")[free_kicks_loc].get_text() #inicia
    #tackles = soup.find_all("td", scope="row")[buscaPosicao('Tackles')].get_text()
    #fouls = soup.find_all("td", scope="row")[buscaPosicao('Fouls')].get_text()
    #corners = soup.find_all("td", scope="row")[buscaPosicao('Corners')].get_text() #inicia
    #penalties = soup.find_all("td", scope="row")[buscaPosicao('Penalties')].get_text() #inicia
    #offsides = soup.find_all("td", scope="row")[buscaPosicao('Offsides')].get_text()
    #substitution = soup.find_all("td", scope="row")[buscaPosicao('Substitution')].get_text()
    #throw_ins = soup.find_all("td", scope="row")[buscaPosicao('Throw-ins')].get_text()
    #goal_kicks = soup.find_all("td", scope="row")[buscaPosicao('Goal Kicks')].get_text()
    #possession = soup.find_all("td", scope="row")[buscaPosicao('Possession')].get_text() #inicia
    #injuries = soup.find_all("td", scope="row")[buscaPosicao('Injuries')].get_text()
    #attacks = soup.find_all("td", scope="row")[buscaPosicao('Attacks')].get_text() #13 - inicia
    #dangerous_attacks = soup.find_all("td", scope="row")[buscaPosicao('Dangerous Attacks')].get_text()  # 14 ou 15 - inicia

        #######   Casa  ######

    time_casa = soup.find_all("th", "item stat")[0].get_text() #fixo
    gols_casa = soup.find_all("p", "ac fs2e bold")[0].get_text()[:-3] #fixo

    chutes_totais_casa = soup.find_all("td", "item stat null")[0].get_text() #fixo
    chutes_no_gol_casa = soup.find_all("td", "item stat null")[2].get_text() #fixo
    chutes_fora_casa = soup.find_all("td", "item stat null")[4].get_text() #fixo

    if(buscaPosicao('Free Kicks')[1] != -1): #mudei testar
        tirodemeta_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Free Kicks')[1]) * 2].get_text()  # as vezes não é informado os dados
    else:
        tirodemeta_casa = 0


    if (buscaPosicao('Tackles')[1] == -1):
        faltaIndireta_casa = 0
    else:
        faltaIndireta_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Tackles')[1])*2].get_text() #as vezes não é informado os dados

    if (buscaPosicao('Fouls')[1] == -1):
        faltasgerais_casa = 0
    else:
        faltasgerais_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Fouls')[1])*2].get_text() #as vezes não é informado os dados

    escanteio_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Corners')[1])*2].get_text()

    cobranca_penalties_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Penalties')[1])*2].get_text()

    if (buscaPosicao('Offsides')[1] == -1):
        impedimentos_casa = 0
    else:
        impedimentos_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Offsides')[1])*2].get_text() #as vezes não é informado os dados

    substituicao_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Substitution')[1])*2].get_text()

    if (buscaPosicao('Throw-ins')[1] == -1):
        lateral_casa = 0
    else:
        lateral_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Throw-ins')[1])*2].get_text() #as vezes não é informado os dados

    if (buscaPosicao('Goal Kicks')[1] == -1):
        faltasemgol_casa = 0
    else:
        faltasemgol_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Goal Kicks')[1])*2].get_text() #as vezes não é informado os dados

    possedebola_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Possession')[1])*2].get_text()

    if (buscaPosicao('Injuries') == ''):
        machucados_casa = 0
    else:
        machucado_casa  = soup.find_all("td", "item stat null")[int(buscaPosicao('Injuries')[1])*2].get_text()
    # injures #aparece de vez em quando nas estatisticas

    ataques_geral_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Attacks')[1])*2].get_text() #ok #[26]# não se altera [n]
    ataques_perigosos_casa = soup.find_all("td", "item stat null")[int(buscaPosicao('Dangerous Attacks')[1])*2].get_text() #ok # não se altera [n]

        ### Visitante ###

    time_visitante = soup.find_all("th", "item stat")[1].get_text() #fixo
    gols_visitante = soup.find_all("p", "ac fs2e bold")[0].get_text()[3:] #fixo

    chutes_totais_visitante = soup.find_all("td", "item stat null")[1].get_text() #fixo
    chutes_no_gol_visitante = soup.find_all("td", "item stat null")[3].get_text() #fixo
    chutes_fora_visitante = soup.find_all("td", "item stat null")[5].get_text() #fixo

    if (buscaPosicao('Free Kicks') == ''):
        tirodemeta_visitante = 0
    else:
        tirodemeta_visitante  = soup.find_all("td", "item stat null")[7].get_text()

    if (buscaPosicao('Tackles') == ''):
        faltaIndireta_visitante = 0
    else:
        faltaIndireta_visitante  = soup.find_all("td", "item stat null")[9].get_text()

    if (buscaPosicao('Fouls') == ''):
        faltasgerais_visitante = 0
    else:
        faltasgerais_visitante  = soup.find_all("td", "item stat null")[11].get_text()

    escanteio_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Corners')[1])*2)+1].get_text()

    cobranca_penalties_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Penalties')[1])*2)+1].get_text()

    if (buscaPosicao('Offsides') == ''):
        impedimentos_visitante = 0
    else:
        impedimentos_visitante  = soup.find_all("td", "item stat null")[17].get_text()

    substituicao_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Substitution')[1])*2)+1].get_text()

    if (buscaPosicao('Throw-ins') == ''):
        lateral_visitante = 0
    else:
        lateral_visitante  = soup.find_all("td", "item stat null")[21].get_text()

    if (buscaPosicao('Goal Kicks') == ''):
        faltasemgol_visitante = 0
    else:
        faltasemgol_visitante  = soup.find_all("td", "item stat null")[23].get_text()

    possedebola_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Possession')[1])*2)+1].get_text()

    if (buscaPosicao('Injuries') == ''):
        machucado_visitante = 0
    else:
        machucado_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Injuries')[1])*2)+1].get_text()
    #injures #aparece de vez em quando nas estatisticas

    ataques_geral_visitante  = soup.find_all("td", "item stat null")[(int(buscaPosicao('Attacks')[1])*2)+1].get_text()  # ok #27#fixo
    ataques_perigosos_visitante = soup.find_all("td", "item stat null")[(int(buscaPosicao('Dangerous Attacks')[1])*2)+1].get_text()  # ok #fixo



    #print(shots_totais, shots_on_target,shots_off_target,free_kicks,tackles,fouls,corners,penalties,offsides,substitution,throw_ins,goal_kicks,attacks,dangerous_attacks)


    # Tabela

    print('\n')
    print(f"Informações e estatísticas do {time_casa} x {time_visitante}")
    print("_" * 60)
    print('\n')

    tabela = [['Mercado',time_casa, 'x',time_visitante],
              ['Placar Atual', gols_casa,'',gols_visitante],
              ['Shots_totais',chutes_totais_casa,'',chutes_totais_visitante],
              ['Shots On Target',chutes_no_gol_casa,'',chutes_no_gol_visitante],
              ['Shots Off Target',chutes_fora_casa,'',chutes_fora_visitante],
              ['Free kicks (Tiro de Meta)',tirodemeta_casa,'',tirodemeta_visitante], #tirodemeta_visitante
              ['Tackles (Falta Indireta)',faltaIndireta_casa,'',faltaIndireta_visitante],
              ['Fouls (Faltas Totais)',faltasgerais_casa,'',faltasgerais_visitante],
              ['Corners',escanteio_casa,'',escanteio_visitante],
              ['Penalties',cobranca_penalties_casa,'',cobranca_penalties_visitante],
              ['Offsides',impedimentos_casa,'',impedimentos_visitante],
              ['Substitution',substituicao_casa,'',substituicao_visitante],
              ['Throw Ins',lateral_casa,'',lateral_visitante],
              ['Goal Kicks',tirodemeta_casa,'',tirodemeta_visitante],
              ['Possession',possedebola_casa,'',possedebola_visitante],
              ['Injuries',machucado_casa,'',machucado_visitante],
              ['Attacks',ataques_geral_casa,'',ataques_geral_visitante],
              ['Dangerous Attacks',ataques_perigosos_casa,'',ataques_perigosos_visitante]]


    print(tabulate(tabela, headers='firstrow', tablefmt='grid'))
    #, headers='firstrow', tablefmt='fancy_grid'
    # tabulate(tabela, headers='firstrow', tablefmt='grid')

    relogio = datetime.now()
    atual=relogio.strftime('%H:%M')
    print(f"\nAtualizado em: {atual}\n")
    time.sleep(120)