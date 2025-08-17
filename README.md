# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido inicialmente no Bootcamp **"DIO & Suzano -
Python Developer"**, com o objetivo de praticar fundamentos da linguagem
Python.\
Após a base inicial, o sistema foi expandido para contemplar
funcionalidades adicionais e simular um ambiente bancário de forma
didática, mas aplicando conceitos utilizados em sistemas corporativos.

------------------------------------------------------------------------

## 📌 Funcionalidades

-   **Depósito**
    -   Adiciona valores à conta.\
    -   Atualiza saldo e extrato automaticamente.
-   **Saque**
    -   Valida saldo disponível.\
    -   Respeita limite por transação (`R$500,00`).\
    -   Controla quantidade máxima de saques diários (`3 saques`).
-   **Extrato**
    -   Apresenta histórico detalhado de movimentações.\
    -   Mostra data/hora de cada operação.\
    -   Exibe saldo atualizado.
-   **Cadastro de Usuários**
    -   Inclui dados pessoais (nome, data de nascimento, CPF).\
    -   Cadastra endereço completo.\
    -   Verifica duplicidade de CPF.
-   **Criação de Contas Correntes**
    -   Permite múltiplas contas vinculadas a um mesmo CPF.\
    -   Identificação de contas pelo formato `Agência/Conta`.
-   **Login com Cookie**
    -   Armazena CPF em sessão (cookie).\
    -   Evita necessidade de login repetido durante a execução.

------------------------------------------------------------------------

## ⚙️ Características Técnicas

-   **Estruturas de Dados**: utilização de **dicionários e listas** para
    armazenamento de clientes, contas e transações.\
-   **Validações de Entrada**: CPF duplicado, valores inválidos, limite
    de transações diárias.\
-   **Controle de Sessão**: gerenciamento de login com cookie para
    manter usuário ativo.\
-   **Datas e Horários**: cálculo automático do tempo restante até a
    liberação de novas transações.\
-   **Funções Modulares**: cada operação implementada de forma
    independente (saque, depósito, extrato, criação de conta/usuário).

------------------------------------------------------------------------

## 🏢 Relevância em um Contexto Empresarial

Apesar de acadêmico, o projeto traz conceitos que são aplicados em
empresas:

-   **Gestão de Identidade e Acesso** → login, autenticação e vínculo de
    contas por CPF.\
-   **Controle Financeiro** → saldo consistente, limites e registro de
    transações com horário.\
-   **Escalabilidade** → estrutura que suporta múltiplas contas por
    cliente.\
-   **Segurança e Integridade de Dados** → validação de entradas e
    duplicidades.\
-   **Organização de Código** → funções modulares, facilitando
    manutenção e evolução.

------------------------------------------------------------------------

## 🚀 Possíveis Evoluções

-   Persistência de dados em banco (SQLite, PostgreSQL).\
-   Interface gráfica (Tkinter ou frameworks web).\
-   Geração de relatórios financeiros automatizados.\
-   Implementação de testes unitários para regras de negócio.\
-   Uso de **APIs REST** para disponibilizar serviços de
    contas/usuários.

------------------------------------------------------------------------

## ▶️ Como Executar o Projeto

1.  Clone este repositório:

    ``` bash
    git clone https://github.com/Danilo-Palacio/sistema_bancario.git
    ```

2.  Entre na pasta do projeto:

    ``` bash
    cd sistema_bancario
    ```

3.  Execute o script em Python:

    ``` bash
    main.py
    ```

------------------------------------------------------------------------

## 📂 Estrutura de Dados

### Exemplo de `usuários`:

``` python
usuarios = {
    1:{
        "Nome":"Danilo",
        "Data de Nascimento": "01/01/1995",
        "CPF": 441,
        "Endereço Formatado" : "Rua da residencia, 00 - Bairro escolhido - cidade/SP",
        "Endereço" : {
            "Logradouro": "Rua da residencia",
            "Numero" : 00,
            "Bairro" : "Bairro escolhidoa",
            "Cidade" : "cidade",
            "Sigla" : "SP"},
        "Conta Corrente" : {"0001": 1}
    }
}
```

### Exemplo de `contas`:

``` python
contas = {
    1:{
        "Agencia": 1,
        "CPF do Titular": usuarios[1]["CPF"],
        "saldo" : 0,
        "limite" : 500,
        "extrato" : {},
        "numero_saques" : 0,
        "numero_depositos" : 0,
        "numero_transacao" : 0,
    }
}
```

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto desenvolvido por **Danilo Palacio** no Bootcamp **DIO & Suzano -
Python Developer**.\
📧 \[[LinkedIn](https://www.linkedin.com/in/danilocpalacio/)]

------------------------------------------------------------------------
