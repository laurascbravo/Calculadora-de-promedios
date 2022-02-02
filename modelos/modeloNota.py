class Nota:
    def __init__(self, pValor, pPeso):
        self.valor = float(pValor)
        self.peso = float(pPeso)

    def darValor(self):
        return self.valor

    def darPeso(self):
        return self.peso
