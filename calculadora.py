continuar = str(input('Deseja fazer uma operação (S/N): ')).strip().upper()

while continuar == 'S':
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    operacao = int(input('Escolha sua operação\n1 Para Adição\n2 Para Subtração\n3 Para Multiplicação\n4 Para Divisão\n'))

    if operacao == 1:
        resultado = num1 + num2
        print('O resultado da soma dos números {} e {} é {}'.format(num1, num2, resultado))
    elif operacao == 2:
        resultado = num1 - num2
        print('O resultado da subtração dos números {} e {} é {}'.format(num1, num2, resultado))
    elif operacao == 3:
        resultado = num1 * num2
        print('O resultado da multiplicação dos números {} e {} é {}'.format(num1, num2, resultado))
    elif operacao == 4:
        if num2 == 0:
            print('Erro: divisão por zero não é permitida.')
        else:
            resultado = num1 / num2
            print('O resultado da divisão dos números {} e {} é {}'.format(num1, num2, resultado))
    else:
        print('Operação invalida!')

    continuar = str(input('Deseja fazer outra operação (S/N): ')).strip().upper()

print('Fim do programa!')