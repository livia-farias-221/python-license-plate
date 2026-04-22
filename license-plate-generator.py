# Gerando uma lista com todas as letras do alfabeto
import string
import random

alfabeto = list(string.ascii_uppercase)

 #Gerando uma lista com número de 1 a 9
numeros = list(range(10))

# Lista para armazenar placas geradas
placasGeradas = []

# String para armazenar a placa gerada em casa iteração
placaString = ""

# Estrutura de placa Mercosul é LLLNLNN, ou seja, três letras, um número, uma letra e dois números

while True:
    control = input('Deseja adicionar uma placa? (S/N) ').strip().upper() # Garantindo que não haverá espaços em branco e que a letra seja sempre maiúscula
    if control == 'N':
        break
    elif control == 'S' :
        # A cada iteração, é escolhido um item aleatorio da lista de números ou de letras e ele é adicionado na string de acordo com a estrtura do Mercosul
        placaString =  random.choice(alfabeto) + random.choice(alfabeto) + random.choice(alfabeto) + str(random.choice(numeros)) + random.choice(alfabeto) + str(random.choice(numeros)) + str(random.choice(numeros))
        print(placaString)
        if placaString not in placasGeradas: #Verifica se já existe uma placa idêntica
        # A string gerada é guardada dentro da lista de placas
            placasGeradas.append(placaString)        
            continue
        else:
            print('Placa já existe. Uma nova vai ser gerada')
    else:
        print('Opção inválida! Tente novamente')
        continue

print('Placas geradas:')      
for placa in placasGeradas:
    print('• ' + placa)




