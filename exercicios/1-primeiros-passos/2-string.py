resumo = """Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."""
# Definir a variável
resumo = """Paloma é uma mulher de 46 anos que deseja mudar de profissão, 
por isso está estudando 'python'."""
print(resumo)

# Imprima na tela apenas a segunda letra da variável
palavra = "Paloma"        # ❗ precisa estar entre aspas, senão o Python acha que é uma variável não definida
print(palavra[1])         # usa print() para mostrar o resultado

# Imprima na tela a idade de Paloma (resposta esperada: "46")
idade = 46
print(idade)              # aqui estamos a imprimir apenas o número 46

# Imprima na tela o trecho final da variável
print(resumo[31:])        # começa no índice 31 e vai até o fim

# Converta todas as letras para minúsculo e imprima na tela
print(resumo.lower())     # usa o método .lower() e print()

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print(resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
print(f"Paloma tem {idade} anos e está estudando Python.")
