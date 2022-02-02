from modelos.modeloCurso import Curso

class Semestre:
    def __init__(self):
        self.listaCursos = []

    def agregarCurso(self, pCreditos, listaNotas, listaPesos):
        nuevoCurso = Curso(pCreditos)
        contador = 0
        for nota in listaNotas:
            nuevoCurso.agregarNota(listaNotas[contador], listaPesos[contador])
            contador = contador + 1
        self.listaCursos.append(nuevoCurso)


    def calcularPromedioSemestre(self):
        totalCreditos = self.calcularTotalCreditos()
        acumulado = 0.0
        for curso in self.listaCursos:
            acumulado = acumulado + curso.calcularPromedioCurso()*curso.darCreditos()
            print('Acumulado Semestre:')
            print(acumulado)

        promedio = acumulado / totalCreditos
        print('Total créditos')
        print(totalCreditos)
        print('Promedio semestre')
        print(promedio)
        return promedio

    def darNumeroCursos(self):
        return len(self.listaCursos)

    def calcularTotalCreditos(self):
        total = 0
        for curso in self.listaCursos:
            total = total + int(curso.darCreditos())
        return total