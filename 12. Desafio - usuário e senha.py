# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.
#print(f"Digite seu usuario\nDigite sua senha")

usuario_padrao = "MarcioASCamara"
senha_padrao= "%X^017**"

usuario = input("Digite seu nome de usuario\nDigite aqui: ")
senha = input("Digite sua Senha:\nDigite aqui: ")
if usuario != usuario_padrao:
    print(f'O nome do usuario {usuario} nao foi encontrado')
if usuario == usuario_padrao and senha != senha_padrao:
    print(f'Ola {usuario} senha incorreta, observe se a tecla caps lock esta pressionada e tente novamente')
if usuario == usuario_padrao and senha == senha_padrao:
    print(f'Ola {usuario} voce foi corretamente autenticado')

