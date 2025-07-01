# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 7
descobriu = False

if not descobriu:
    numero_escolhido = int(input('Escolha um numero entre 1 e 10:\nDigite aqui: '))
    if  numero_escolhido < numero_secreto:
        print('Voce ainda tem duas tentativas. Tente um numero maior do que o escolhido')
    elif numero_escolhido > numero_secreto:
        print('Voce ainda tem uma tentativa. Tente um numero menor do que o escolhido')
    else:
        print('Descobriu')
        descobriu =True

if not descobriu:
    numero_escolhido = int(input('Escolha um numero entre 1 e 10:\nDigite aqui: '))
    if  numero_escolhido < numero_secreto:
        print('Voce ainda tem uma tentativa. Tente um numero maior do que o escolhido')
    elif numero_escolhido > numero_secreto:
        print('Voce ainda tem uma tentativa. Tente um numero menor do que o escolhido')
    else:
        print('Descobriu')
        descobriu =True

if not descobriu:
    numero_escolhido = int(input('Escolha um numero entre 1 e 10:\nDigite aqui: '))
    if  numero_escolhido < numero_secreto:
        print('O numero digitado era maior do que o escolhido. Suas tentativas acabaram')
    elif numero_escolhido > numero_secreto:
        print('O numero digitado era menor do que o escolhido. Suas tentativas acabaram')
    else:
        print('Descobriu')
        descobriu =True

if descobriu:
    print('parabens vc acertou')
else:
    print(f'Que pena, voce errou! O numero secreto era {numero_secreto}')
