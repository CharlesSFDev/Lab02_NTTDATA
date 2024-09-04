import textwrap
from datetime import datetime

def menu():
    menu = '''\n
    ---------------MENU---------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNota Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair
    ----------------------------------
    '''
    return input(textwrap.dedent(menu))
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite permitido.")

    elif excedeu_saques:
        print("Operação falhou! Você já fez o número máximo de saques por hoje.")

    elif valor > 0:
        saldo = saldo - valor
        extrato += f"Saque: R$ {valor}. /n Saldo = R$ {saldo}./n Data e Hora: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}\n"
        numero_saques = numero_saques + 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo  = saldo + valor
        extrato += f"Depósito: R$ {valor}./nSaldo = R$ {saldo}./n Data e Hora: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("--------------EXTRATO--------------")
    print("Não foram realizadas transaçõs." if not extrato else extrato)
    print(f"Saldo: R$ {saldo}.")
    print("-----------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário cadastrado com este CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "endereço":endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("Usuário não encontrado!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado: "))
            saldo, extrato = sacar(saldo = saldo, 
                                valor = valor,
                                extrato = extrato,
                                limite = limite,
                                numero_saques = numero_saques,
                                limite_saques = LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta =  len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
main()