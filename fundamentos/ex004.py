X = input('Digite qualquer coisa: ')
print(f'Seu tipo primitivo: {type(X)}\nAlguns detalhes sobre o tipo...')

print(f'AlphaNumero? {X.isalnum()}\n'
      f'Numeric? {X.isnumeric()}\n'
      f'Alphabetic? {X.isalpha()}')
