# Desafio de Código: Sistema Bancário Orientado a Objetos

## Objetivo
O objetivo geral deste desafio é atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML fornecido.

## Contextualização
Vamos atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos. O foco é em Programação Orientada a Objetos (POO) e a modelagem de classes. Não é necessário entender todos os detalhes do diagrama UML fornecido, pois o foco é na implementação em Python.

## Diagrama UML
![Diagrama UML](images/Trilha%20Python%20-%20desafio.png)

## Desafio Parte 1
1. **Modelagem das Classes**: Crie classes para representar `Conta`, `ContaCorrente`, `Cliente`, `PessoaFisica`, `Historico`, `Transacao`, `Deposito` e `Saque` conforme o diagrama UML.
2. **Implementação Inicial**: Construa a estrutura das classes e seus atributos e métodos, conforme descrito no diagrama.
3. **Operações Básicas**: As operações de `saldo`, `nova_conta`, `sacar` e `depositar` devem ser implementadas na classe `Conta`.
4. **Histórico de Transações**: A classe `Historico` deve permitir adicionar transações, e a classe `Transacao` deve ser uma interface para `Deposito` e `Saque`.

A resolução da parte 1 pode ser encontrada em `src/resolucao_desafio_parte_1.py`.

## Desafio Parte 2
1. **Atualização dos Métodos**: Após concluir a modelagem das classes, atualize os métodos que tratam as opções do menu para funcionarem com as classes modeladas.
2. **Integração com o Menu**: Faça com que o sistema volte a funcionar redondinho com o uso do menu e as operações todas funcionando.

A resolução da parte 2 pode ser encontrada em `src/resolucao_desafio_parte_2.py`.
