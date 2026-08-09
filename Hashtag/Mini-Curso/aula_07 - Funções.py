
def se_inscreve_no_canal(): #Função Simplies / Função sem parametro
    print('Clique no batão abaixo de video escrito "Se Inscreva"')
    print('Dê um like no video')
se_inscreve_no_canal()

#Exemplos
#Para produtos de ATÈ 1000, pagam 10% de imposto
#Para produtos acima de 1000, pagam 15% de imposto

lista_precos = [1500, 1000, 800, 2000]
#Funções com Parâmetros e Retorno
def definir_taxa_imposto(preco): #criação de função apenas para calcular imposto
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    return taxa #para usar o valor de uma variavel fora da função, precisa usar o retorm, que sempre encerra a função

def calcular_imposto(lista_valores): 
    imposto_total = 0
    for preco in lista_valores:
        taxa = definir_taxa_imposto(preco)
        imposto = preco * taxa
        imposto_total += imposto

    return imposto_total

imposto_total1 = calcular_imposto(lista_precos)
print(imposto_total1)

#Segunda Lista
lista2_precos = [500, 400, 3200, 2600, 1000]
imposto_total2 = calcular_imposto(lista2_precos)
print(imposto_total2)


#Onde as variaveis vivem
variavel_global = "Eu sou global!"

def exemplo_escopo():
    variavel_local = "Eu sou local!"
    print(variavel_global)  # Acessa a variável global
    print(variavel_local)   # Acessa a variável local

exemplo_escopo()
print(variavel_global)  # Funciona!
# print(variavel_local)  # ERRO! Variável local não existe fora da função.


