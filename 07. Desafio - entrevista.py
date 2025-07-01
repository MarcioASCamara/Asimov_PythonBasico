# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(nome + idade)
# - Dá oi para você
#print('Olá ' + nome + '!' )
print(f'Olá, {nome}!')
# - Conta quantas letras seu nome possui
#print ('Seu nome tem ' + str(len(nome)) + ' letras')
print (f'Seu nome tem {len(nome)} letras.')
# - Fala quantos anos você terá daqui a 5 anos
print (f"Em cinco anos você terá {int(idade) + 5 } anos")
