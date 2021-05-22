Resp = 's'
while Resp == 's':
    N1 = int(input("Insira o primeiro número: "))
    N2 = int(input("Insira o segundo número: "))

    Escolha = int(input('''\nEscolha uma opção:\n
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO\n
Resposta: '''))

    if Escolha == 1:
        Soma = N1 + N2
        print(f"\n{N1} + {N2} = {Soma}\n")
    elif Escolha == 2:
        Sub = N1 - N2
        print(f"\n{N1} - {N2} = {Sub}\n")
    elif Escolha == 3:
        Multi = N1 * N2
        print(f"\n{N1} x {N2} = {Multi}\n")
    elif Escolha == 4:
        Div = N1 / N2
        print(f"\n{N1} / {N2} = {Div:1f}\n")
    Resp = str(input("Deseja fazer um novo calculo? [S/N] ")).lower()
    if Resp == 'n':
        print("Encerrando...")