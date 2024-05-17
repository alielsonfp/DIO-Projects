import textwrap
 
    

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu)) 


def depositar(saldo, valor, extrato,/):   
     if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("=== Deposito realizado com sucesso ===")
     else:
        print("Insira um valor de deposito valido")
    
     return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques =  numero_saques >= limite_saques

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
        print("=== Saque realizado com sucesso ===")
        print(numero_saques)
    else:
        ("Insira um valor de saque valido")

    return saldo,extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    else:
        nome = input("Insira seu nome: ")
        data_nascimento = input("Insira sua data de nascimento: ")
        endereco = input("Insira seu endereço: ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})

        print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []   

    while True:
        opcao = menu()


        if opcao == "d":
            valor = float(input("Insira o valor desejado depositar: "))

            saldo,extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":
            valor = float(input("Insira o valor que deseja sacar: "))

            saldo, extrato,numero_saques = sacar(
                saldo= saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, selecione uma opção valida")

main()
