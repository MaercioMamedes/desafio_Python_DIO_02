Desafio 01 do Bootcamp Python AI Backend Developer - Vivo - Digital Innovation One

## TODO

1. ### Modularizar o código criando funções para as operações: 
   - #### depositar
     - Deve receber os argumentos apenas por posição
   - #### sacar
     - Deve receber os argumentos apenas por nome
   - #### extrato
     - Deve receber os argumentos por posição e nome
       * argumento posicional: **saldo**
       * argumento nomeado: **extrato**
2. ### Criar mais duas funcionalidades para a aplicação:
   - #### Criar Usuário(cliente do Banco)
     - O programa deve armazenar os usuários numa lista
     - um Usuário é composto por:
       - Nome
       - data de nascimento
       - cpf
       - endereço (string: `Logradouro, número - bairro - cidade/sigla`)
     - Deve ser armazenado somente os números do CPF
     - Não é permitido 2 usuários com o mesmo CPF
   - #### criar Conta Correte( vinculada a um Usuário)
     - O programa deve armazenar contas em uma lista
     - uma conta é composta por:
       - agência
       - número da conta
       - usuário
     - O número da conta é sequencial, iniciando em 1
     - O número da agência é fixo: `0001`
     - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.