carteira = float(input('Informe o valor da sua carteira: '))
novaCarteira = (carteira / 3.27)
print('Desconto de 1,5% do cambio...')
print(f'R${carteira} = US${novaCarteira - (novaCarteira * 0.015):.2f}')
