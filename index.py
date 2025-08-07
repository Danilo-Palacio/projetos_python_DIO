from datetime import datetime, time, timedelta

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

def funcao_deposito(dados, agora,/): 
    print("===============================================")
    print("\nOpção escolhida - Depositar")
    deposito = input("insira o valor para depósito: ")
    
    if deposito != "":
        deposito = float(deposito)
        if deposito > 0:
            dados["saldo"] += deposito
            dados["numero_depositos"] += 1
            dados["numero_transacao"] += 1
            dados["extrato"].update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"+ R$ {deposito:.2f}"})
            print("\n===============================================\n")
            print(f"O novo saldo é de R${dados["saldo"]:.2f}")
            print(f"Atualizado o Extrato, foram feitas {dados["numero_transacao"]} transações.")
            print("\n===============================================")

        else:
            print("Operação falhou! Insira um valor positivo")

    else:
            print("Operação falhou! Insira um valor")

def funcao_saque(*, dados, agora):
    print("\n===============================================\n")
    print("Opção escolhida - Sacar")
    print(f"Seu saldo é de R$ {dados["saldo"]}\n")

    saque = input("Insira o valor para saque: ")

    if saque == "" :
        print("Operação falhou! Insira um valor")              

    else:
        saque = float(saque)

        if saque < 0:
            print("Operação falhou! Insira um valor positivo")

        elif saque > dados["saldo"]:
            print("Operação falhou! Não é possivel sacar o dinheiro por falta de saldo")

        elif saque > 500.00:
            print("Operação falhou! Valor acima do limite por saque, escolha um valor abaixo de R$ 500,00")

        else:
            dados["numero_saques"] += 1
            dados["numero_transacao"] += 1
            dados["saldo"] -= saque
            print("\n===============================================\n")
            print("Saque será realizado")
            print(f"Saldo de R${dados["saldo"]}")
            print(f"Ainda possui {LIMITE_TRANSACAO - dados["numero_transacao"]} transações.")
            dados["extrato"].update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"- R$ {saque:.2f}"})
            print("\n===============================================\n")

def funcao_extrato(dados):
    
    print("Opção escolhida - Extrato")
    print("\n=================== EXTRATO ===================")
    if not dados["extrato"]:
        print("Não foram realaizadas movimentações.")  

    else: 
        for chave, valor in dados["extrato"].items():
            print(f"{chave}                  {valor}")
            

    print(f"\nSaldo de : R$ {dados["saldo"]:.2f}")
    print("===============================================")
    print("Extrato fechado")

dados = {
    "saldo" : 0,
    "limite" : 500,
    "extrato" : {},
    "numero_saques" : 0,
    "numero_depositos" : 0,
    "numero_transacao" : 0,
}


LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 10

while True:
    agora = datetime.now()
    amanha = (agora + timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0)
    diferenca = amanha - agora
    faltam_horas = diferenca.seconds//3600
    faltam_minutos = (diferenca.seconds%3600) // 60
    opcao = input(menu).upper()

    texto_excedeu_transacoes = f"""

\nVocê excedeu o número de transações permitidas para hoje!
limite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos.

"""

    if opcao == "D":
        
        if dados["numero_transacao"] >= 10 :
            print(texto_excedeu_transacoes)
            continue

        funcao_deposito(dados, agora)

    elif opcao =="S":

        if dados["numero_transacao"] >= 10 :
                print(
        f'\nVocê excedeu o número de transações permitidas para hoje!\nlimite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos.')
                continue
        
        if dados["numero_saques"] >= LIMITE_SAQUES :
             print("Operação falhou! Você alcançou o limite diario, novo saque apenas amanhã")

        else: 
            funcao_saque(dados = dados, agora = agora)

    elif opcao == "E":
        funcao_extrato(dados)

    elif opcao == "Q":

        print("Sistema fechado.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")