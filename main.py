#1. Verificação de Positivo, Negativo ou Zero
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#2. Verificação de Número Par/Ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#3. Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", num1 + num2)
elif operacao == "-":
    print("Resultado:", num1 - num2)
elif operacao == "*":
    print("Resultado:", num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: Divisão por zero.")
else:
    print("Operação inválida.")

#4. Maior de Três Números

#5. Classificação de Idade
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 19:
    print("Adolescente")
elif idade >= 20 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida.")


#6. Verificação de Triângulo
lado1 = int(input("Digite o comprimento do primeiro lado A: "))
lado2 = int(input("Digite o comprimento do segundo lado B: "))
lado3 = int(input("Digite o comprimento do terceiro lado C: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados não formam um triângulo.")

#7. Conversão de Notas
nota = float(input("Digite a nota (0 a 100): "))
if nota >= 90 and nota <= 100:
    print("Conceito: A")
elif nota >= 80 and nota < 90:
    print("Conceito: B")
elif nota >= 70 and nota < 80:
    print("Conceito: C")
elif nota >= 60 and nota < 70:
    print("Conceito: D")
elif nota >= 0 and nota < 60:
    print("Conceito: F")
else:
    print("Nota inválida.")

#8. Validação de Login
username = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if username == "admin" and senha == "12345":
    print("Acesso concedido")
else:
    print("Acesso negado")

#9. Calculadora de IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 39.9:
    print("Obeso")
else:
    print("Muito obeso")



#10. Verificação de Ano Bissexto
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")












