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

    dadosDisponivel = []
    def qtdItens():  # informa quais dadso estão disponíveis
        #total = len(dados_live)
        total = 16
        n = 0
        cont = 0
        #dadosDisponivel=[]
        while cont <= total:
            #linhas= dados_live[cont]
            res = soup.find_all("td", scope="row")[cont].get_text()
            #print(f"{res}\n")
            dadosDisponivel.append(res)

            if(dadosDisponivel[cont] =='Dangerous Attacks' ):
                break
            cont += 1
            #return dadosDisponivel.append(res)
        print(dadosDisponivel)
        return dadosDisponivel

    def buscaPosicao(busca):
        #qtd = len(listaBusca)
        #print(qtd)
        cont = 0
        for localizacao in dadosDisponivel:
            #print(f"[{cont}]{localizacao}")
            if localizacao == f"{busca}":
                print(cont)
                return cont
                break
            #else:
            #    return False
            cont += 1

        #return cont




    qtdItens()

    #buscaPosicao('Injuries')

    shots_totais_loc = buscaPosicao('Shots Total')
    shots_on_target_loc = buscaPosicao('Shots On Target')
    shots_off_target_loc = buscaPosicao('Shots Off Target')
    #free_kicks_loc = buscaPosicao('Free Kicks')
    free_kicks_loc = {buscaPosicao('Free Kicks'):[soup.find_all("td", "item stat null")[6].get_text(),soup.find_all("td", "item stat null")[7].get_text()]}

    #print(dados_live)
    #print(len(dados_live))
    #total = len(dados_live)

    #dados_live2 = soup.find_all("th", "item stat")
    #print(dados_live2)

    ################### Quais Dados #########################

    shots_totais = soup.find_all("td", scope="row")[shots_totais_loc].get_text()  # 0- inicia
    shots_on_target = soup.find_all("td", scope="row")[shots_on_target_loc].get_text() #inicia
    shots_off_target = soup.find_all("td", scope="row")[shots_off_target_loc].get_text() #inicia
    free_kicks = soup.find_all("td", scope="row")[free_kicks_loc].get_text() #inicia
    tackles = soup.find_all("td", scope="row")[buscaPosicao('Tackles')].get_text()
    fouls = soup.find_all("td", scope="row")[buscaPosicao('Fouls')].get_text()
    corners = soup.find_all("td", scope="row")[buscaPosicao('Corners')].get_text() #inicia
    penalties = soup.find_all("td", scope="row")[buscaPosicao('Penalties')].get_text() #inicia
    offsides = soup.find_all("td", scope="row")[buscaPosicao('Offsides')].get_text()
    substitution = soup.find_all("td", scope="row")[buscaPosicao('Substitution')].get_text()
    throw_ins = soup.find_all("td", scope="row")[buscaPosicao('Throw-ins')].get_text()
    goal_kicks = soup.find_all("td", scope="row")[buscaPosicao('Goal Kicks')].get_text()
    possession = soup.find_all("td", scope="row")[buscaPosicao('Possession')].get_text() #inicia
    injuries = soup.find_all("td", scope="row")[buscaPosicao('Injuries')].get_text()
    attacks = soup.find_all("td", scope="row")[buscaPosicao('Attacks')].get_text() #13 - inicia
    dangerous_attacks = soup.find_all("td", scope="row")[buscaPosicao('Dangerous Attacks')].get_text()  # 14 ou 15 - inicia

        #######   Casa  ######

    time_casa = soup.find_all("th", "item stat")[0].get_text() #fixo
    gols_casa = soup.find_all("p", "ac fs2e bold")[0].get_text()[:-3] #fixo

    chutes_totais_casa = soup.find_all("td", "item stat null")[0].get_text() #fixo
    chutes_no_gol_casa = soup.find_all("td", "item stat null")[2].get_text() #fixo
    chutes_fora_casa = soup.find_all("td", "item stat null")[4].get_text() #fixo

    tirodemeta_casa = soup.find_all("td", "item stat null")[6].get_text() #as vezes não é informado os dados

    faltaIndireta_casa = soup.find_all("td", "item stat null")[8].get_text() #as vezes não é informado os dados

    faltasgerais_casa = soup.find_all("td", "item stat null")[10].get_text() #as vezes não é informado os dados
    escanteio_casa = soup.find_all("td", "item stat null")[12].get_text()
    #escanteio_casa = soup.find_all("td", "item stat null")[12].get_text()
    cobranca_penalties_casa = soup.find_all("td", "item stat null")[14].get_text()
    impedimentos_casa = soup.find_all("td", "item stat null")[16].get_text() #as vezes não é informado os dados
    substituicao_casa = soup.find_all("td", "item stat null")[18].get_text()
    #substituicao_casa = soup.find_all("td", "item stat null")[18].get_text()
    lateral_casa = soup.find_all("td", "item stat null")[20].get_text() #as vezes não é informado os dados
    #posse_de_bola_casa = soup.find_all("td", "item stat null")[20].get_text()
    faltasemgol_casa = soup.find_all("td", "item stat null")[22].get_text() #as vezes não é informado os dados

    possedebola_casa = soup.find_all("td", "item stat null")[24].get_text()
    # injures #aparece de vez em quando nas estatisticas
    ataques_geral_casa = soup.find_all("td", "item stat null")[24].get_text() #ok #[26]# não se altera [n]
    #ataques_perigosos_casa = soup.find_all("td", "item stat null")[24].get_text()
    ataques_perigosos_casa = soup.find_all("td", "item stat null")[24].get_text() #ok # não se altera [n]

        ### Visitante ###

    time_visitante = soup.find_all("th", "item stat")[1].get_text() #fixo
    gols_visitante = soup.find_all("p", "ac fs2e bold")[0].get_text()[3:] #fixo

    chutes_totais_visitante = soup.find_all("td", "item stat null")[1].get_text() #fixo
    chutes_no_gol_visitante = soup.find_all("td", "item stat null")[3].get_text() #fixo
    chutes_fora_visitante = soup.find_all("td", "item stat null")[5].get_text() #fixo

    tirodemeta_visitante  = soup.find_all("td", "item stat null")[7].get_text()

    faltaIndireta_visitante  = soup.find_all("td", "item stat null")[9].get_text()

    faltasgerais_visitante  = soup.find_all("td", "item stat null")[11].get_text()
    escanteio_visitante  = soup.find_all("td", "item stat null")[13].get_text()
    # escanteio_casa = soup.find_all("td", "item stat null")[12].get_text()
    cobranca_penalties_visitante  = soup.find_all("td", "item stat null")[15].get_text()
    impedimentos_visitante  = soup.find_all("td", "item stat null")[17].get_text()
    substituicao_visitante  = soup.find_all("td", "item stat null")[19].get_text()
    # substituicao_casa = soup.find_all("td", "item stat null")[18].get_text()
    lateral_visitante  = soup.find_all("td", "item stat null")[21].get_text()
    # posse_de_bola_casa = soup.find_all("td", "item stat null")[20].get_text()
    faltasemgol_visitante  = soup.find_all("td", "item stat null")[23].get_text()

    possedebola_visitante  = soup.find_all("td", "item stat null")[25].get_text()
    #injures #aparece de vez em quando nas estatisticas
    ataques_geral_visitante  = soup.find_all("td", "item stat null")[25].get_text()  # ok #27#fixo
    # ataques_perigosos_casa = soup.find_all("td", "item stat null")[24].get_text()
    ataques_perigosos_visitante = soup.find_all("td", "item stat null")[25].get_text()  # ok #fixo



    #print(shots_totais, shots_on_target,shots_off_target,free_kicks,tackles,fouls,corners,penalties,offsides,substitution,throw_ins,goal_kicks,attacks,dangerous_attacks)


    # Tabela

    print('\n')
    print(f"Informações e estatísticas do {time_casa} x {time_visitante}")
    print("_" * 60)
    print('\n')

    tabela = [['Mercado',time_casa, 'x',time_visitante],
              ['Placar Atual', gols_casa,'',gols_visitante],
              [shots_totais,chutes_totais_casa,'',chutes_totais_visitante],
              [shots_on_target,chutes_no_gol_casa,'',chutes_no_gol_visitante],
              [shots_off_target,chutes_fora_casa,'',chutes_fora_visitante],
              [free_kicks +'(Tiro de Meta)',free_kicks_loc[0],'',free_kicks_loc[1]], #tirodemeta_visitante
              [tackles +'(Falta Indireta)',faltaIndireta_casa,'',faltaIndireta_visitante],
              [fouls + '(Faltas Totais)',faltasgerais_casa,'',faltasgerais_visitante],
              [corners,escanteio_casa,'',escanteio_visitante],
              [penalties,cobranca_penalties_casa,'',cobranca_penalties_visitante],
              [offsides,impedimentos_casa,'',impedimentos_visitante],
              [substitution,substituicao_casa,'',substituicao_visitante],
              [throw_ins,lateral_casa,'',lateral_visitante],
              [goal_kicks,tirodemeta_casa,'',tirodemeta_visitante],
              [possession,possedebola_casa,'',possedebola_visitante],
              [injuries,'','',''],
              [attacks,ataques_geral_casa,'',ataques_geral_visitante],
              [dangerous_attacks,ataques_perigosos_casa,'',ataques_perigosos_visitante]]

    #tabela = [['Mercado',time_casa, 'x',time_visitante],
    #          ['Placar Atual', gols_casa,'',gols_visitante],
    #          [shots_totais,chutes_totais_casa,'',chutes_totais_visitante],
    #          [shots_on_target,chutes_no_gol_casa,'',chutes_no_gol_visitante],
    #          [shots_off_target,chutes_fora_casa,'',chutes_fora_visitante],
    #          [tackles,existencia(roubada_de_bola_casa),'',existencia(roubada_de_bola_visitante)],
    #          [fouls,existencia(faltas_casa),'',existencia(faltas_visitante)]]



    print(tabulate(tabela, headers='firstrow', tablefmt='grid'))
    #, headers='firstrow', tablefmt='fancy_grid'
    # tabulate(tabela, headers='firstrow', tablefmt='grid')

    relogio = datetime.now()
    atual=relogio.strftime('%H:%M')
    print(f"\nAtualizado em: {atual}\n")
    time.sleep(120)