import pilas, random
from pilas.actores import Banana, Bomba, Aceituna, Mono

pilas.iniciar()
musica = pilas.musica.cargar('cancionMario.mp3')
musica.reproducir()


class EscenaDeMenu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        fondo = pilas.fondos.DesplazamientoHorizontal()
        fondo.agregar('fondoMenu.png')

        opciones = [
		    ('Jugar con Mario', self.comenzar),
		    ('Jugar con Luigi', self.comenzarL),
            ('Salir', self.salir)]

        self.menu = pilas.actores.Menu(opciones)

    def comenzar(self):
        pilas.cambiar_escena(EscenaDeJuego())

    def comenzarL(self):
        pilas.cambiar_escena(Luigi())

    def salir(self):
        import sys
        sys.exit(0)


class EscenaDeJuego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        class BananaConMovimiento(Banana):

            def __init__(self, x=0, y=0):
                Banana.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Hongo.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 140

            def actualizar(self):
                self.y += -2.5
                if (puntos.obtener() > 790):
                    self.y -= 3
                elif (puntos.obtener() > 1190):
                    self.y -= 3.5

        def comer_banana(mono, banana):
            banana.eliminar()
            Hongo = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
            Hongo.escala = 0.15
            bananas.append(Hongo)
            puntos.aumentar(20)
            pactuales = puntos.obtener()
            if (pactuales == 300 or pactuales==600 or pactuales == 900 or pactuales == 1200 or pactuales == 1500):
                vidas.ganarvidas()

        def crear_comida():
            if (puntos.obtener() > 790):
                t = 0.5
            else:
                t = 1
            Hongo = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
            Hongo.escala = 0.15
            bananas.append(Hongo)
            pilas.mundo.agregar_tarea(t, crear_comida)

        class BombaConMovimiento(Bomba):

            def __init__(self, x=0, y=0):
                Bomba.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Enemigo.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 80

            def actualizar(self):
                self.y += -2.5
                if (puntos.obtener() > 790):
                    self.y -= 3
                elif (puntos.obtener() > 1190):
                    self.y -= 3.5

        class PlantaC(Aceituna):

            def __init__(self, x=0, y=0):
                Aceituna.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Planta.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 40
                self.direccion = 0.5

            def actualizar(self):
                if (self.y > -175):
                    self.direccion = -self.direccion
                self.y += self.direccion

        def crear_planta():
            t = 10
            planta = PlantaC(x=random.randrange(-320, 320), y=-280)
            planta.escala = 0.7
            planta.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
            plantas.append(planta)
            pilas.mundo.agregar_tarea(t, crear_planta)

        def crear_enemigo():
            if (puntos.obtener() > 790):
                t = 0.5
            else:
                t = 1 
            enemigo = BombaConMovimiento(x=random.randrange(-320, 320), y=240)
            enemigo.escala = 0.2
            bombas.append(enemigo)
            pilas.mundo.agregar_tarea(t, crear_enemigo)

        def hacer_explotar_una_bomba(mono, bomba):
            bomba.explotar()
            puntos.aumentar(-40)
            vidas.perdervidas()

        def morir_por_planta(mono, plantas):
            puntos.aumentar(-40)
            vidas.perdervidas()

        class Vidas():

            def __init__(self, Vida=3):
                self.vidas = Vida
                self.vida0 = MiProtagonista(x=-290, y=160)
                self.vida1 = MiProtagonista(x=-240, y=160)
                self.vida2 = MiProtagonista(x=-190, y=160)
                self.vida0.escala = 0.12
                self.vida1.escala = 0.12
                self.vida2.escala = 0.12

            def ganarvidas(self):
                self.vidas += 1
                if (self.vidas == 2):
                    self.vida1 = MiProtagonista(x=-240, y=160)
                    self.vida1.escala = 0.12
                    pilas.avisar("Ahora tienes 2 vidas")
                elif (self.vidas == 3):
                    self.vida2 = MiProtagonista(x=-190, y=160)
                    self.vida2.escala = 0.12
                    pilas.avisar("Ahora tienes 3 vidas")
                elif (self.vidas == 4):
                    self.vida3 = MiProtagonista(x=-140, y=160)
                    self.vida3.escala = 0.12
                    pilas.avisar("Ahora tienes 4 vidas")
                elif (self.vidas == 5):
                    self.vida4 = MiProtagonista(x=-90, y=160)
                    self.vida4.escala = 0.12
                    pilas.avisar("Ahora tienes 5 vidas")
                elif (self.vidas == 6):
                    self.vidas -= 1

            def perdervidas(self):
                self.vidas -= 1
                if (self.vidas == 4):
                    self.vida4.eliminar()
                    pilas.avisar("Te quedan 4 vidas")
                elif (self.vidas == 3):
                    self.vida3.eliminar()
                    pilas.avisar("Te quedan 3 vidas")
                elif (self.vidas == 2):
                    self.vida2.eliminar()
                    pilas.avisar("Te quedan 2 vidas")
                elif (self.vidas == 1):
                    self.vida1.eliminar()
                    pilas.avisar("Te queda 1 vida!!")
                elif (self.vidas == 0):
                    self.vida0.eliminar()
                    tperder = pilas.actores.Texto("Has perdido ...")
                    tperder.escala = 5
                    tperder.escala = [1], 0.5
                    pilas.escena_actual().tareas.eliminar_todas()
                    mono.eliminar()
                    pilas.avisar("Pulsa la tecla 'Q' para regresar al menu...")

        class MiProtagonista(Mono):
            
            def __init__(self, x=0, y=0):
                Mono.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Mario.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 100


