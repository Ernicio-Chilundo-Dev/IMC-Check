def calcular_imc():
    print("Calculadora de IMC")
    print("=" * 30)
    
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Por favor, insira valores válidos para peso e altura.")
            return
        
        imc = peso / (altura ** 2)
        print(f"\nSeu IMC é: {imc:.2f}")
        
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            print("Classificação: Peso normal")
        elif 25 <= imc < 29.9:
            print("Classificação: Sobrepeso")
        elif 30 <= imc < 34.9:
            print("Classificação: Obesidade grau I")
        elif 35 <= imc < 39.9:
            print("Classificação: Obesidade grau II")
        else:
            print("Classificação: Obesidade grau III")
    except ValueError:
        print("Erro: Por favor, insira números válidos.")

# Executa a calculadora
calcular_imc()