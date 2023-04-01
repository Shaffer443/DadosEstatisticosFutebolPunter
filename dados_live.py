import requests
from bs4 import BeautifulSoup
import math
import funcoes


# site : sofa score

# link's dos dados qeu deseja analisar.
insert_link = input('Insira o link dos dados sobre o time da CASA do site  www.fctables.com:: ')
link_live = f"{insert_link}"
headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"}
# passando o que queremos do site:
site = requests.get(link_live, headers=headers)
# recebendo o objeto do soup
# parser - informa o tipo de dados que irá receber
soup = BeautifulSoup(site.content, 'html.parser')

#expectativa de gol: <span class="sc-bqWxrE sc-d0fb9fae-0 fHlyYu jtdnHK">0.17</span>
#posse de bola: <span class="sc-bqWxrE sc-d0fb9fae-0 fHlyYu jtdnHK">69%</span>

#time <text class="timer" font-weight="700" font-size="14px" opacity="1" x="151.25555555555556" text-anchor="middle" style="fill: rgb(231, 59, 59);" y="-10">31:38</text>

#graficos de intensidade: <svg class="sc-5a3daee1-1 iTErcE"><defs><clipPath id="round-corner"><rect x="0" y="0" width="424" height="80" rx="4" ry="4"></rect></clipPath></defs><g class="background-group" clip-path="url(#round-corner)"><rect width="150.75555555555556" x="0" y="0" height="80" fill="#1c2632"></rect><rect width="150.75555555555556" x="0" y="0" height="40" fill="rgba(85, 189, 95, 0.25)"></rect><rect width="150.75555555555556" x="0" y="26.666666666666668" height="13.333333333333334" fill="rgba(85, 189, 95, 0.25)"></rect><rect width="150.75555555555556" x="0" y="40" height="40" fill="rgba(75, 157, 239, 0.25)"></rect><rect width="150.75555555555556" x="0" y="40" height="13.333333333333334" fill="rgba(75, 157, 239, 0.25)"></rect></g><g class="bars-group"><rect x="1" y="39.6" height="0.4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="5.711111111111111" y="36" height="4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="10.422222222222222" y="30.799999999999997" height="9.200000000000001" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="15.133333333333333" y="32.8" height="7.199999999999999" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="19.844444444444445" y="34.4" height="5.6000000000000005" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="24.555555555555557" y="35.2" height="4.8" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="29.266666666666666" y="36" height="4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="33.97777777777778" y="36.4" height="3.5999999999999996" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="38.68888888888889" y="36.4" height="3.5999999999999996" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="43.4" y="36.4" height="3.5999999999999996" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="48.111111111111114" y="19.2" height="20.8" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="52.82222222222222" y="25.6" height="14.399999999999999" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="57.53333333333333" y="27.2" height="12.8" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="62.24444444444445" y="33.6" height="6.4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="66.95555555555556" y="28" height="12" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="71.66666666666667" y="36" height="4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="76.37777777777778" y="36.8" height="3.2" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="81.08888888888889" y="37.2" height="2.8000000000000003" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="85.8" y="37.2" height="2.8000000000000003" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="90.51111111111112" y="37.2" height="2.8000000000000003" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="95.22222222222223" y="37.2" height="2.8000000000000003" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="99.93333333333334" y="32.8" height="7.199999999999999" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="104.64444444444445" y="34.8" height="5.2" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="109.35555555555555" y="36" height="4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="114.06666666666666" y="36.8" height="3.2" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="118.77777777777779" y="40" height="9.6" width="3.7111111111111112" fill="#4b9def" stroke-width="1"></rect><rect x="123.4888888888889" y="40" height="0.8" width="3.7111111111111112" fill="#4b9def" stroke-width="1"></rect><rect x="128.2" y="37.6" height="2.4" width="3.7111111111111112" fill="rgb(85, 189, 95)" stroke-width="1"></rect><rect x="132.91111111111113" y="9.2" height="30.8" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="137.62222222222223" y="10" height="30" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="142.33333333333334" y="28" height="12" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect><rect x="147.04444444444445" y="36" height="4" width="3.7111111111111112" fill="#55bd5f" stroke-width="1"></rect></g><g class="lines-group"><line x1="151.25555555555556" y1="0" x2="151.25555555555556" y2="80" stroke-width="1" stroke="rgb(231, 59, 59)" clip-path=""></line><line x1="0" y1="40" x2="424" y2="40" stroke-width="1" stroke="rgba(255, 255, 255, 0.08)" clip-path="url(#round-corner)"></line><line x1="212" y1="0" x2="212" y2="80" stroke-width="1" stroke="rgb(28, 38, 50)" clip-path="url(#round-corner)"></line><circle cy="0" r="3" cx="151.25555555555556" stroke="#e73b3b" stroke-width="2" fill="#1c2632" class="live"></circle><circle cy="78" r="3" cx="0" stroke="#55bd5f" stroke-width="2" fill="#1c2632" class="start"></circle></g><g class="time-group"><text class="timer" font-weight="700" font-size="14px" opacity="1" x="151.25555555555556" text-anchor="middle" style="fill: rgb(231, 59, 59);" y="-10">32:11</text><g class="legend-group"><text font="&quot;Roboto&quot;, sans-serif" font-weight="500" font-size="12px" x="0" y="96" style="fill: rgb(85, 189, 95);">14:00</text><text font-family="&quot;Roboto&quot;, sans-serif" font-weight="500" font-size="12px" x="212" text-anchor="middle" y="96" style="fill: rgba(255, 255, 255, 0.4);">HT</text><text font-size="12px" font-family="&quot;Roboto&quot;, sans-serif" font-weight="500" x="424" text-anchor="end" y="96" style="fill: rgba(255, 255, 255, 0.4);">FT</text></g></g><g class="inciden

# /html/body/div[1]/div/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/a[1]/div/span
# <span color="sofaSingles.value" class="sc-bqWxrE Zxkvo">4.00</span>
# <span class="sc-bqWxrE jcJzAv" color="primary.default">Copa do Nordeste</span>
tempo_de_jogo=soup.find_all("strong")[2].get_text()

# CASA:
gol_time_casa = soup.find_all("span","goal_p")[6].get_text()
#posse_timedacasa = soup.find_all("li","line-top")
chute_time_casa = soup.find_all("span","goal_p")[0].get_text()
chute_nogol_time_casa = soup.find_all("span","goal_p")[1].get_text()

# Visitante:

gol_time_visitante=soup.find_all("strong")[4].get_text()
chute_time_visitante = soup.find_all("span","goal_t")[0].get_text()
chute_nogol_time_visitante = soup.find_all("span","goal_t")[1].get_text()

print(f"Tempo de jogo: {tempo_de_jogo}")

print(f"Gol's do time da Casa: {gol_time_casa}")
#print(posse_timedacasa)
print(f"Chutes do time da casa: {chute_time_casa}")
print(f"Chutes no GOL do time da casa: {chute_nogol_time_casa}")

print(f"\nGol's do time da Visitante: {gol_time_visitante}")
print(f"Chutes do time da Visitante: {chute_time_visitante}")
print(f"Chutes no GOL do time da Visitante: {chute_nogol_time_visitante}")



