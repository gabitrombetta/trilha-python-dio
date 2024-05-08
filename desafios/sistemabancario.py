saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while (True):
    print(f'''
        MENU
        [d] Depósito
        [s] Saque
        [e] Extrato
        [q] Sair
        ''')
    option = input("Informe a opção desejada: ")

    if (option == 'd'.lower()):
        valor = float(input("Informe o valor do depósito: R$"))

        if (valor > 0):
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}'
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif (option == 's'.lower()):
        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = valor > LIMITE_SAQUES

        if (excedeu_saques):
            print("Operação falhou! Saldo insuficientee.")
        elif (excedeu_limite):
            print("Operação falhou! O valor do saque excede o limite.")
        elif (excedeu_saques):
            print("Operação falhou! Número máximo de saques excedido.")
        elif (valor > 0):
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}'
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido")
    elif (option == 'e'):
        print("===============EXTRATO===============")
        if(not saldo):
            print("Não foram realizadas movimentações")
        else:
             print(f"{extrato} \n")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=====================================")
    elif (option == 'q'.lower()):
        break
    else:
        print("Opção inválida, por favor tente novamente.")