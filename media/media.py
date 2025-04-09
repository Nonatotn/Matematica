def calcular_media(valores):
    return sum(valores) / len(valores)

def main():
    try:
        n = int(input("Quantos valores você deseja inserir? "))
        if n <= 0:
            print("O número de valores deve ser maior que zero.")
            return
        
        valores = [float(input(f"Digite o valor {i+1}: ")) for i in range(n)]
        print(f"A média dos valores é: {calcular_media(valores):.2f}")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números corretamente.")

if __name__ == "__main__":
    main()