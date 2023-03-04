

##### Calculos do time da CASA ####

def oddWinCasaTotal(jogos, vitorias):
        number_jogos = int(jogos)
        number_vitorias=int(vitorias)
        probabilidades = (number_vitorias/number_jogos)*100
        odds_validas = 100/probabilidades

        #print(f"     Probabilidades do evento: {probabilidades:.2f}% - Odds Válidas acima de {odds_validas:.2f}")

        return odds_validas

def over15CasaTotal(over15):
        config_number_over = over15[:-1]
        #print(config_number_over)
        number_over = float(config_number_over)
        odds_validas = 100/number_over
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return odds_validas

def over25CasaTotal(over25):
        config_number_over = over25[:-1]
        #print(config_number_over)
        number_over = float(config_number_over)
        odds_validas = 100/number_over
        #print(f"     Odds Válidas acima de {odds_validas:.2f}")
        return odds_validas