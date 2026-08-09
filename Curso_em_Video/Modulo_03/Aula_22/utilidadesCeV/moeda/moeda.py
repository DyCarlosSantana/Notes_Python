# Módulo moeda.py (Dentro de utilidadesCeV/moeda/)

def moeda(preco=0):
    """
    Formata um valor numérico para o formato de moeda monetária (R$).
    """
    try:
        return f"R${preco:.2f}".replace('.', ',')
    except (TypeError, ValueError):
        return "R$0,00"


def metade(preco=0, format_preco=False):
    """
    Calcula a metade do preço, com opção de formatação monetária.
    """
    res = preco / 2
    return moeda(res) if format_preco else res


def dobro(preco=0, format_preco=False):
    """
    Calcula o dobro do preço, com opção de formatação monetária.
    """
    res = preco * 2
    return moeda(res) if format_preco else res


def diminuir(preco=0, porcentagem=10, format_preco=False):
    """
    Diminui uma porcentagem do preço, com opção de formatação monetária.
    """
    res = preco - (preco * porcentagem / 100)
    return moeda(res) if format_preco else res


def aumentar(preco=0, porcentagem=10, format_preco=False):
    """
    Aumenta uma porcentagem do preço, com opção de formatação monetária.
    """
    res = preco + (preco * porcentagem / 100)
    return moeda(res) if format_preco else res


def resumo(preco=0, porcentagem_aumenta=10, porcentagem_diminui=10):
    """
    Exibe um painel completo com análises sobre o preço passado.
    """
    print("-" * 35)
    print(f"{'RESUMO DO VALOR':^35}")
    print("-" * 35)
    print(f"Preço analisado:    \t{moeda(preco)}")
    print(f"Dobro do preço:     \t{dobro(preco, True)}")
    print(f"Metade do preço:    \t{metade(preco, True)}")
    print(f"{porcentagem_aumenta}% de aumento: \t{aumentar(preco, porcentagem_aumenta, True)}")
    print(f"{porcentagem_diminui}% de redução: \t{diminuir(preco, porcentagem_diminui, True)}")
    print("-" * 35)