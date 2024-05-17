menu = """"

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)


    if opcao == "d":
        valor = float(input("Insira o valor desejado depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Insira um valor de deposito valido")


    elif opcao == "s":
        valor = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques =  numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("O valor de saque excede o limite")

        elif excedeu_saques:
            print("Você excedeu seu limite de saques")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R${valor:.2f}\n"
        else:
            ("Insira um valor de saque valido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, selecione uma opção valida")
