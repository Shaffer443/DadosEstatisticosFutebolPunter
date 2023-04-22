# Aquisição de Dados e Valores de Parâmetros para Entradaas Esportivas (Futebol) via link de Web de Estatísticas.

**Bibliotecas e Frameworks**

- requests (pip install requests)
- beautifulsoup4 (pip install beautifulsoup4) 
- tabulate (pip install tabulate) (from tabulate import tabulate)
  documentação: https://pypi.org/project/tabulate/
- pyinstaller (pip install pyinstaller) - Criação de arquivos .exe

**pyinstaller**
Exemplo de criação: pyinstaller --onefile -w <nome do arquivo>

parâmetro "-w", caso precise de interação do usuário na aplicaçao. Caso não precise, pode-se usar sem:
Exemplo:
  pyinstaller --onefile <nome do arquivo>



- Site de referência para os dados: https://www.fctables.com

# problemas e linha de pensamento

** footystats_dados_live.py**

- Principal problema é que nem sempre se é carregada na hora da chamada todos os dados que o script pede.
    - Podemos selecionar apenas os que geralmente aparece
    - Organizar uam forma de selecionar
    - Puxar de outro site que tenha as informações mais constantes e frequentes
    - aparecer elementos dinâmicos que contém nos dados. observar a numeração da lista, pois se altera a ordem pelo tamanho