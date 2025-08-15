from datetime import datetime, time, timedelta

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuario
[n] Nova Conta Corrente
[p] Pesquisa de usuário
[q] Sair


=> """


def teste_dados_iguais(texto_dado):
    opcao = -1
    while opcao != 0 :
        
        teste = 1
        solicitacao_do_dado = input(texto_dado)

        if solicitacao_do_dado.isdigit() == True:
          
            for usuario in usuarios:
                if usuarios[usuario]["CPF"] == int(solicitacao_do_dado):
                    teste = 0

            if teste == 0 :
                print(f'Opa! Esse CPF ({solicitacao_do_dado}) já está na nossa base.\nSe ele for seu, é só recuperar sua conta.\nQuer continuar? Basta informar outro CPF.')
                opcao = -1

            elif teste != 0 :
                opcao = 0
                return solicitacao_do_dado

        else:
            print("Não é digito")
            teste = False
            return teste

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

def funcao_criar_usuario():
        
        novo_usuario = len(usuarios) + 1
        print(f"Criando o usuario {novo_usuario:04d}")
        
        texto_cpf = "Digite seu CPF (apenas números, sem pontos ou traços): "
        cpf_testado = teste_dados_iguais(texto_cpf)
        nome = input("Digite seu nome completo: ")
        data_de_nascimento = input("Digite sua data de nascimento: ")
        
        print("\nVamos cadastrar seu endereço!\n")

        endereco_rua = input("Digite a rua: ")
        endereco_numero = input("Digite o numero: ")
        endereco_bairro = input("Digite o bairro: ")
        endereco_cidade = input("Digite a cidade: ")
        endereco_estado = input("Digite a sigla do estado: ")

        print(f"""
Olá {nome}!, vamos confirmar os dados, ok?
Data de Nascimento: {data_de_nascimento}
CPF: {cpf_testado}
Endereço: {endereco_rua}, {endereco_numero} - {endereco_bairro} - {endereco_cidade}/{endereco_estado}.
              """)
        
        confirmacao = input('Você confirma essas informações? \ndigite [s] ou [n]: ').upper()
        if confirmacao == "S" :
            endereco_formatado = f"{endereco_rua}, {endereco_numero} - {endereco_bairro} - {endereco_cidade}/{endereco_estado}"
            usuarios.update({novo_usuario: {
                "Nome":nome,
                "Data de Nascimento": data_de_nascimento,
                "CPF": cpf_testado,
                "Endereço Formatado" : endereco_formatado,
                "Endereço" : {
                    "Logradouro": endereco_rua,
                    "Numero" : endereco_numero,
                    "Bairro" : endereco_bairro,
                    "Cidade" : endereco_cidade,
                    "Sigla" : endereco_estado},
                "Conta Corrente" : None
                    }})
            print("Parabens! Você acaba de cadastrar o usuario!")
            

        else:
            input("Ok, vamos iniciar novamente o cadastro.")

def funcao_criar_conta(cpf):
    nova_conta = len(contas)+1
    contas.update({nova_conta:{
        "Agencia": 1,
        "CPF do Titular": cpf,
        "saldo" : 0,
        "limite" : 500,
        "extrato" : {},
        "numero_saques" : 0,
        "numero_depositos" : 0,
        "numero_transacao" : 0,}
        })
    print(f"\nConta {contas[nova_conta]["Agencia"]:04d}/{nova_conta:08d} Criada com sucesso!")

def pesquisa_cpf (cpf):
    teste_cpf = None
    for usuario in usuarios:
        extrair_cpf = usuarios[usuario]["CPF"]
        if str(extrair_cpf) == str(cpf):
            teste_cpf = usuario
        else:
            teste_cpf = "Não Localizado"
    return teste_cpf

def pesquisa_conta(cpf):
    teste_conta = ""

    for conta in contas:
        extrair_conta = contas[conta]["CPF do Titular"]
        if str(extrair_conta) == str(cpf):
            conta_encontrada = conta
            teste_conta += f"Conta Corrente: {contas[conta]["Agencia"]:04d}/{conta_encontrada:08d}\n"
    
    if not teste_conta:
        teste_conta = "Não Localizado Conta Corrente vinculadas a este CPF"
    
    return teste_conta

def texto_padrao_usuario(conta):

    trasnformar_cpf_string = str(usuarios[conta]["CPF"])
    cpf_formatado = f"{trasnformar_cpf_string[:3]}.{trasnformar_cpf_string[3:6]}.{trasnformar_cpf_string[6:9]}-{trasnformar_cpf_string[9:]}"
    texto_padrao = f"\nUsuario: {conta:04} \n   Nome: {usuarios[conta]['Nome']}\n   CPF: {cpf_formatado}\n   Endereço: {usuarios[conta]["Endereço Formatado"]}"      
    
    return texto_padrao

dados = {
    "saldo" : 0,
    "limite" : 500,
    "extrato" : {},
    "numero_saques" : 0,
    "numero_depositos" : 0,
    "numero_transacao" : 0,
}
contas = {1:{
    "Agencia": 1,
    "CPF do Titular": 44113756805,
    "saldo" : 0,
    "limite" : 500,
    "extrato" : {},
    "numero_saques" : 0,
    "numero_depositos" : 0,
    "numero_transacao" : 0,}
}

usuarios = { 1:{
        "Nome":"Danilo",
        "Data de Nascimento": "29/09/1995",
        "CPF": 44113756805,
        "Endereço Formatado" : "Rua Moema, 53 - Vila Pereta - Poá/SP",
        "Endereço" : {
            "Logradouro": "Rua Moema",
            "Numero" : 53,
            "Bairro" : "Vila Pereta",
            "Cidade" : "Poá",
            "Sigla" : "SP"},
        "Conta Corrente" : {"0001": 1}
        }}

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
    
    elif opcao == "C":

        print("Criar Usuario")
        funcao_criar_usuario()
        
    elif opcao == "N":
        print("Criar Conta Corrente")
        cpf_para_pesquisa = input("Favor digite o CPF do titular da nova conta: ")

        if pesquisa_cpf(cpf_para_pesquisa) == "Não Localizado" :

            print("Não existe usuário com este CPF, deseja criar um novo usuário?")
            teste = input("Digite [C] para Criar Usuário ou [S] para Sair: ")

            if teste == "c":
                print("Criar Usuário")
                funcao_criar_usuario()
            
        else:
            print(f"\n{pesquisa_conta(cpf_para_pesquisa)}")
            print("\nDeseja criar uma nova conta?")

            criar_nova_conta = input("Digite [S] para sim e [N] para não: ").upper()

            if criar_nova_conta == "S":
                funcao_criar_conta(cpf_para_pesquisa)
            else: continue

    elif opcao == "P":
        print("Verificar os usuarios")
        pesquisa_usuario = input('''
Você está na pagina para localizar os contratos feitos       
Para listar todos digite - [1]
Para buscar um usuario digite - [2]
''')
        
        if pesquisa_usuario == "1":

            for usuario in usuarios:
                print(texto_padrao_usuario(usuario)) 

        elif pesquisa_usuario == "2":

            pesquisa_por_cpf = int(input("Digite o CPf para pesquisa: "))
            conta = pesquisa_cpf(pesquisa_por_cpf)  
            print(texto_padrao_usuario(conta))

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")