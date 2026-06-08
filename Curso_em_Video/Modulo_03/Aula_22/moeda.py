

# --- Exercício 107 ---
def metade(preco, format_preco=False):
    try:
        valor_metade = preco / 2
        if format_preco == True:
            return moeda(valor_metade)
        else:
            return valor_metade
    except:
        print("Erro (metade)... Tente novamente")
    return None


def dobro(preco, format_preco=False):
    try:
        valor_dobro = preco * 2
        if format_preco == True:
            return moeda(valor_dobro)
        else:
            return valor_dobro
    except:
        print("Erro (dobro)... Tente novamente")
    return None


def diminuir(preco, porcentagem, format_preco=False):
    try:
        cal_porcentagem = (preco * porcentagem) / 100
        valor_diminuir = preco - cal_porcentagem
        if format_preco == True:
            return moeda(valor_diminuir)
        else:
            return valor_diminuir
    except:
        print("Erro (diminuição)... Tente novamente")
    return None


def aumentar(preco, porcentagem, format_preco=False):
    try:
        cal_porcentagem = (preco * porcentagem) / 100
        valor_aumentar = preco + cal_porcentagem
        if format_preco == True:
            return moeda(valor_aumentar)
        else:
            return valor_aumentar
    except:
        print("Erro (aumento)... Tente novamente")
    return None

# --- Exercício 108 --- 
def moeda(preco): 
    try:
        format_preco = f"R${preco:.2f}".replace('.', ',')
    except:
        print("Erro (moeda)... Tente novamente")
    return format_preco

# --- Exercício 110 ---
def resumo(preco, porcentagem_aumenta=10, porcentagem_diminui=10):
    try:
        print("---" *10)
        print(f"{'RESUMO DO VALOR':^30}")
        print("---" *10)
        print(f"Preço analisado:     {moeda(preco)}")
        print(f"Dobro do preço:      {moeda(dobro(preco))}")
        print(f"Metade do preço:     {moeda(metade(preco))}")
        print(f"{porcentagem_aumenta}% de aumento:      {moeda(aumentar(preco, porcentagem_aumenta))}")
        print(f"{porcentagem_diminui}% de redução:      {moeda(diminuir(preco, porcentagem_diminui))}")
        print("---" *10)
    except:
        print("Erro (resumo)... Tente novamente")

