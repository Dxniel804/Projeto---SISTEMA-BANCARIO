from abc import ABC, abstractmethod 
from funcoes import *
import os

class Conta(ABC):   
    # Construtor
    def __init__(self, saldo:float=0.0):
        self.__saldo = saldo
    @abstractmethod
    def depositar(self) -> None:
        """Adiciona o valor ao saldo"""
        pass
     
    @abstractmethod
    def sacar(self) -> None:
        """Remove o valor do saldo"""
        pass

    def transferir(self, conta_destino, valor: float) -> None:
        """Transfere valor para outra conta"""
        if self.getSaldo() >= valor:
           self.sacar(valor)
           conta_destino.depositar(valor)
           print(f"Transferência de R${valor}")
        else:
           print("Saldo insuficiente para realizar tranferência")
        
    def consultar_saldo(self) -> float:
        """Retorna o saldo atual"""
        return self.__saldo

# METODOS GET
    def getSaldo(self):
        return self.__saldo # Retorna o saldo atual da conta com o self privado

    def setSaldo(self, saldo):
        self.__saldo = saldo
#-------------------------------------------------------------------

class ContaCorrente(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo)
    
    def sacar(self, valor: float) -> None:
        if valor > self.getSaldo(): 
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.setSaldo(self.getSaldo() - valor)
            print(f"Saque de R${valor} realizado com sucesso")
            print(f'Saldo atual {self.getSaldo()}')

    def depositar(self, deposito: float):
        self.setSaldo(self.getSaldo() + deposito)
     
    def __str__(self):
        return f"R${self.getSaldo():.2f}"
    #Método (str): Definir como um objeto sera mostrado como uma string 
#-------------------------------------------------------------------    
def consultar_conta(self, cpf, senha):

    for conta in self.__contas:    
        if cpf == conta.getCpf() and senha == conta.getSenha():
            print("Login feito com sucesso :)")
            return True, conta, self  # Retorna também a instância do cliente
    print("CPF ou senha inválidos. Tente novamente.")
    return False, None, None  # Retorna None para o cliente também

class ContaPoupanca(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo)

    def sacar(self, valor: float) -> None:

        if self.getSaldo() - valor >= 100:
            self.setSaldo(self.getSaldo() - valor) 
            print(f"Saque de R${valor} realizado com sucesso")
            print(f'Saldo atual {self.getSaldo()}')
        else:
            print('Seu saldo está abaixo de R$100.00')

    def depositar(self, valor):

        self.setSaldo(self.getSaldo() + valor)
        print(f"Depósito de R${valor} realizado com sucesso!")

    def adicionarSaldo(self, deposito):

        self.__saldo += deposito
    
#-------------------------------------------------------------------

class Cliente():    
    def __init__(self, nome, cpf, senha, saldo_corrente=0.0, saldo_poupanca=0.0):
        
        self.__nome = nome # Armazena o nome do usuario como um atributo privado

        self.__cpf = cpf # Armazena o CPF do usuario como um atributo privado

        self.__senha = senha  # Armazena a senha do usuario como um atributo privado

        self.__contas = []  # Inicializa uma lista vazia para armazenar as contas dos clientes

        self.conta_corrente = ContaCorrente(saldo=saldo_corrente) 
        self.conta_poupanca = ContaPoupanca(saldo=saldo_poupanca) 

    def adicionar_conta(self, clientes):

        self.__contas.append(clientes)
        print(f'Conta do {clientes} adicionada')
    # Adiciona uma nova conta a lista de contas do usuario

    def remover_conta(self, conta):

        if conta in self.__contas:
            self.__contas.remove(conta)
            print(f'Conta {conta} removida com sucesso')
        else:
            print("Conta não encontrada, tente novamente")
    # Remove uma conta da lista de contas do usuario

    def getLista(self):

        return self.__contas

    def consultar_conta(self, cpf, senha):

        for conta in self.__contas:    
            if cpf == conta.getCpf() and senha == conta.getSenha():
                print("Login feito com sucesso :)")
                return True, conta, self  # Retorna também a instância do cliente
        print("CPF ou senha inválidos. Tente novamente.")
        return False, None, None  # Retorna None para o cliente também

    def retirar_saldo(self, deposito):

        if deposito <= self.__saldo:
            self.__saldo -= deposito
            return True
        else:
            print("Saldo insuficiente.")
            return False

# Métodos GET
    
    def getNome(self):
        return self.__nome # Retorna o nome do usuario

    def getCpf(self):
        return self.__cpf # Retorna o CPF do usuario
    
    def getSenha(self):
        return self.__senha # Retorna a senha do usuario
    
    def getSaldo(self):
        return self.__saldo # Retorna o saldo do usuario

# Métodos SET

    def setNome(self, nome):
        self.__nome = nome  # Define ou tambem pode atualizar o nome do usuario

    def setCpf(self, cpf):
        self.__cpf = cpf # Define ou tambem pode atualizar o nome do usuario

    def setSenha(self, senha):
        self.__senha = senha # Define ou tambem pode atualizar o nome do usuario

    def setSaldo(self, saldo):
        self.__saldo = saldo

#-------------------------------------------------------------------

class Extrato():
    def __init__(self, saldo):
        self.__saldo = saldo
        self.__transacoes = []
 # Inicializa uma nova instancia da classe Extrato
# Cria uma lista privada para armazenar as transações        
    
    def adicionar_transacao(self, descricao: str, valor: float) -> None:

        transacao = {'Descrição': descricao, 'Valor': valor} # Cria um dicionário para a transação com descrição e valor 
        self.__transacoes.append(transacao) # Adiciona a transação a lista privada de transações   
        
    def consultar_extrato(self) -> list:

        self.consultar_extrato = []

    # Retorna a lista de transações armazenadas    

# METODOS GET
    def getSaldo(self):
        return self.__saldo

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Banco():
    def __init__(self):
        self.clientes = []
# Inicializa uma nova instância da classe Banco
# Cria uma lista para armazenar os clientes do banco

    def adicionar_cliente(self, clientes: 'Cliente') -> None:  
        
        self.clientes.append(clientes)
    # Adiciona o cliente à lista de clientes    

    def remover_cliente(self, cliente: 'Cliente') -> None: 
        
        if cliente in self.__cliente:
            self.__clientes.remove(cliente)
        else:
            print("Cliente não foi encontrado no banco.")
    
#--------------------------------------------------------------------------------


