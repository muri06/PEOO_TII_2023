'''1. Ler dois valores inteiros e imprimir o maior deles, ou a mensagem "Números iguais", se forem iguais.'''
print('Digite dois valores inteiros')
a = int(input())
b = int(input())
if a == b:
  print('Números iguais')
elif a > b:
  print(a)
else:
  print(b)