#Ubicacion, color y tamano de los puntos
        puntos = pilas.actores.Puntaje(x=-260, y=220, color=pilas.colores.blanco)
        puntos.magnitud = 40
#carga las vidas
        vidas = Vidas()

#El personaje que se usa
        mono = MiProtagonista(x=0, y=-180)
        fondo = pilas.fondos.DesplazamientoHorizontal()
        fondo.agregar('fondo.png')
        pilas.actores.Sonido()

#habilidades del protagonista
        mono.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        mono.escala = 0.2
        pilas.avisar("Pulsa A o D para mover al mono. \nLas plantas matan instantaneamente")
#asignacion de teclas del control
        teclas = {pilas.simbolos.a: 'izquierda',
                  pilas.simbolos.d: 'derecha',}
        mi_control = pilas.control.Control(pilas.escena_actual(), teclas)
        mono.aprender(pilas.habilidades.MoverseConElTeclado, control=mi_control)

        planta = PlantaC(x=random.randrange(-320,320), y=-280)
        planta.escala = 0.7
        plantas = [planta]

        banana = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
        banana.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        banana.escala = 0.15
        bananas = [banana]

        bomba = BombaConMovimiento(x=random.randrange(-320, 320), y=240)
        bomba.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        bomba.escala = 0.2
        bombas = [bomba]

        pilas.mundo.agregar_tarea(1, crear_enemigo)
        pilas.mundo.agregar_tarea(1, crear_comida)
        pilas.mundo.agregar_tarea(10, crear_planta)

        pilas.escena_actual().colisiones.agregar(mono, bananas, comer_banana)
        pilas.escena_actual().colisiones.agregar(mono, bombas, hacer_explotar_una_bomba)
        pilas.escena_actual().colisiones.agregar(mono, plantas, morir_por_planta)

        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == 'q':
            pilas.cambiar_escena(EscenaDeMenu())

