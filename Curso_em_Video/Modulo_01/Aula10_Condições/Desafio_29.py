velocidade = int(input('Velocidade do automovel: '))
limite = 80
multa = 7.00
ultrapassou = (velocidade - limite)
total = ultrapassou * multa

if velocidade >= limite:
    print('Velocidade ultrapassou o limite estabelecido de {}Km/h.'.format(limite))
    print('Multa equivalente a R${}, por Km ultrapassado.'.format(multa))
    print('Km ultrapassados: {}Km'.format(ultrapassou))
    print('Valor total: R${}'.format(total))