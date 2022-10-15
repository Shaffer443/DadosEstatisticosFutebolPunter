#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    printf("Sistema de Conversoes & Probabilidades Para Entradas Esportivas");
    printf("Ultima atualizacao: 15/10/2022 (Versao 1.2.3)\n");
    printf("@github: Shaffer443 - Instagram: @rafaelgouveiashaffer\n\n");

    int opcao, entradas, green, red;
    float odds, porcentagem, resultado1, resultado2, resultado2_1, resultado3;
    float mediagols, total, media1, media2, media3;
    float casa,favor,contra,kelly,kellyporc;
    int jogos, contador, gols, over1=2, over2=3, over3=4, cont1=0, cont2=0, cont3=0;
    float odds_atual, stake_max, ganhos_max, red_ajustes_max, transf_adds_atual, transf_ganhos_max, transf_red_ajustes_max, r,calc_1, calc_2, calc_x, stakeideal, valor_sugerido,valor_sugerido_stake;
    float prob_red_ajuste, trans_prob_green_do_evento, trans_prob_red_ajuste, trans_odds, trans_comissao_trade, prob_green_do_evento, comissao_trade, stake, valor_bruto_do_green, valor_liquido_comissao, valor_liquido_do_green , faturamento_green, faturamento_red, saldo_da_operacao;


    do{
        printf("\n");
        puts("1. Validar uma Probabilidade.");
        puts("2. Transformar Odds em Porcentagem.");
        puts("3. Transformar Porcentagem em Odds.");
        puts("4. Porcentagem de Acertabilidade de entradas Punter.");
        puts("5. Probabilidade de Over - Under.");
        puts("6. Criterio de Kelly.");
        puts("7. EV+");
        puts("8. Sair");
        printf("Digite a opcao desejada: ");
        scanf("%d", &opcao);

        switch (opcao){
        case 1:
            printf("\nDigite o total de jogos para analisar: ");
            scanf("%d", &entradas);
            printf("\nDigite o total de acertos (green): ");
            scanf("%d", &green);
            resultado3 = (green*100)/entradas;
            red = entradas - green;

                printf("\n>> Com suas %d Entradas(Operacoes), voce teve a %d acertos(green) e %d red(s), e teve %.2f de sucesso.\n", entradas, green, red, resultado3);

                if ( resultado3 > 80){
                    printf("\nProbabilidade #Alta#\n\n");
                } else if (resultado3 >= 65 && resultado3 <= 80){
                    printf("\nProbabilidade #Moderada#\n\n");
                } else {
                    printf("\nProbabilidade #Baixa#\n\n");
                }
            break;
        case 2:
            printf("\nDigite o valor da odds: ");
            scanf("%f", &odds);
            resultado1 = (1/odds)*100;
                printf(">> Para a Odds %1.2f, voce tem a probabilidade de %2.2f % de acerto.\n\n", odds, resultado1);
            break;
        case 3:
            printf("\nDigite o valor da Porcentagem:  ");
            scanf("%f", &porcentagem);
            resultado2 = (porcentagem/100);
            resultado2_1 = 1/resultado2;
                printf(">> Para a Porcentagem de %2.2f, voce tem a Odds Justa de %1.2f .\n\n", porcentagem, resultado2_1);
            break;

        case 4:

            printf("\nDigite o total das Entradas: ");
            scanf("%d", &entradas);
            printf("\nDigite o total de acertos (green): ");
            scanf("%d", &green);
            resultado3 = (green*100)/entradas;
            red = entradas - green;

                printf(">> Com suas %d Entradas(Operacoes), voce teve a %d acertos(green) e %d red(s), e teve %.2f de sucesso.\n\n", entradas, green, red, resultado3);
            break;

        case 5:


            printf("\nNumero total de jogos para analisar: ");
            scanf("%d", &jogos);


            printf("\nDigite os dados dos %d jogos... \n", jogos);

            for (contador = 1 ; contador <= jogos ; contador ++ ){
                printf ("\nDigite os gols da partida: ");
                    scanf("%d", &gols);
                        total= total + gols;

            if(gols >= over1){
                cont1++;
                    }if(gols >= over2){
                        cont2++;
                            } if(gols >= over3){
                                cont3++;
                }
            }

        media1 = (cont1*100)/jogos;
         media2 = (cont2*100)/jogos;
          media3 = (cont3*100)/jogos;

        printf("\n>> Partidas Over 1.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media1, cont1, jogos);

            if ( media1 > 85){
                printf("\n# Altissima Prababilidade #\n");
                    }if ( media1 >= 75 && media1 < 85){
                        printf("\n# Alta Prababilidade #\n");
                            } if ( media1 >= 65 && media1 <75){
                                printf("\n# Moderada Prababilidade #\n");
                                    } if (media1 < 65){
                                        printf("\n# Baixa Probabilidade #\n");
                                        }


            printf("\n>> Partidas Over 2.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media2, cont2, jogos);
                                            // so  o 2.5 está retornando numeros errados nos dois primeiros resulatdos do printf.
                 if ( media2 > 85){
                    printf("\n# Altissima Prababilidade #\n");
                        }if ( media2 >= 75 && media2 < 85){
                            printf("\n# Alta Prababilidade #\n");
                                } if ( media2 >= 65 && media2 <75){
                                    printf("\n# Moderada Prababilidade #\n");
                                        } if (media2 < 65){
                                            printf("\n# Baixa Probabilidade #\n");
                                            }


                printf("\n>> Partidas Over 3.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media3, cont3, jogos);

                    if ( media3 > 85){
                    printf("\n# Altissima Prababilidade #\n");
                        }if ( media3>= 75 && media1 < 85){
                            printf("\n# Alta Prababilidade #\n");
                                } if ( media3 >= 65 && media1 <75){
                                    printf("\n# Moderada Prababilidade #\n");
                                        } if (media3 < 65){
                                            printf("\n# Baixa Probabilidade #\n\n");
                                            }




                            mediagols = total / jogos;

                            puts("--------------------------------");
                            printf(">> Media de Gols = %1.1f\n", mediagols);
                            puts("--------------------------------");
                            puts("\n");


                            break;



        case 6:

        puts("\n  Método Critério de Kelly Simples");
        puts("-------------------------------------\n");


        printf("Qual Odds do mercado para o evento:");
        scanf("%f",&odds_atual);

        printf("Valor máximo de entrada da stake (valor int):");
        scanf("%f",&stake_max);

        printf("Qual a probabilidade(%) maxima, esperada para o green:");
        scanf("%f",&ganhos_max);

        printf("Qual a probabilidade(%) maxima de stop lost para um red ou ajustes: ");
        scanf("%f",&red_ajustes_max);

        /*Transformando as porcentagens:*/
        transf_adds_atual = odds_atual/100;
        transf_ganhos_max = ganhos_max/100;
        transf_red_ajustes_max = red_ajustes_max/100;

        r = transf_ganhos_max/transf_red_ajustes_max;

        calc_1=1-transf_adds_atual;
        calc_2=transf_ganhos_max/transf_red_ajustes_max;
        calc_x =calc_1/calc_2;
        stakeideal = transf_adds_atual - calc_x;
        valor_sugerido = stake_max*stakeideal;
        valor_sugerido_stake = stake_max-valor_sugerido ;


        printf("\n\nEntrada ideal R$ %.2f \n",valor_sugerido_stake);
        printf("Ajuste da stake de R$ %.2f, equivalente a %.2f \n",valor_sugerido,stakeideal);

        break;

        case 7:
            /* Confirmar se tal valor de odds do evento, vale a entrda ou não na operação*/

            printf("Probabilidade(%) do evento ocorrer: ");
            scanf("%f",&prob_green_do_evento);
            printf("Porcentagem da comissao(%): ");
            scanf("%f",&comissao_trade);
            printf("Valor(R$) da stake para operação: ");
            scanf("%f",&stake);
            printf("Odds ofertada para o evento: ");
            scanf("%f",&odds);

            /*Transformações das porcentagens em decimal*/

            trans_comissao_trade = comissao_trade/100;
            trans_odds = odds-1; /*observar isso*/

            /*Valor para operação*/
            valor_bruto_do_green = stake * trans_odds;

            valor_liquido_comissao = valor_bruto_do_green*trans_comissao_trade;

            valor_liquido_do_green = valor_bruto_do_green - valor_liquido_comissao;

            /*Tratamento da probabilidade*/
            prob_red_ajuste = 100 - prob_green_do_evento;

            trans_prob_green_do_evento = prob_green_do_evento/100;
            trans_prob_red_ajuste = prob_red_ajuste/100;

            /*valores finais para cada green e red*/
            faturamento_green= valor_liquido_do_green * trans_prob_green_do_evento;

            faturamento_red= -stake * trans_prob_red_ajuste;
            saldo_da_operacao = faturamento_green+faturamento_red;

            if(saldo_da_operacao>0){
              printf("\n< EV+ > - Operação tem valor. Lucro por operação GREEN de R$ %.2f \n", saldo_da_operacao);

            }else{
              printf("\nEsta operação não tem valor. Prejuizo por peração de R$ %.2f\n", saldo_da_operacao);
            }
             break;

        case 8:

            printf("fechando Sistema...\n");
            break;

        default:
            printf("\nErro. Opcao Invalida. Digite uma opcao do Menu abaixo:\n\n"); //digitando 4 está aparecendo esta messagem.
            break;
        }




    }while(opcao!=8);

    return 0;
}
