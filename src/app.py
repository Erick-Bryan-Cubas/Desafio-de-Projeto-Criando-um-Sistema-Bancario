""" Simula um sistema bancário com cadastro de usuários, 
criação de contas correntes e operações bancárias. """

class Banco:
    """ Classe para simular um sistema bancário. """
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.numero_conta_atual = 1

    def formatar_cpf(self, cpf_numeros):
        """Recebe uma string com 11 dígitos numéricos e retorna o CPF formatado."""
        return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"

    def cadastrar_usuario(self):
        """Cadastra um novo usuário e retorna o dicionário com os dados do usuário,
        ou None se o usuário não for cadastrado."""
        nome = input("Informe seu nome, por gentileza: ")
        if len(nome) <= 4:
            print("Informe um nome válido.")
            return None
        data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
        cpf_numeros = input("Informe seu CPF (apenas números): ")
        cpf_formatado = self.formatar_cpf(cpf_numeros)
        if (not cpf_numeros.isdigit() or
            len(cpf_numeros) != 11 or
            any(usuario['cpf'] == cpf_formatado for usuario in self.usuarios)):
            print("CPF inválido ou já cadastrado.")
            return None
        endereco = input(
            "Informe seu endereço (logradouro, nro - bairro - cidade/sigla do estado): "
            )
        usuario = {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cpf": cpf_formatado,
                "endereco": endereco
                }
        self.usuarios.append(usuario)
        return usuario

    def criar_conta_corrente(self, usuario):
        """Cria uma nova conta corrente para o usuário e retorna o dicionário com os dados da conta,
        ou None se a conta não for criada."""
        conta = {
            "Agencia": "0001",
            "Numero": self.numero_conta_atual,
            "Usuario": usuario['cpf'],
            "Saldo": 0,
            "Movimentacoes": [],
            "SaquesRealizados": 0
        }
        self.contas.append(conta)
        self.numero_conta_atual += 1
        return conta

    def encontrar_conta_por_cpf(self, cpf):
        """Retorna uma lista com as contas do usuário com o CPF informado,
        ou None se não encontrar nenhuma conta."""
        cpf_formatado = self.formatar_cpf(cpf)
        contas_usuario = [conta for conta in self.contas if conta["Usuario"] == cpf_formatado]
        if contas_usuario:
            return contas_usuario
        return None

    def extrato(self, conta):
        """
        Imprime um extrato bancário, mostrando o saldo atual e todas as movimentações realizadas.
        """
        print("=" * 30)
        print("Extrato Bancário")
        print("=" * 30)
        print(f"Saldo: R$ {conta['Saldo']:.2f}")
        print("Movimentações:")
        for movimento in conta['Movimentacoes']:
            print(movimento)
        print("=" * 30)

    def depositar(self, conta):
        """Deposita um valor na conta corrente."""
        deposito = float(input("Informe o valor para efetuar o depósito: "))
        if deposito <= 0:
            print("Valor para depósito inválido! Informe um valor inteiro positivo não nulo.")
        else:
            conta["Saldo"] += deposito
            movimento = f"Depósito de R$ {deposito:.2f}"
            conta["Movimentacoes"].append(movimento)
            print(f"Foram depositados na conta de {conta['Usuario']}: R$ {deposito:.2f} reais")
            print(f"Saldo atualizado: R$ {conta['Saldo']:.2f}")

    def sacar(self, conta):
        """Realiza um saque na conta corrente."""
        if conta['SaquesRealizados'] >= 3:
            print("Limite máximo de saques diários atingido.")
            return
        saque = float(input("Informe o valor para efetuar o saque: "))
        if saque <= 0 or saque > 500:
            print(
                "Valor para saque inválido! O valor do saque deve ser maior "
                "que zero e no máximo R$ 500,00."
                )
        elif conta["Saldo"] < saque:
            print("Saldo insuficiente! Tente outro valor.")
        else:
            conta["Saldo"] -= saque
            movimento = f"Saque de R$ {saque:.2f}"
            conta["Movimentacoes"].append(movimento)
            conta['SaquesRealizados'] += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            print(f"Saldo atualizado: R$ {conta['Saldo']:.2f}")

    def acessar_conta(self):
        """Permite ao usuário criar um novo usuário e conta corrente 
        ou acessar uma conta existente."""
        print("Selecione uma opção:")
        print("1 - Criar novo usuário e conta corrente")
        print("2 - Acessar conta existente")
        opcao = input("Opção: ")
        if opcao == "1":
            usuario = self.cadastrar_usuario()
            if usuario:
                nova_conta = self.criar_conta_corrente(usuario)
                print(
                    f"Conta número {nova_conta['Numero']} criada para o usuário "
                    f"{usuario['nome']} na agência {nova_conta['Agencia']}!"
                    )
                return nova_conta
        elif opcao == "2":
            cpf = input("Informe seu CPF para acesso: ")
            contas = self.encontrar_conta_por_cpf(cpf)
            if contas:
                if len(contas) > 1:
                    numeros_conta = [str(conta['Numero']) for conta in contas]
                    mensagem = (
                        f"Você tem as seguintes contas: {', '.join(numeros_conta)}. "
                        "Qual número de conta deseja acessar? "
                    )
                    numero_conta = input(mensagem)
                    conta_selecionada = next(
                    (conta for conta in contas if str(conta['Numero']) == numero_conta),
                    None
                    )

                    if conta_selecionada:
                        print(
                            f"Bem-vindo de volta, {conta_selecionada['Usuario']}!" 
                            f"Conta número {conta_selecionada['Numero']} acessada."
                            )
                        return conta_selecionada
                    else:
                        print("Número de conta não encontrado.")
                else:
                    conta_selecionada = contas[0]
                    print(
                        f"Bem-vindo de volta, {conta_selecionada['Usuario']}! "
                        f"Conta número {conta_selecionada['Numero']} acessada."
                        )
                    return conta_selecionada
            else:
                print("Conta não encontrada.")
        else:
            print("Opção inválida.")
        return None

banco = Banco()
print("=" * 30)
print("Seja bem-vindo ao DIO-BANK")
print("=" * 30)

while True:
    print("""
Deseja acessar uma conta?
    Pressione 1 para entrar
    Pressione 0 para sair
""")
    acessar_conta_opcao = input()
    if acessar_conta_opcao == "0":
        break
    elif acessar_conta_opcao == "1":
        conta_atual = banco.acessar_conta()
        if conta_atual is not None:
            while True:
                print("""
Selecione a operação desejada:
    1 - Depositar
    2 - Sacar
    3 - Visualizar Extrato
    0 - Sair
""")
                operacao = input()
                if operacao == "1":
                    banco.depositar(conta_atual)
                elif operacao == "2":
                    banco.sacar(conta_atual)
                elif operacao == "3":
                    banco.extrato(conta_atual)
                elif operacao == "0":
                    break
                else:
                    print("Operação inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
