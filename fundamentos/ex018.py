from math import cos, tan, sin, radians

angulo = int(input('Inform a angle: '))
angulo = radians(angulo)

print(f'Seno {sin(angulo):.3f}\n'
      f'Cosseno {cos(angulo):.3f}\n'
      f'Tangente {tan(angulo):.3f}')
