import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Raízes: {x1} e {x2}"

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(bhaskara(a, b, c))
