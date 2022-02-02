from modelos.modeloNota import Nota

class Curso:
    def __init__(self, pNumeroCreditos):
        self.listaNotas = []
        self.numeroCreditos = int(pNumeroCreditos)

    def darCreditos(self):
        return self.numeroCreditos

    def agregarNota(self, pValor, pPeso):
        nuevaNota = Nota(pValor, pPeso)
        self.listaNotas.append(nuevaNota)

    def darNumeroCursos(self):
        return len(self.listaNotas)

    def calcularPromedioCurso(self):

        acumulado = 0.0
        for nota in self.listaNotas:
            acumulado = acumulado + nota.darValor()*nota.darPeso()
            print('Acumulado Curso:')
            print(acumulado)


        promedio = acumulado
        print('Promedio curso')
        print(promedio)

        return promedio