class Luigi(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        class BananaConMovimiento(Banana):

            def __init__(self, x=0, y=0):
                Banana.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Hongo.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 140

            def actualizar(self):
                self.y += -2.5
                if (puntos.obtener() > 790):
                    self.y -= 3
                elif (puntos.obtener() > 1190):
                    self.y -= 3.5

        def comer_banana(mono, banana):
            banana.eliminar()
            Hongo = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
            Hongo.escala = 0.15
            bananas.append(Hongo)
            puntos.aumentar(20)
            pactuales = puntos.obtener()
            if (pactuales == 300 or pactuales==600 or pactuales == 900 or pactuales == 1200 or pactuales == 1500):
                vidas.ganarvidas()

        def crear_comida():
            if (puntos.obtener() > 790):
                t = 0.5
            else:
                t = 1
            Hongo = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
            Hongo.escala = 0.15
            bananas.append(Hongo)
            pilas.mundo.agregar_tarea(t, crear_comida)

        class BombaConMovimiento(Bomba):

            def __init__(self, x=0, y=0):
                Bomba.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Enemigo.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 80

            def actualizar(self):
                self.y += -2.5
                if (puntos.obtener() > 790):
                    self.y -= 3
                elif (puntos.obtener() > 1190):
                    self.y -= 3.5

        class PlantaC(Aceituna):

            def __init__(self, x=0, y=0):
                Aceituna.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Planta.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 40
                self.direccion = 0.5

            def actualizar(self):
                if (self.y > -175):
                    self.direccion = -self.direccion
                self.y += self.direccion

        def crear_planta():
            t = 10
            planta = PlantaC(x=random.randrange(-320, 320), y=-280)
            planta.escala = 0.7
            planta.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
            plantas.append(planta)
            pilas.mundo.agregar_tarea(t, crear_planta)

        def crear_enemigo():
            if (puntos.obtener() > 790):
                t = 0.5
            else:
                t = 1 
            enemigo = BombaConMovimiento(x=random.randrange(-320, 320), y=240)
            enemigo.escala = 0.2
            bombas.append(enemigo)
            pilas.mundo.agregar_tarea(t, crear_enemigo)

        def hacer_explotar_una_bomba(mono, bomba):
            bomba.explotar()
            puntos.aumentar(-40)
            vidas.perdervidas()

        def morir_por_planta(mono, plantas):
            puntos.aumentar(-40)
            vidas.perdervidas()

        class Vidas():

            def __init__(self, Vida=3):
                self.vidas = Vida
                self.vida0 = MiProtagonista(x=-290, y=160)
                self.vida1 = MiProtagonista(x=-240, y=160)
                self.vida2 = MiProtagonista(x=-190, y=160)
                self.vida0.escala = 0.12
                self.vida1.escala = 0.12
                self.vida2.escala = 0.12

            def ganarvidas(self):
                self.vidas += 1
                if (self.vidas == 2):
                    self.vida1 = MiProtagonista(x=-240, y=160)
                    self.vida1.escala = 0.12
                    pilas.avisar("Ahora tienes 2 vidas")
                elif (self.vidas == 3):
                    self.vida2 = MiProtagonista(x=-190, y=160)
                    self.vida2.escala = 0.12
                    pilas.avisar("Ahora tienes 3 vidas")
                elif (self.vidas == 4):
                    self.vida3 = MiProtagonista(x=-140, y=160)
                    self.vida3.escala = 0.12
                    pilas.avisar("Ahora tienes 4 vidas")
                elif (self.vidas == 5):
                    self.vida4 = MiProtagonista(x=-90, y=160)
                    self.vida4.escala = 0.12
                    pilas.avisar("Ahora tienes 5 vidas")
                elif (self.vidas == 6):
                    self.vidas -= 1

            def perdervidas(self):
                self.vidas -= 1
                if (self.vidas == 4):
                    self.vida4.eliminar()
                    pilas.avisar("Te quedan 4 vidas")
                elif (self.vidas == 3):
                    self.vida3.eliminar()
                    pilas.avisar("Te quedan 3 vidas")
                elif (self.vidas == 2):
                    self.vida2.eliminar()
                    pilas.avisar("Te quedan 2 vidas")
                elif (self.vidas == 1):
                    self.vida1.eliminar()
                    pilas.avisar("Te queda 1 vida!!")
                elif (self.vidas == 0):
                    self.vida0.eliminar()
                    tperder = pilas.actores.Texto("Has perdido ...")
                    tperder.escala = 5
                    tperder.escala = [1], 0.5
                    pilas.escena_actual().tareas.eliminar_todas()
                    mono.eliminar()
                    pilas.avisar("Pulsa la tecla 'Q' para regresar al menu...")

        class MiProtagonista(Mono):
            
            def __init__(self, x=0, y=0):
                Mono.__init__(self, x, y)
                self.image_normal = pilas.imagenes.cargar('Luigi.png')
                self.definir_imagen(self.image_normal)
                self.radio_de_colision = 100


#Ubicacion, color y tamano de los puntos
        puntos = pilas.actores.Puntaje(x=-260, y=220, color=pilas.colores.blanco)
        puntos.magnitud = 40

#seteo de la musica de fondo
        musica = pilas.musica.cargar('cancionMario.mp3')
        musica.reproducir()
#carga las vidas
        vidas = Vidas()

#El personaje que se usa
        mono = MiProtagonista(x=0, y=-180)
        fondo = pilas.fondos.DesplazamientoHorizontal()
        fondo.agregar('fondo.png')
        pilas.actores.Sonido()

#habilidades del protagonista
        mono.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        mono.escala = 0.15
        pilas.avisar("Pulsa A o D para mover al mono. \nLas plantas matan instantaneamente")
#asignacion de teclas del control
        teclas = {pilas.simbolos.a: 'izquierda',
                  pilas.simbolos.d: 'derecha',}
        mi_control = pilas.control.Control(pilas.escena_actual(), teclas)
        mono.aprender(pilas.habilidades.MoverseConElTeclado, control=mi_control)

        planta = PlantaC(x=random.randrange(-320,320), y=-280)
        planta.escala = 0.7
        plantas = [planta]

        banana = BananaConMovimiento(x=random.randrange(-320, 320), y=240)
        banana.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        banana.escala = 0.15
        bananas = [banana]

        bomba = BombaConMovimiento(x=random.randrange(-320, 320), y=240)
        bomba.aprender(pilas.habilidades.SeMantieneEnPantalla, permitir_salida=True)
        bomba.escala = 0.2
        bombas = [bomba]

        pilas.mundo.agregar_tarea(1, crear_enemigo)
        pilas.mundo.agregar_tarea(1, crear_comida)
        pilas.mundo.agregar_tarea(10, crear_planta)

        pilas.escena_actual().colisiones.agregar(mono, bananas, comer_banana)
        pilas.escena_actual().colisiones.agregar(mono, bombas, hacer_explotar_una_bomba)
        pilas.escena_actual().colisiones.agregar(mono, plantas, morir_por_planta)

        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def cuando_pulsa_tecla(self, evento):
        if evento.texto == 'q':
            pilas.cambiar_escena(EscenaDeMenu())
	
# Carga la nueva escena
pilas.cambiar_escena(EscenaDeMenu())
pilas.ejecutar()
