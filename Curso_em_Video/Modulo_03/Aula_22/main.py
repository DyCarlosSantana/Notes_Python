# Importando os submódulos dos pacotes de utilidades
from utilidadesCeV.moeda import moeda
from utilidadesCeV.dado import dado

# Usando a função leiaDinheiro (Ex 112) criada para garantir dados limpos
num = dado.leiaDinheiro("Digite um preço: R$")

# Exibimos o resumo (Ex 110) configurado com 20% de aumento e 20% de redução
moeda.resumo(num, 20, 20)