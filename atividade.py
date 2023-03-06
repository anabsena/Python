n = input("nome: ")
sn = input("sobrenome: ")
id =int(input('idade: '))
peso=float(input("peso: "))
altura=float(input("altura: "))
if id>=18:
  print(f' {id}anos, maior de idade...')
else:
    print(f'{id}anos, menor de idade...')
print(f'NOME: {n} \n SOBRENOME: {sn} \n IDADE: {id} \n PESO: {peso} \n ALTURA: {altura} cm')
