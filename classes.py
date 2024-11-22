from abc import ABC, abstractmethod
from funcoes import *
import os

class Conta(ABC):
    # Construtor
    def __init__(self, saldo: float = 0.0):
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
        if self.get_saldo >= valor:
           self.sacar(valor)
           conta_destino.depositar(valor)
           print(f"Transferência de R${valor}")
        else:
           print("Saldo insuficiente para realizar tranferência")
        
    def consultar_saldo(self) -> float:
        """Retorna o saldo atual"""
        return self._saldo

# METODOS GET
    def get_saldo(self):
        return self.__saldo #   # Retorna o saldo atual da conta com o self privado

# METODOS SET
    def set_saldo(self, saldo: float) -> None: # Recebeu um novo valor como argumento e definiu o saldo
        return self.__saldo
    
#-------------------------------------------------------------------

class ContaCorrente(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo) 
        # Inicializa a conta corrente com um saldo inicial

    def sacar(self, valor: float) -> None:
        if valor > self.get_saldo():
            raise ValueError("Saldo insuficiente para realizar o saque.")
        else:
               self.set_saldo(self.get_saldo() - valor)
               print(f"Saque de R${valor} realizado com sucesso")
               print(f'Saldo atual {self.get_saldo()}')
            # Realiza o saque, sem alguma restrição de limite minimo de saldo
        
    def depositar(self, valor: float):
        self.set_saldo(self.get_saldo() + valor)
     
# METODOS GET
    def get_saldo(self):
        return super().consultar_saldo()  #   # Retorna o saldo atual da conta com o self privado

# METODOS SET
    def set_saldo(self, saldo: float) -> None: # Recebeu um novo valor como argumento e definiu o saldo

        self._Conta__saldo = saldo # Acessar um atributo que seja privado, já que é privado, nao posso tentar pegar diretamente na classe filha

    # Name mangling é uma maneira de acessar atributos privados de outra classe
     
#-------------------------------------------------------------------

class ContaPoupanca(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo)
        # Inicializa a conta poupança com um saldo inicial, chamando o construtor da classe base
        
    def sacar(self, valor: float) -> None:
          
           if self.get_saldo() - valor >= 100:
              print(f"Saque de R${valor} realizado com sucesso")
              print(f'Saldo atual {self.get_saldo()}')
           else:
               raise ValueError('Seu saldo está abaixo de R$100.00')
           # Verifica se o saldo restante sera igual ou maior que 100,00 antes de fazer o saque

    def depositar(self, valor: float):
        self.set_saldo(self.get_saldo() + valor)

# Métodos GET
    def get_saldo(self):
        return super().consultar_saldo()

# Métodos SET
    def set_saldo(self, saldo: float) -> None: # Recebeu um novo valor como argumento e definiu o saldo

        self._Conta__saldo = saldo
    
#-------------------------------------------------------------------

class Cliente():    
    def __init__(self, nome, cpf, senha, saldo):
        
        self.__nome = nome # Armazena o nome do usuario como um atributo privado

        self.__cpf = cpf # Armazena o CPF do usuario como um atributo privado

        self.__senha = senha  # Armazena a senha do usuario como um atributo privado

        self.__contas = []  # Inicializa uma lista vazia para armazenar as contas dos clientes

        self.__saldo = saldo

    def adicionar_conta(self, clientes):
        self.__contas.append(clientes)
    # Adiciona uma nova conta a lista de contas do usuario

    def remover_conta(self, clientes):
        if clientes in self.__contas:
            self.__contas.remove(clientes)
        else:
            print("Conta não encontrada!, tente novamente")
    # Remove uma conta da lista de contas do usuario

    def getLista(self):
        return self.__contas

    def consultar_conta(self, cpf, senha):
        for conta in self.__contas:    
            if cpf == conta.getCpf() and senha == conta.getSenha():
                print("Login feito com sucesso :)")
                return True, conta
        print("CPF ou senha inválidos. Tente novamente.")
        return False, None 
        # Retorna falso se a conta nao for encontrada

# Métodos GET
    
    def getNome(self):
        return self.__nome # Retorna o nome do usuario

    def getCpf(self):
        return self.__cpf # Retorna o CPF do usuario
    
    def getSenha(self):
        return self.__senha # Retorna a senha do usuario
    
    def getSaldo(self):
        return self.__saldo

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
    def __init__(self):
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
    def get_saldo(self):
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
        
        if cliente in self._cliente:
            self._clientes.remove(cliente)
        else:
            print("Cliente não foi encontrado no banco.")
    
#--------------------------------------------------------------------------------


