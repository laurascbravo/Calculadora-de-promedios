from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Importamos modelos
from modelos.modeloSemestre import Semestre

class NotasSabana(App):

    def build(self):
        # Inicializando modelos
        self.semestre = Semestre()

        # Configuramos los elementos
        self.window = GridLayout()
        self.window.cols = 2


        self.window.size_hint = (0.6, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.tfNota1 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 1"
        )

        self.tfPeso1 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 1"
        )

        self.tfNota2 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 2"
        )

        self.tfPeso2 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 2"
        )

        self.tfNota3 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 3"
        )

        self.tfPeso3 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 3"
        )

        self.tfNota4 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 4"
        )

        self.tfPeso4 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 4"
        )

        self.tfNota5 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 5"
        )

        self.tfPeso5 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 5"
        )

        self.tfNota6 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 6"
        )

        self.tfPeso6 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 6"
        )

        self.tfNota7 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 7"
        )

        self.tfPeso7 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 7"
        )

        self.tfNota8 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 8"
        )

        self.tfPeso8 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 8"
        )

        self.tfNota9 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 9"
        )

        self.tfPeso9 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 9"
        )

        self.tfNota10 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Nota 10"
        )

        self.tfPeso10 = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Peso 10"
        )

        # Un par de listas para manejar esto mejor
        self.listaTfNotas = [self.tfNota1, self.tfNota2, self.tfNota3, self.tfNota4, self.tfNota5, self.tfNota6, self.tfNota7, self.tfNota8, self.tfNota9, self.tfNota10]
        self.listaTfPesos = [self.tfPeso1, self.tfPeso2, self.tfPeso3, self.tfPeso4, self.tfPeso5, self.tfPeso6, self.tfPeso7, self.tfPeso8, self.tfPeso9, self.tfPeso10]

        self.tfCreditos = TextInput(
            multiline=False,
            size_hint=(0.4, 0.3),
            hint_text="Créditos del curso"
        )

        self.lNota = Label(
            text="Nota (Ej. 4.3)",
            font_size=35,
            color="#ffcc00"
        )

        self.lPeso = Label(
            text="Peso (Ej. 0.4)",
            font_size=35,
            color="#ffcc00"
        )

        self.lConfirmacion = Label(
            text="No se han añadido cursos.",
            font_size=15,
            color="#ffcc00"
        )
        self.lVacio = Label(
            text="   ",
            font_size=15,
            color="#ffcc00"
        )

        self.botCalcular = Button(text="Calcular Promedio",
             size_hint=(1, 0.5),
             bold=True,
             background_color="#ffcc00"  # ,
             # background_normal = ""
             )

        self.botRegistrar = Button(text="Registrar curso",
             size_hint=(1, 0.5),
             bold=True,
             background_color="#ffcc00"  # ,
             # background_normal = ""
             )

        # Agregamos los elementos
        self.window.add_widget(Image(source="./img/logo.png"))

        self.greeting = Label(
            text = "Inserta tus notas",
            font_size = 25,
            color="#ffcc00"
            )
        self.window.add_widget(self.greeting)


        self.window.add_widget(self.lNota)
        self.window.add_widget(self.lPeso)

        self.window.add_widget(self.tfNota1)
        self.window.add_widget(self.tfPeso1)

        self.window.add_widget(self.tfNota2)
        self.window.add_widget(self.tfPeso2)

        self.window.add_widget(self.tfNota3)
        self.window.add_widget(self.tfPeso3)

        self.window.add_widget(self.tfNota4)
        self.window.add_widget(self.tfPeso4)

        self.window.add_widget(self.tfNota5)
        self.window.add_widget(self.tfPeso5)

        self.window.add_widget(self.tfNota6)
        self.window.add_widget(self.tfPeso6)

        self.window.add_widget(self.tfNota7)
        self.window.add_widget(self.tfPeso7)

        self.window.add_widget(self.tfNota8)
        self.window.add_widget(self.tfPeso8)

        self.window.add_widget(self.tfNota9)
        self.window.add_widget(self.tfPeso9)

        self.window.add_widget(self.tfNota10)
        self.window.add_widget(self.tfPeso10)

        self.window.add_widget(self.lConfirmacion)
        self.window.add_widget(self.tfCreditos)

        self.botRegistrar.bind(on_press=self.callRegistrar)
        self.window.add_widget(self.botRegistrar)

        self.botCalcular.bind(on_press=self.callCalcular)
        self.window.add_widget(self.botCalcular)

        return self.window

    def callRegistrar(self, instance):
        datosListos = self.validarDatos()
        if datosListos == True:
            listaNotas = []
            listaPesos = []

            for i in range(10):
                hayNotaYPeso = True
                # Chequeamos notas no vacías
                if self.listaTfNotas[i].text == "":
                    print('tfNota'+str(i+1) + ' está vacío.')
                    hayNotaYPeso = False

                if self.listaTfPesos[i].text == "":
                    print('tfPeso'+str(i+1) + ' está vacío.')
                    hayNotaYPeso = False

                if hayNotaYPeso:
                    listaPesos.append(self.listaTfNotas[i].text)
                    listaNotas.append(self.listaTfPesos[i].text)

            self.semestre.agregarCurso(self.tfCreditos.text, listaNotas, listaPesos)

            self.lConfirmacion.text = 'Número de cursos registrados: '+str(self.semestre.darNumeroCursos())
        else:
            self.lConfirmacion.text = 'Falta información mínima.'

    def callCalcular(self, instance):
        promedio = self.semestre.calcularPromedioSemestre()
        self.greeting.text = 'Promedio: '+str(promedio)

    def validarDatos(self):

        # Chequeamos primera nota no vacía
        if self.tfNota1.text == "":
            print('tfNota1 está vacío.')
            return False

        if self.tfPeso1.text == "":
            print('tfPeso1 está vacío.')
            return False

        # Chequeamos créditos no vacío
        if self.tfCreditos.text == "":
            return False

        return True