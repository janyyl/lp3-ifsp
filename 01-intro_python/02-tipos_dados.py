# 1. Números 

# int
idade = 20

# float
altura = 1.6

# complex
# cálculos com números complexos

numero_complexo = 1 + 2j

# 2. Booleano
verdade = True
mentira = False

# 3. Sequências 
# str, list, tuple, set, dict

# str
# conjunto de caracteres 
nome = "João da Silva"
nome = "Maria da Silva"

# str de multiplas linhas
frase = '''
oookaj
olll
mooo
''''

# interpolação de str
nome = "Giovana"
idade = 78

mensagem = f"{nome} é uma pessoa legal! Ela tem {idade} anos"

# char 
# não existe
# usar str de tamanho 1 
letra = A

# Como acessar os caracteres de uma str?
nome = "Silvio Santos"
print(nome[2])

# Metodos de str
print(nome.upper())
print(nome.capitalize())
print(nome)


# list
# lista de valores
# permitir diferentes tipos de dados na mesma linha

habilidades = ["python" , "java", "javascript"]
print (habilidades[1]) # java

for habilidades in habilidades:
    print(habilidades)

# adiciona no final da linha
habilidades.append("html")

# adiciona em uma posiçao
habilidades.insert(1 , "css") 

# remover
habilidades.remover("css")

# tuple 
# lista de valores
# não pode ser alterada
# sim , não e talvez
opcoes = ("sim" , "nao" , "talvez")
raca_rpg = ("humano" , "elfo" , "orc")

def estatisticas_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/ len(notas)
    return maior, menor , media 

notas = [10.0 , 3.5 , 7.8]
estatistica = estatisticas_notas(notas)
print (estatistica)

# desempacotar uma tupla
maior, menor, media = estatisticas_notas(notas)
print(maior, menor, media)

#set 
# conjunto de valores
# não é indexado
# permite elemnetos duplicados 
habilidades = {"java" , "python"}
habilidades.add = ("javascript")
print(habilidades)

for habilidades in habilidades:
    print(habilidades)


# dict
# palavra -> definição
# chave -> valor
# key -> value

nome = "Silvio"
idade = 89
patrimônio = 2000000
altura - 1.7

pessoa = {

    "nome" = "Silvio",
    "idade" = 89,
    "patrimonio" = 2000000,
    "altura" = 1.7
}


print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["patromonio"])
print(pessoa["altura"])


# None
# Variaveis que serão inicializadas em tempo de execução
# Retorno de função
# Parametros de função
nulo = nome