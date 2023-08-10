quantidadeKmRodado = int(input('Informe os kms rodados: '))
quantidadeDiasAluguel = int(input('Informe a quantidade de dias alugados: '))

custoAluguel = quantidadeDiasAluguel * 60
custoKmRodado = quantidadeKmRodado * 0.15

custoTotal = custoAluguel + custoKmRodado
print(f'Custo total a pagar = R${custoTotal:.2f}')
