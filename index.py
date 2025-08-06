from datetime import datetime, time, timedelta

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = {}
numero_saques = 0
numero_depositos = 0
numero_transacao = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 10


while True:
    agora = datetime.now()
    amanha = (agora + timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0)
    diferenca = amanha - agora
    faltam_horas = diferenca.seconds//3600
    faltam_minutos = (diferenca.seconds%3600) // 60
    opcao = input(menu).upper()

    if opcao == "D":
        print("Opção escolhida - Depositar")

        if numero_transacao >= 10 :
            print(
f'''\nVocê excedeu o número de transações permitidas para hoje!
limite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos.''')
            continue

        deposito = input("insira o valor para depósito: ")

        if deposito != "":
            deposito = float(deposito)
            if deposito > 0:
                saldo += deposito
                numero_depositos += 1
                numero_transacao += 1
                extrato.update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"+ R$ {deposito:.2f}"})

                print(f"O novo saldo é de R${saldo:.2f}")
                print(f"Atualizado o Extrato, foram feitas {numero_transacao} transações.")

            else:
                print("Operação falhou! Insira um valor positivo")

        else:
                print("Operação falhou! Insira um valor")

    elif opcao =="S":

      
        if numero_transacao >= 10 :
                print(
        f'\nVocê excedeu o número de transações permitidas para hoje!\nlimite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos.')
                continue
        
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
                    numero_transacao += 1
                    saldo -= saque
                    print("Saque será realizado")
                    print(f"Saldo de R${saldo}")
                    print(f"Ainda possui {LIMITE_TRANSACAO - numero_transacao} transações.")
                    extrato.update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"- R$ {saque:.2f}"})

    elif opcao == "E":

        print("Opção escolhida - Extrato")
        print("\n=================== EXTRATO ===================")
        if not extrato:
            print("Não foram realaizadas movimentações.")  

        else: 
            for chave, valor in extrato.items():
                print(f"{chave}                  {valor}")
               

        print(f"\nSaldo de : R$ {saldo:.2f}")
        print("===============================================")
        print("Extrato fechado")

    elif opcao == "Q":

        print("Sistema fechado.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")