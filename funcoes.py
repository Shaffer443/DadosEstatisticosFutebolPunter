####### Funções pré #######



##### Calculos do time da CASA ####

def oddWinCasaTotal(jogos, vitorias):
        number_jogos = int(jogos)
        number_vitorias=int(vitorias)
        probabilidades = (number_vitorias/number_jogos)*100
        odds_validas = 100/probabilidades
        resposta = f"{odds_validas:.2f}"
        #print(f"     Probabilidades do evento: {probabilidades:.2f}% - Odds Válidas acima de {odds_validas:.2f}")

        return resposta

def over15Total(over15):
        config_number_over = over15[:-1]
        #print(config_number_over)
        number_over = float(config_number_over)
        odds_validas = 100/number_over
        resposta = f"{odds_validas:.2f}"
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return resposta
def over25Total(over25):
        config_number_over = over25[:-1]
        #print(config_number_over)
        number_over = float(config_number_over)
        odds_validas = 100/number_over
        resposta = f"{odds_validas:.2f}"
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return resposta

def medias(a,b):
        calculos = (float(a)+float(b))/2
        resposta = f"{calculos:.2f}"
        return resposta

#-------------------------------------------------------------------------------#
# Dados para os 6 ultimos jogos

def over15Total_6ultimos(over15_6ultimos):
        config_number_over_a = over15_6ultimos[:-2]
        config_number_over_b = over15_6ultimos[2:]

        #print(f"{config_number_over_a}-{config_number_over_b}")
        #print(type(config_number_over_b))

        number_over = (float(config_number_over_a)/float(config_number_over_b))*100
        porcentagem = f"{number_over:.2f}%"
        #print(porcentagem)
        config_porcentagem = porcentagem[:-1]
        odds_validas = 100/float(config_porcentagem)
        resposta = f"{odds_validas:.2f}"
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return porcentagem, resposta

def over25Total_6ultimos(over25_6ultimos):
        config_number_over_a = over25_6ultimos[:-2]
        config_number_over_b = over25_6ultimos[2:]

        #print(f"{config_number_over_a}-{config_number_over_b}")
        #print(type(config_number_over_b))

        number_over = (float(config_number_over_a)/float(config_number_over_b))*100
        porcentagem = f"{number_over:.2f}%"
        #print(porcentagem)
        config_porcentagem = porcentagem[:-1]
        odds_validas = 100/float(config_porcentagem)
        resposta = f"{odds_validas:.2f}"
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return porcentagem, resposta


############################### outras funções ##########################################

def evPositivo(jogos, wins, valorEntrada, oddsAtual):
        comissao=float(0.065) #6,5%

        probabilidade = wins/jogos
        #transf_probabilidade = probabilidade[:-1]
        #n_probabilidade = float(transf_probabilidade)
        #porcentagem_probabilidade = n_probabilidade/100

        n_valorEntrada = float(valorEntrada)

        n_oddsAtual = float(oddsAtual)
        porcentagem_odds = (1/n_oddsAtual)*100 #sem uso essa transformação

        calculo01 = ((n_oddsAtual-1)*n_valorEntrada)-n_valorEntrada
        green01 = n_valorEntrada+calculo01
        valorComissao = green01*comissao
        saldo01 = green01-valorComissao

        greenfinal = probabilidade*saldo01

        # red:

        red_max = -n_valorEntrada
        porcentagem_red = 1.00-probabilidade
        redfinal =  porcentagem_red*red_max

        saldoOperacao = greenfinal+redfinal # subtração pq o red já vem negativo

        if(saldoOperacao <= 0):
                print('Operação com prejuizo com esta odds: # NÃO OPERAR - Prejuízo a longo prazo. # !')
                return print('Prejuizo')
        else:
                print(f"Operação com Lucatividade de R${saldoOperacao:.2f} \n- Lucro a longo prazo com esta odds de {n_oddsAtual} com a probabilidade de {porcentagem_odds:.2f}% !")
                return saldoOperacao,n_oddsAtual, porcentagem_odds
        #print(saldoOperacao)
        #print(redfinal)
        #print(red_max)
        #print(porcentagem_red)
        #print(greenfinal)
        #print(calculo01,valorComissao, saldo01)

#evPositivo(16,7,'100.00','2.10')

def previssoesGols(mediaGolsCasa,mediasGolsVisitante):
        number_mediaGolsCasa = float(mediaGolsCasa)
        number_mediaGolsVisitante = float(mediasGolsVisitante)

        mediaGeral = (number_mediaGolsCasa+number_mediaGolsVisitante)/2

        if (mediaGeral < 1.5):
                return "Under"
        if(mediaGeral >= 1.5 and mediaGeral <= 2.0):
                return "Over 1.5"
        elif (mediaGeral > 2.0 and mediaGeral <= 3.0):
                return "Over 2.5"
        else:
                return "Over 3.5"



