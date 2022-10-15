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

    do{
        printf("\n");
        puts("1. Validar uma Probabilidade.");
        puts("2. Transformar Odds em Porcentagem.");
        puts("3. Transformar Porcentagem em Odds.");
        puts("4. Porcentagem de Acertabilidade de entradas Punter.");
        puts("5. Probabilidade de Over - Under.");
        puts("6. Criterio de Kelly.");
        puts("7. Sair");
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

        /*
        Kelly = (BP – Q) / B

        B = (Odd da Casa) – 1
        P = Probabilidade de o resultado acontecer (de acordo com sua opinião)
        Q = Probabilidade de o resultado não acontecer, ou seja 1 – P
        */





        puts("\n  Método Critério de Kelly Simples");
        puts("-------------------------------------\n");

        /*printf("Qual o valor da odds do time da casa? use ponto (.):  ");
        scanf("%f",&casa);

        favor = (1/casa);
        contra = (1.00 - favor);

        kelly = ((casa - 1) * (favor-contra))/(casa-1);
        kellyporc = kelly*100;

        printf("\n %.4f ou %.2f % \n", kelly, kellyporc);

        if (kelly >= 0.05){

        puts("\n* Tem +EV * \n");

         } else{

           puts("\n * Não vale a operação * \n");

            };*/

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

    /*O resultado acima deu negativo, e você deve estar se perguntando se há algo de errado com o cálculo. Não, não há.

      Isso ocorre porque segundo o Critério de Kelly não compensa apostar nesse resultado com essa odd de vitória para o Time casa ser negativo.

      Por quê?

      Porque a odds que a casa colocou na vitória do Time da Casa, significa que a casa acha que a probabilidade do time vencer não vale a opereção.

      Se a casa dá uma chance de vitória Time da Casa maior do que a que a gente acha que é verdadeira, então não compensa apostar nesse resultado. Não é uma aposta de valor!

      Mas vamos a um exemplo quando o critério é positivo, o Critério de Kelly nos diz que você deve apostar o valor que a % mencionar da sua banca na vitória.

      Isso só é possível levando em consideração a odd da casa e a probabilidade real de o evento acontecer.

      Aqui identificamos um pequeno problema do método: pode acontecer de o método sugerir apostar porcentagens muito altas da sua banca.

      Cabe o discernimento do apostador em decidir se vale a pena fazer a aposta ou não. É costume no Critério de Kelly estabelecer um teto porcentual máximo.*/



        case 7:

            printf("fechando Sistema...\n"); /* não está fechando e saindo*/

        default:
            printf("\nErro. Opcao Invalida. Digite uma opcao do Menu abaixo:\n\n"); //digitando 4 está aparecendo esta messagem.
            break;
        }




    }while(opcao!=7);

    return 0;
}
