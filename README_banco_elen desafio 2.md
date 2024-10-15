#OTIMIZAÇÃO DO DESAFIO SISTEMA BANCARIO SIMPLES 


#Teremos a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. **O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas**. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.


#>>Regras de Negócio
#>>>**Novo Depósito**
# A função desopito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

Antes >> Deve ser possível depositar **valores positivos**¹ para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e **exibidos na operação de extrato**².

#>>>**Novo Saque**
# A função saque deve receber os argumentos por nome (keywoord only) Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

Antes >> O sistema deve permitir realizar **3 saques diários**³ com **limite máximo de R$ 500,00 por saque**4. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**5. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#>>>**Novo Extrato**
# A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Antes >> Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o **saldo atual da conta**¨6. Se o **extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações**7.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
#1500.45 = R$ 1500.4

# NOVA FUNÇÃO


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