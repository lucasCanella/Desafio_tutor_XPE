def NumPrimo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        return print(num, "é um número primo")
    return print(num, "não é um número primo")

while True:
    try:
        Entrada = int(input("Digite um número para saber se é um número primo "))
        NumPrimo(Entrada)
        reset = int(input("Deseja inserir outro número? [ 1 ] Sim [ 2 ] Digite outro número "))
        if reset != 1:
            break
    except:
        print("valor inválido")
