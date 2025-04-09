import math

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return math.pi * raio ** 2

print("Escolha a forma geométrica:")
print("1 - Retângulo")
print("2 - Triângulo")
print("3 - Círculo")
opcao = int(input("Digite o número da opção: "))

if opcao == 1:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print(f"A área do retângulo é: {area_retangulo(base, altura)}")
elif opcao == 2:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    print(f"A área do triângulo é: {area_triangulo(base, altura)}")
elif opcao == 3:
    raio = float(input("Digite o raio do círculo: "))
    print(f"A área do círculo é: {area_circulo(raio)}")
else:
    print("Opção inválida!")
