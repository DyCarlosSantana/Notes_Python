'''
    74 - Crie uma tupla preenchida com os vinte primeiros colocados da tabela do comapeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
        a) Apenas os 5 primeiros colocados;
        b) Os últimos 4 colocados da tabela;
        c) Uma lista com os times em ordem alfabetica;
        d) Em que posição na tabela o time da Chapecoense.
'''
colocados_brasileirao_2025 = (
    "Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Fluminense",
    "Botafogo", "Bahia", "São Paulo", "Grêmio", "Red Bull Bragantino", "Atlético Mineiro", "Santos", "Corinthians", "Vasco da Gama", "Vitória", "Internacional", "Ceará", "Fortaleza", "Juventude", "Sport")

print(f'Os vinte colocados do brasileirão 2025: {colocados_brasileirao_2025}')
print('--------------------------------------------------------------------')
print(f'Os primeiros cinco colocados: {colocados_brasileirao_2025[0:5]}')
print('--------------------------------------------------------------------')
print(f'Os útimos 4 colocados: {colocados_brasileirao_2025[-4:]}') #motre do -4(16) para frente (até o ultimmo)
print('--------------------------------------------------------------------')
print(f'Lista dos times em ordem alfabetica: {sorted(colocados_brasileirao_2025)}')
print('--------------------------------------------------------------------')
try:
    print(f'Posição na tabela o time Chapecoense: {colocados_brasileirao_2025.index("Chapecoense")+1}°') # +1 para se equivaler a posição na tupla
except:
    if "Chaepcoense" not in colocados_brasileirao_2025:
        print('A posição não pode ser indentificada pois o time "Chapecoense" não esta no top 20 colocados')
