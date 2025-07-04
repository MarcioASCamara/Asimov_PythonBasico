# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

numeros = range(1,101)
soma = 0
for n in numeros:
   soma += n
print (soma)

media = soma/len(numeros)
print(media)

palavras = ['jabuticaba','chorar','laranja','machado','uva','tambor','pão','pedra']

for p in palavras:
    if len(p) > 5:
        print(p)

