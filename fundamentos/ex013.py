salarioAtual = float(input('Informe o salario atual: '))
novoSalario = salarioAtual + (salarioAtual * 0.15)
diference = novoSalario - salarioAtual
print(f'Update salario R${salarioAtual} >> R${novoSalario:.2f}\nDiference R${diference:.3f}')
