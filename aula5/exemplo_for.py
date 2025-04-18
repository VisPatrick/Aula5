for n in range(5):
   print('Olá Mundo')

for n in range(5):
   print(n)

inicio = int(input('Informe o início: '))
fim = int(input('Informe o final: '))

for i in range (inicio, fim):
    print(i)

for i in range (5, 50, 5):
    print(i)

for n in range (3):
    print(f'Pessoa {n+1}')
    nome = input('Informe o nome da pessoa: ')
    print(f'O nome da pessoa é: {nome}')

soma = 0.0
for num in range (5):
    numero =  float(input('Informe o número: '))
    # soma = soma + numero
    soma += numero 

print(f'O total é: {soma}')