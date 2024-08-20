                                                   #Calculadora Simples# 

def somar(a, b):
    #Retorna a soma de dois números.#
    return a + b

def subtrair(a, b):
    #Retorna a subtração de dois números.#
    return a - b

def multiplicar(a, b):
    #Retorna a multiplicação de dois números.#
    return a * b

def dividir(a, b):
    #Retorna a divisão de dois números.#
    if b == 0:
        return"Erro: Divisão por zero."
    return a / b

def menu():
        #Exibe o menu de opções ao usuário.#
    print("Escolha uma operação: ")
    print("1 .Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = int(input("Digite sua escolha: "))
        if escolha == 0:
            print("Saindo...")
            break  
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if escolha == 1:
            print(f"Resultado: {somar(a, b)}")
        elif escolha == 2:
            print(f"Resultado: {subtrair(a, b)}")
        elif escolha == 3:
            print(f"Resultado: {multiplicar(a, b)}")
        elif escolha == 4:
            print(f"Resultado: {dividir(a, b)}")
        else:
            print("Escolha inválida, tente novamente.")

if __name__== "__main__": 
    main()            
