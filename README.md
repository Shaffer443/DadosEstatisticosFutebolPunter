# Dados Estatísticos, Informações de Probabilidades Punter no Futebol

Programa em linguagem C para ajudar, de forma pontual, algumas diretrizes para auxiliar em uma entrada Punter nas apostas esportivas de futebol.

Tais como:

- Odds válidas
- Transformar Porcentagem em Odds
- Transformar Odds em Poercentagem

Além de analises pontuais e verificações simples, pela média, por exemplo:

- Validar uma Probabilidade
- Porcentagem de Acertabilidade de entradas Punter
- Probabilidade de Over - Under.

Este sistema foi criado para uso pessoal, como exercício em uma atividade de _lógica de programação_, onde aprendiamos em _linguamgem C_. 
Decidi criar um sistema, que não precisa ser intalado, bastando baixar os arquivos do repositorio e clicar em _main.exe_, para que se abra em _terminal cmd_ e possa ser utilizado.

[Imagem](https://github.com/Shaffer443/DadosEstatisticosFutebolPunter/blob/6c81dd24b04ca8e47ee901ff5f18ef69fb96dd5b/ProgramaAn%C3%A1lise%20DeOdds_Porcentagens_outros_executavel.png?raw=true)


## Explicando cada função do Switch Case (Opções):

#_1. Validar uma Probabilidade_

Escolhendo esta opção, o sistema pedira a inserção de _Digite o total de jogos para analisar:_ e _Digite o total de acertos (green):_. 
Com esses dados o sitema retornará uma probabilidade.

Exemplo:

_Digite a opcao desejada: 1_

_Digite o total de jogos para analisar: 10_

_Digite o total de acertos (green): 5_

_Com suas 10 Entradas(Operacoes), voce teve a 5 acertos(green) e 5 red(s), e teve 50.00 de sucesso._

Premissa desta opção é levantar de forma simples, uma probabilidade em porcentagem (%), que pode ser usado para se ter um Odds com uma média para a operação analisada
e com isso, adiocnar a Odds ticks que a tornem com +EV.

#_2. Transformar Odds em Porcentagem e 3. Transformar Porcentagem em Odds_

- Transformar Odds em Porcentagem: solicita ao usuário uma valor de Odds (usando ponto "." e não virgula), e recebe a porcentagem da probabilidade referente a odds inserida.
- Transformar Porcentagem em Odds: solicita ao usuário uma valor de porcentagem (usando ponto "." e não virgula), e recebe a odds referente a porcentagem inserida.

#_4. Porcentagem de Acertabilidade de entradas Punter_

Praticamento faz o mesmo que a opção: _1. Validar uma Probabilidade_, porém, analisa mais uma acertivaidade de operações feitas. No geral, o mecanismo informa resulatdos similares.

Exemplo:

_Digite o total das Entradas: 10_

_Digite o total de acertos (green): 5_
_Com suas 10 Entradas(Operacoes), voce teve a 5 acertos(green) e 5 red(s), e teve 50.00 de sucesso._

#_5. Probabilidade de Over - Under_

Através de inputs de numeros de partidas (eventos), e seus respectivos numeros de gols totais ocorridos nessas aprtidas, o sistema informará a probabiidades de um Over 1,5 | Over 2,5 | Over 3,5.

Através dessas procentagens informadas, se pode ter uma noção se é melhro usar uma Under ou Over nas operações de gols. 

Exemplo:

_Numero total de jogos para analisar: 10_

_Digite os dados dos 10 jogos..._

_Digite os gols da partida: 2_

_Digite os gols da partida: 3_

_Digite os gols da partida: 5_

_Digite os gols da partida: 4_

_Digite os gols da partida: 8_

_Digite os gols da partida: 7_

_Digite os gols da partida: 2_

_Digite os gols da partida: 1_

_Digite os gols da partida: 1_

_Digite os gols da partida: 1_

_Partidas Over 1.5 tem porcentagem de 70.00  de probabilidade de ocorrer, em 7 partidas de um total de 10._

_# Moderada Prababilidade #_

_Partidas Over 2.5 tem porcentagem de 50.00  de probabilidade de ocorrer, em 5 partidas de um total de 10._

_# Baixa Probabilidade #_

_Partidas Over 3.5 tem porcentagem de 40.00  de probabilidade de ocorrer, em 4 partidas de um total de 10._

_# Baixa Probabilidade #_

--------------------------------
_Media de Gols = 3.4_
--------------------------------

#_6. Criterio de Kelly_

A princípio, a Fórmula de Kelly é muito simples. A fórmula diz que o valor da sua aposta deve ser tão grande quanto a probabilidade de ganhar menos a probabilidade de perder. Se você tem 55% de chance de ganhar e 45% de chance de perder, você deve apostar 10% da sua banca (55-45 = 10). Como mencionamos anteriormente, a fórmula impede que você faça uma aposta quando o valor é zero ou menos. O sistema reduz a possibilidade de você perder todo seu dinheiro, pois pressupõe que você sempre aposta uma porcentagem da sua banca.

Você pensou em apostar no Time A para vencer o Time B. Segundo a sua análise, o Time A tem 50% de chance de ganhar. Isso significa que há 50% de chance de o jogo terminar empatado ou de o Time B vencer, o que seria uma perda para você. A casa de apostas oferece odds de 2.10 para o Time A vencer. Usando esses dados na fórmula ficaria:

(0,50 x 2,10 - 1) / (2,10 - 1) = 0,045

De acordo com a Fórmula de Kelly, você deve apostar 4,5% da sua banca neste jogo, pois esta é a vantagem que você tem sobre a casa de apostas.

#OBS: Está função está incompleta, precisa de ajustes.

Exemplo:

_MÚtodo CritÚrio de Kelly Simples_
-------------------------------------

_Qual o valor da odds do time da casa? use ponto (.):  1.45_

 _0.3793 ou 37.93_

* Tem +EV *
