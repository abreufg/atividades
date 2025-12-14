#Sisteminha de pagamentos

from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass


class Cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self):
        pass


class CartaoCredito(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.valor} processado no cartão de crédito.")

    def cancelar_pagamento(self):
        print("Pagamento no cartão de crédito cancelado.")


class Pix(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.valor} processado via Pix.")

    def cancelar_pagamento(self):
        print("Pagamento via Pix cancelado.")


class Boleto(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print(f"Boleto no valor de R$ {self.valor} gerado com sucesso.")

    def cancelar_pagamento(self):
        print("Boleto cancelado.")


pagamentos = [
    CartaoCredito(150),
    Pix(80),
    Boleto(200)
]

for pagamento in pagamentos:
    pagamento.processar_pagamento()
    pagamento.cancelar_pagamento()


