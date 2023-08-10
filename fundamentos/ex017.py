from math import hypot
catetoOposto = float(input('Cateto Oposto: '))
catetoAdjacente = float(input('Cateto Adjacente: '))

# hipotenusa = sqrt(catetoOposto ** 2 + catetoAdjacente ** 2)

hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'Comprimento da hipotenusa {hipotenusa:.2f}')
