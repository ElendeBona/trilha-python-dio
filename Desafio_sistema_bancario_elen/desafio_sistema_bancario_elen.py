menu = """

[d] Depositar
[s] Sacar
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
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: ##verifica se é valor positivo
            saldo += valor ##contatena/soma ao valor do deposito ao saldo existente
            extrato += f"Depósito: R$ {valor:.2f}\n" #gera a visualização de extrato na formatação de duas casas decimais 

        else:
            print("Operação falhou! O valor informado é inválido.") #caso seja um valor negativo de deposito gera uma mensagem de falha e que o valor é invalido

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo #operação que gera caso exceda o saldo

        excedeu_limite = valor > limite #operação que gera caso exceda o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES #operação que verifica se excedeu o numero de saques diarios = 3 

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.") #mensagem que não deixa sacar

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.") #mensagem que não deixa sacar

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.") #mensagem que não deixa sacar

        elif valor > 0: #caso passe por todos os if/elifs anteriores, gera uma verificação aconteça
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
