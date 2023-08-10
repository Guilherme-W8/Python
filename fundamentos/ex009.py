inteiro = int(input('Informe um numero: '))

print('-' * 18)

for i in range(10):
    i += 1
    print(f'| {inteiro:>3} x {i:<2} = {(inteiro * i):<3} |')

print('-' * 18)
