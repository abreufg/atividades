#questao 1
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):
        return self.__saldo


conta = ContaBancaria()
conta.depositar(100)
conta.sacar(30)
print("Saldo:", conta.ver_saldo())
#Questão 2
class Pessoa:
    def __init__(self, nome, ano_nasceu):
        self.nome = nome          # público
        self._anoNasceu = ano_nasceu  # protegido


p = Pessoa("João", 2000)

print(p.nome)          # acesso normal
print(p._anoNasceu)    # possível, mas NÃO recomendado
#questão 3
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("O saldo não pode ser negativo.")


conta = ContaBancaria()
conta.saldo = 200
print(conta.saldo)
#Questai 4
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.preco = preco  # usa o setter

    @property
    def nome(self):
        return self.__nome   # somente leitura

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço não pode ser negativo.")


produto = Produto("Caderno", 15.50)
print(produto.nome)
print(produto.preco)

produto.preco = 20
print(produto.preco)
