Desafio 02 do Bootcamp Python AI Backend Developer - Vivo - Digital Innovation One

## ToDo

1. ### Modularizar o código criando funções para as operações: 
   - #### depositar
     - :white_check_mark: Deve receber os argumentos apenas por posição: `saldo, valor, extrato`
   - #### sacar
     - :white_check_mark: Deve receber os argumentos apenas por nome: `saldo, valor, extrato, numero_saques, limite_saques`
   - #### extrato
     - Deve receber os argumentos por posição e nome
       * :white_check_mark: argumento posicional: **saldo**
       * :white_check_mark: argumento nomeado: **extrato**
2. ### Criar mais duas funcionalidades para a aplicação:
   - #### Criar Usuário(cliente do Banco)
     - :white_check_mark: O programa deve armazenar os usuários numa lista
     - um Usuário é composto por:
       - :white_check_mark: Nome
       - :white_check_mark: data de nascimento
       - :white_check_mark: cpf
       - :white_check_mark: endereço (string: `Logradouro, número - bairro - cidade/sigla`)
     - :white_check_mark: Deve ser armazenado somente os números do CPF
     - :white_check_mark: Não é permitido 2 usuários com o mesmo CPF
   - #### criar Conta Correte( vinculada a um Usuário)
     - :white_check_mark: O programa deve armazenar contas em uma lista
     - :white_check_mark: uma conta é composta por:
       - :white_check_mark: agência
       - :white_check_mark: número da conta
       - :white_check_mark: usuário
     - :white_check_mark:O número da conta é sequencial, iniciando em 1
     - :white_check_mark: O número da agência é fixo: `0001`
     - :white_check_mark: O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.