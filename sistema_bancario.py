
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Opção escolhida - Depositar")

        deposito = input("insira o valor para depósito: ")

        if deposito != "":
            deposito = float(deposito)

            if deposito > 0:
                saldo += deposito
                extrato.append(f"+ R$ {deposito:.2f}")
                print(f"O novo saldo é de R${saldo:.2f}")
                print("Atualizado o Extrato")

            else:
                print("Operação falhou! Insira um valor positivo")

        else:
                print("Operação falhou! Insira um valor")

    elif opcao =="s":

        if numero_saques >= LIMITE_SAQUES :
             print("Operação falhou! Você alcançou o limite diario, novo saque apenas amanhã")

        else: 
            print("Opção escolhida - Sacar")
            print(f"Seu saldo é de R$ {saldo}")
            saque = input("Insira o valor para saque: ")

            if saque == "" :
                print("Operação falhou! Insira um valor")              

            else:
                saque = float(saque)

                if saque < 0:
                    print("Operação falhou! Insira um valor positivo")

                elif saque > saldo:
                    print("Operação falhou! Não é possivel sacar o dinheiro por falta de saldo")

                elif saque > 500.00:
                    print("Operação falhou! Valor acima do limite por saque, escolha um valor abaixo de R$ 500,00")

                else:
                    numero_saques += 1
                    saldo -= saque
                    print("Saque será realizado")
                    print(f"Saldo de R${saldo}")
                    print(f"Ainda possui {LIMITE_SAQUES - numero_saques} saques.")
                    extrato.append(f"- R$ {saque:.2f}")


    elif opcao == "e":

        print("Opção escolhida - Extrato")
        print("\n=================== EXTRATO ===================")
        if not extrato:
            print("Não foram realaizadas movimentações.")  

        else: 
            for i in extrato:
                print(i)

        print(f"\nSaldo de : R$ {saldo:.2f}")
        print("===============================================")
        print("Extrato fechado")


    elif opcao == "q":

        print("Sistema fechado.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")