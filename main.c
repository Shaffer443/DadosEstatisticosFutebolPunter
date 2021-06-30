#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    printf("Sistema de Conversao & Probabilidades Pre-Jogos - Ultima atualizacao: 07/06/2021 (Versao 1.2.1)\n");
    printf("@github: Shaffer443 - Instagram: @rafaelgouveiashaffer\n\n");

    int opcao, entradas, green, red;
    float odds, porcentagem, resultado1, resultado2, resultado2_1, resultado3;
    float mediagols, total, media1, media2, media3;
    int jogos, contador, gols, over1=2, over2=3, over3=4, cont1=0, cont2=0, cont3=0;

    do{
        puts("1. Validar uma Probabilidade.");
        puts("2. Transformar Odds em Porcentagem.");
        puts("3. Transformar Porcentagem em Odds.");
        puts("4. Porcentagem de Acertabilidade de entradas Punter.");
        puts("5. Probabilidade de Over - Under.");
        puts("6. Sair");
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

                printf("\nCom suas %d Entradas(Operacoes), voce teve a %d acertos(green) e %d red(s), e teve %.2f de sucesso.\n", entradas, green, red, resultado3);

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
                printf("Para a Odds %1.2f, voce tem a probabilidade de %2.2f % de acerto.\n\n", odds, resultado1);
            break;
        case 3:
            printf("\nDigite o valor da Porcentagem:  ");
            scanf("%f", &porcentagem);
            resultado2 = (porcentagem/100);
            resultado2_1 = 1/resultado2;
                printf("Para a Porcentagem de %2.2f, voce tem a Odds Justa de %1.2f .\n\n", porcentagem, resultado2_1);
            break;

        case 4:

            printf("\nDigite o total das Entradas: ");
            scanf("%d", &entradas);
            printf("\nDigite o total de acertos (green): ");
            scanf("%d", &green);
            resultado3 = (green*100)/entradas;
            red = entradas - green;

                printf("Com suas %d Entradas(Operacoes), voce teve a %d acertos(green) e %d red(s), e teve %.2f de sucesso.\n\n", entradas, green, red, resultado3);
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

        printf("\nPartidas Over 1.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media1, cont1, jogos);

            if ( media1 > 85){
                printf("\n# Altissima Prababilidade #\n");
                    }if ( media1 >= 75 && media1 < 85){
                        printf("\n# Alta Prababilidade #\n");
                            } if ( media1 >= 65 && media1 <75){
                                printf("\n# Moderada Prababilidade #\n");
                                    } if (media1 < 65){
                                        printf("\n# Baixa Probabilidade #\n");
                                        }


            printf("\nPartidas Over 2.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media2, cont2, jogos);
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


                printf("\nPartidas Over 3.5 tem porcentagem de %2.2f  de probabilidade de ocorrer, em %d partidas de um total de %d.\n", media3, cont3, jogos);

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
                            printf("Media de Gols = %1.1f\n", mediagols);
                            puts("--------------------------------");
                            puts("\n");


                            break;



        case 6:

            printf("fechando Sistema...\n"); /* não está fechando e saindo*/

        default:
            printf("\nErro. Opcao Invalida. Digite uma opcao do Menu abaixo:\n\n"); //digitando 4 está aparecendo esta messagem.
            break;
        }




    }while(opcao!=6);

    return 0;
}
