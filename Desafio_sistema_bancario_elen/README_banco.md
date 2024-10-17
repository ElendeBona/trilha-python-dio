#DESAFIO SISTEMA BANCARIO SIMPLES 


#Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#>>Regras de Negócio
#>>>**Depósito**
#Deve ser possível depositar **valores positivos**¹ para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e **exibidos na operação de extrato**².

#>>>**Saque**
#O sistema deve permitir realizar **3 saques diários**³ com **limite máximo de R$ 500,00 por saque**4. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**5. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#>>>**Extrato**
#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o **saldo atual da conta**¨6. Se o **extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações**7.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
#1500.45 = R$ 1500.4

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> ""MENU DE OPERAÇÃO""
#Regras de negócio 
saldo = 0 >0
limite = 500 #limite por operação por dia
extrato = "" #Menu com resumo de todos extratos e operações realizadas 
numero_saques = 0 != 3 por dia
LIMITE_SAQUES = 3


#Caminho para a pasta da minha versão do desafio > /trilha-python-dio-main/Desafio_sistema_bancario_elen/ 

sacjsjfcsp