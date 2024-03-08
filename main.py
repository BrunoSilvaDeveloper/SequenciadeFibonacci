def sequencia_fibonacci(n):
    sequenciaFib = [0, 1]
    while sequenciaFib[-1] + sequenciaFib[-2] <= n:
        sequenciaFib.append(sequenciaFib[-1] + sequenciaFib[-2])
    return sequenciaFib

def verificar_numero(num):
    sequenciaFib = sequencia_fibonacci(num)
    if num in sequenciaFib:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        num = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
        if num < 0:
            print("Por favor, digite um número positivo.")
        else:
            if verificar_numero(num):
                print(f"\nO número {num} faz parte da sequência de Fibonacci.")
            else:
                print(f"\nO número {num} não faz parte da sequência de Fibonacci.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

    while True:
        escolha = input('\nVocê deseja ver a sequência até este número? \nDigite 1 para Sim \nDigite 2 para não \n: ')

        if escolha == '1':
            print(f'\nA sequência de fibonacci até o número {num} é {sequencia_fibonacci(num)}')
            break
        elif escolha == '2':
            print('\nPrograma finalizado!')
            break
        else:
            print('\nDigite um número inteiro!')