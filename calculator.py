def calcular(operacao, *numeros):
    if operacao == "soma":
        return sum(numeros)
    
    elif operacao == "subtracao":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        return resultado

    elif operacao == "multiplicacao":
        resultado = 1
        for n in numeros:
            resultado *= n
        return resultado

    elif operacao == "divisao":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                return "Erro: Divisão por zero"
            resultado /= n
        return resultado

    else:
        return "Operação inválida!"


while True:
    print("\n=== CALCULADORA PYTHON ===")
    print("Operações disponíveis: soma, subtracao, multiplicacao, divisao")
    print("Digite 'sair' para encerrar.\n")
    
    operacao = input("Digite a operação: ").strip().lower()

    if operacao == "sair":
        print("Encerrando calculadora...")
        break

    entrada = input("Digite os números separados por espaço: ").strip()

    try:
        numeros = tuple(map(float, entrada.split()))
        if len(numeros) < 2:
            print("Digite pelo menos dois números!")
            continue
        resultado = calcular(operacao, *numeros)
        print(f"Resultado da {operacao}: {resultado}")
    except ValueError:
        print("Entrada inválida! Use apenas números separados por espaço.")
