# Sistema Bancário DIO-BANK

O Sistema Bancário DIO-BANK é uma simulação de operações bancárias básicas, incluindo cadastro de usuários, criação de contas correntes e execução de operações bancárias como depósitos, saques e consulta de extratos.

## Funcionalidades

- **Cadastro de Usuários:** Permite o cadastro de novos usuários com informações básicas como nome, data de nascimento, CPF e endereço.
- **Criação de Contas Correntes:** Após o cadastro, é possível criar uma conta corrente associada ao usuário.
- **Operações Bancárias:** Os usuários podem realizar depósitos e saques em suas contas correntes, além de consultar o extrato bancário que mostra todas as movimentações. Contudo o saque só é permitido se o saldo for suficiente. Além de ser limitado a R$ 500,00 em apenas 3 operações por dia.

## Como Usar

Para utilizar o sistema, siga os passos abaixo:

1. Inicie o script para que o sistema seja carregado.
2. Será apresentada a mensagem de boas-vindas do DIO-BANK. Siga as instruções na tela para acessar uma conta existente ou criar uma nova conta.
3. Se optar por criar uma nova conta, informe os dados solicitados (nome, data de nascimento, CPF e endereço).
4. Para acessar uma conta existente, informe o CPF associado à conta.
5. Uma vez na conta, escolha entre as operações disponíveis: depositar, sacar, visualizar extrato ou sair.

## Tecnologias Utilizadas

- Python: Linguagem de programação utilizada para desenvolver todas as funcionalidades do sistema.

## Limitações

- O sistema não possui persistência de dados, ou seja, todas as informações são perdidas ao encerrar a execução do script.
- A validação dos dados é básica, focando principalmente na formatação e na unicidade do CPF.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
