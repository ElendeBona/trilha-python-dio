# MODELANDO O DESAFIO SISTEMA BANCARIO V1 e V2


>Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML a seguir:
![diagrama do modelo UML sistema bancário](<modelando oo sistema bancario .png>)


# Desafio Extra
Após concluir a modelagem das classes e a criação dos métodos. Atualizar os métodos que tratam as opções do menu, para funcionarem com as classes modeladas. 

_______________________________

# >>Regras de Negócio

## >**NOVO Depósito**
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

*Antes* > Deve ser possível depositar **valores positivos**¹ para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e **exibidos na operação de extrato**².<br>

## >**NOVO Saque**

A função saque deve receber os argumentos por nome (keywoord only) Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

*Antes* > O sistema deve permitir realizar **3 saques diários**³ com **limite máximo de R$ 500,00 por saque**. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.<br>

## >**NOVO Extrato**
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

*Antes* > Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o **saldo atual da conta**. Se o **extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações**.Os valores devem ser exibidos utilizando o formato *R$ xxx.xx*, *exemplo: 1500.45 = R$ 1500.4*.


____________________________

## NOVA FUNÇÃO

## >> *Criar Usuário - Cliente* 
O programa deve armazenar os usuários erm uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.


## >> *Criar Conta corrente* 
O programa deve armazenar contas em uma lista, uma cconta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

```
menu =

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
```


## => ""MENU DE OPERAÇÃO""
# Regras de negócio 
```
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
```

> #Caminho para a pasta da minha versão do desafio > <br>
.trilha-python-dio-main\trilha-python-dio\README_banco_elen poo desafio 3.md <br>
.trilha-python-dio-main\trilha-python-dio\Desafio_sistema_bancario_elen\desafio_elen modelando sistema v1.py<br>
.trilha-python-dio-main\trilha-python-dio\Desafio_sistema_bancario_elen\desafio__elen modelando sistema v2.py<br>

