#Exercícios

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 1 - print

#print simples
print("Hello World")

#print com variáveis
a = 10

print(f"O número é {a}")
print("O número é %a" %a)
print("O número é {}" .format(a))
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 2 - Tipos de variáveis

#str

a = str(input("Digite uma frase: "))
#ou
a = input("Digite uma frase: ")

print(a)

#-----------------------------------------------------------

#int

b = int(input("Digite um número inteiro: "))

print(b)

#float

c = float(input("Digite um número decimal: "))

print(c)

#bool

d = bool(True)
#ou
d = bool(False)

print(bool)

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 3 - Expressões Aritméticas

#adição
x = 1
y = 2
print(x + y)

#subtração
x = 5
y = 3
print(x - y)

#multiplicação
x = 10
y = 3
print(x * y)

#divisão
x = 25
y = 5
print(x / y)

#divisão inteira
x = 32
y = 3
print(x // y)

#resto(módulo)
x = 10
y = 3
print(x % y)

#menos unário
x = 1
print(-x)

#potenciação
x = 2
y = 3
print(x ** y)

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 4 - Estruturas Condicionais

'''
Operadores de comparação

== (igual)

!= (diferente)

> (maior)

< (menor)

>= (maior ou igual)

<= (menor ou igual)
'''

#if
n = int(input("Digite um número: "))
if n % 2 == 0:
    print(f"O número {n} é par")

#if, else
n = int(input("Digite um número: "))
if n % 2 == 0:
    print(f"O número {n} é par")
else:
    print(f"O número {n} é ímpar")

#if, elif, else
n = int(input("Digite um número: "))
if n < 11:
    print(f"{n} é menor que 10")
elif n < 101:
    print(f"{n} é maior que 10 e menor que 100")
else:
    print(f"{n} é maior que 100")

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

# 5 - Estruturas Repetição

#while
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
while x <= y:
    print(x)
    x = x + 1 # ou x += 1

#for
for x in range(0, 11, 2):
    print(x)


