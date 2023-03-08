

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