def evPositivoPunter(jogos, wins, valorEntrada, oddsAtual):
        comissao=float(0.065) #6,5%
        int_jogos = int(jogos)
        int_wins = int(wins)

        probabilidade = int_wins/int_jogos
        #transf_probabilidade = probabilidade[:-1]
        #n_probabilidade = float(transf_probabilidade)
        #porcentagem_probabilidade = n_probabilidade/100

        n_valorEntrada = float(valorEntrada)

        n_oddsAtual = float(oddsAtual)
        porcentagem_odds = (1/n_oddsAtual)*100 #sem uso essa transformação

        calculo01 = ((n_oddsAtual-1)*n_valorEntrada)-n_valorEntrada
        green01 = n_valorEntrada+calculo01
        valorComissao = green01*comissao
        saldo01 = green01-valorComissao

        greenfinal = probabilidade*saldo01

        # red:

        red_max = -n_valorEntrada
        porcentagem_red = 1.00-probabilidade
        redfinal =  porcentagem_red*red_max

        saldoOperacao = greenfinal+redfinal # subtração pq o red já vem negativo

        calculo_probabilidade = probabilidade - porcentagem_red

        if(calculo_probabilidade < 0): #avaliar os divisores em testes
                if(calculo_probabilidade > -0.07):
                        porcentagem_premissa = (calculo_probabilidade/1.2)*-1 #deixando positivo
                        valor_Premissa_odds_porcentagem = float(oddsAtual)*porcentagem_premissa
                        oddsPremissa = float(oddsAtual)+valor_Premissa_odds_porcentagem
                        resultado = f"{oddsPremissa:.2f}"
                        # print(oddsPremissa)
                        return resultado
                elif (calculo_probabilidade < -0.07 and calculo_probabilidade >= -0.15 ):
                        porcentagem_premissa = (calculo_probabilidade / 4.8) * -1  # deixando positivo 1.2*4=4.8
                        valor_Premissa_odds_porcentagem = float(oddsAtual) * porcentagem_premissa
                        oddsPremissa = float(oddsAtual) + valor_Premissa_odds_porcentagem
                        resultado = f"{oddsPremissa:.2f}"
                        # print(oddsPremissa)
                        return resultado
                elif (calculo_probabilidade < -0.15 ):
                        porcentagem_premissa = (calculo_probabilidade / 7.2) * -1  # deixando positivo 1.2*6=9.7.2
                        valor_Premissa_odds_porcentagem = float(oddsAtual) * porcentagem_premissa
                        oddsPremissa = float(oddsAtual) + valor_Premissa_odds_porcentagem
                        resultado = f"{oddsPremissa:.2f}"
                        # print(oddsPremissa)
                        return resultado
        else:
                if(calculo_probabilidade <= 0.15):
                        porcentagem_premissa = (calculo_probabilidade / 3) #verificar as divisões
                        valor_Premissa_odds_porcentagem = float(oddsAtual) * porcentagem_premissa
                        oddsPremissa = float(oddsAtual) + valor_Premissa_odds_porcentagem
                        resultado = f"{oddsPremissa:.2f}"
                        # print(oddsPremissa)
                        return resultado
                elif(calculo_probabilidade > 0.15 and calculo_probabilidade <= 0.30 ):
                        porcentagem_premissa = (calculo_probabilidade / 6)  # verificar as divisões
                        valor_Premissa_odds_porcentagem = float(oddsAtual) * porcentagem_premissa
                        oddsPremissa = float(oddsAtual) + valor_Premissa_odds_porcentagem
                        resultado = f"{oddsPremissa:.2f}"
                        # print(oddsPremissa)
                        return resultado
                elif (calculo_probabilidade > 0.30 and calculo_probabilidade <= 0.60):
                        porcentagem_premissa = (calculo_probabilidade / 9)  # verificar as divisões
                        valor_Premissa_odds_porcentagem = float(oddsAtual) * porcentagem_premissa
                        oddsPremissa = float(oddsAtual) + valor_Premissa_odds_porcentagem
                        resultado=f"{oddsPremissa:.2f}"
                        #print(oddsPremissa)
                        return resultado
        #print(probabilidade)
        #print(porcentagem_red)

#x=evPositivoPunter(44,31,'100.00','1.42')
#print(x)


######## Funções Live ########

