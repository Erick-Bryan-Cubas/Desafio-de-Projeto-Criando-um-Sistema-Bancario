print("=" * 30)
print("Seja bem-vindo! ao DIO-BANK")
print("=" * 30)

banco = []

def criar_conta():
    conta = {"Saldo": 0}
    usuario = input("Informe seu nome, por gentileza: ")
    
    if len(usuario) <= 4:
        print("Informe um nome válido.")
        return None
    
    conta["Usuario"] = usuario
    banco.append(conta)
    
    return conta

def depositar(conta):
    deposito = float(input("Informe o valor para efetuar o depósito: "))
    if deposito <= 0:
        print("Valor para depósito inválido! Informe um valor inteiro positivo não nulo.")
    else:
        conta["Saldo"] += deposito
        print(f"Foram depositados na conta de {conta['Usuario'].upper()}: R$ {deposito} reais")

def sacar(conta):
    saque = float(input("Informe o valor para efetuar o saque: "))
    if conta["Saldo"] < saque:
        print("Saldo insuficiente! Tente outro valor.")
    else:
        conta["Saldo"] -= saque

def visualizar_extrato(conta):
    print(f"Saldo atual da conta de {conta['Usuario'].upper()}: R$ {conta['Saldo']:.2f} reais")

while True:
    acessar_conta = int(input(f"""
Deseja acessar uma conta?
    Pressione 1 para entrar
    Pressione 0 para sair
"""))
    if acessar_conta == 0:
        break
    elif acessar_conta == 1:
        conta_atual = criar_conta()
        if conta_atual is not None:
            while True:
                operacao = int(input(f"""
Selecione a operação desejada:
    1 - Depositar
    2 - Sacar
    3 - Visualizar Extrato
    0 - Sair
"""))
                if operacao == 1:
                    depositar(conta_atual)
                elif operacao == 2:
                    sacar(conta_atual)
                elif operacao == 3:
                    visualizar_extrato(conta_atual)
                elif operacao == 0:
                    break
                else:
                    print("Operação inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
