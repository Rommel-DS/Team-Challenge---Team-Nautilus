import numpy as np
import random
import string


class Tablero:
    def __init__(self, dimensiones=(10, 10), id_user=1, id_machine=0):
        self.dimensiones = dimensiones
        self.id_user = id_user
        self.id_machine = id_machine
        self.tablero_user = np.full(dimensiones, "~")
        self.tablero_machine = np.full(dimensiones, "~")
        self.disparos_realizados_user = set()
        self.disparos_realizados_machine = set()

    def colocar_barcos_en_tablero(self, barcos_dict, tablero):
#Coloca los barcos en el tablero.
        for posiciones in barcos_dict.values():
            for fila, columna in posiciones:
                tablero[fila, columna] = "O"

    def crear_barcos_aleatorios(self, tablero, esloras=[1, 2, 3, 4], cantidades=[4, 3, 2, 1], max_intentos=100):
#Crea barcos aleatorios en el tablero respetando las esloras y cantidades.
        barcos_dict = {}
        for eslora, cantidad in zip(esloras, cantidades):
            for n in range(cantidad):
                posiciones = self.intentar_colocar_barco(tablero, eslora, max_intentos)
                if posiciones:
                    barcos_dict[f"barco{eslora}_{n+1}"] = posiciones
        return barcos_dict

    def intentar_colocar_barco(self, tablero, eslora, max_intentos=100):
#Intenta colocar un barco de determinada eslora en el tablero, con un límite de intentos.
        for _ in range(max_intentos):
            fila_inicial, columna_inicial, orientacion = self.obtener_posicion_aleatoria(eslora)
            posiciones = [(fila_inicial, columna_inicial)]
            if self.posicion_valida(tablero, posiciones, orientacion, eslora):
                for _ in range(1, eslora):
                    fila_inicial, columna_inicial = self.siguiente_posicion(posiciones[-1][0], posiciones[-1][1], orientacion)
                    if not (0 <= fila_inicial < self.dimensiones[0] and 0 <= columna_inicial < self.dimensiones[1]):
                        break
                    posiciones.append((fila_inicial, columna_inicial))
                else:
                    self.colocar_barcos_en_tablero({f"barco{eslora}": posiciones}, tablero)
                    return posiciones
        return None

    def obtener_posicion_aleatoria(self, eslora):
#Devuelve una posición aleatoria válida para colocar un barco de una determinada eslora."""
        fila_inicial = random.randint(0, self.dimensiones[0] - 1)
        columna_inicial = random.randint(0, self.dimensiones[1] - 1)
        orientacion = random.choice(["N", "S", "O", "E"])
        return fila_inicial, columna_inicial, orientacion

    def posicion_valida(self, tablero, posiciones, orientacion, eslora):
#Valida si es posible colocar un barco de eslora en una orientación y posición dada en el tablero.
        for _ in range(1, eslora):
            fila_inicial, columna_inicial = self.siguiente_posicion(posiciones[-1][0], posiciones[-1][1], orientacion)
            if not (0 <= fila_inicial < self.dimensiones[0] and 0 <= columna_inicial < self.dimensiones[1]):
                return False
            if tablero[fila_inicial, columna_inicial] != "~":
                return False
            posiciones.append((fila_inicial, columna_inicial))
        return True

    def siguiente_posicion(self, fila, columna, orientacion):
#Devuelve la siguiente posición a partir de la posición actual y la orientación.
        direcciones = {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "O": (0, -1),
        }
        return fila + direcciones[orientacion][0], columna + direcciones[orientacion][1]

    def disparar(self, fila, columna, tablero_oponente, disparos_realizados):
#Realiza un disparo en las coordenadas dadas y devuelve el resultado.
        if (fila, columna) in disparos_realizados:
            return "Ya habías intentado aquí"
        disparos_realizados.add((fila, columna))
        if tablero_oponente[fila, columna] == "O":
            tablero_oponente[fila, columna] = "X"
            return "Impacto"
        tablero_oponente[fila, columna] = "*"
        return "Fallaste"
    
    #Comprobar Tocado o hundido
    def tocado_hundido(impacto):#impacto debería provenir de un imput que usaremos para la función disparar y para la función tocado_hundido
        impacto= tuple(impacto)# Por si introducen las coordenadas del impacto en tipo lista
        for barco, coordenadas in barcos_enemigos_dict.items():
                longitud_barco= len(coordenadas)
                comprueba_impactos= 0
                if impacto in coordenadas:
                        for coordenada in coordenadas:
                                if tablero_machine[coordenada]=="X":
                                        comprueba_impactos += 1
                        if comprueba_impactos== longitud_barco:
                                print("Barco Hundido")
                        elif comprueba_impactos< longitud_barco:
                                print("Barco Tocado")

    def imprimir_tablero(self, tablero, ocultar_barcos=False):
#Imprime el tablero, ocultando los barcos si se especifica.
        columnas = list(string.ascii_uppercase[:self.dimensiones[1]])
        print("  " + " ".join(columnas))
        for i, fila in enumerate(tablero):
            fila_impresa = [
                "~" if (casilla == "O" and ocultar_barcos) else casilla for casilla in fila
            ]
            print(f"{i + 1:2} " + " ".join(fila_impresa))  # Se ajusta para que la numeración de las filas empiece desde 1, no desde 0

    def obtener_coordenadas_usuario(self):
#Obtiene las coordenadas del disparo del usuario.
        while True:
            disparo = input("Ingresa las coordenadas del disparo (Ejemplo: A1, B3): ").upper()
            if len(disparo) >= 2 and disparo[0] in string.ascii_uppercase[:self.dimensiones[1]] and disparo[1:].isdigit():
                columna = string.ascii_uppercase.index(disparo[0])
                fila = int(disparo[1:]) - 1
                if 0 <= fila < self.dimensiones[0] and 0 <= columna < self.dimensiones[1]:
                    return fila, columna
            print("Coordenada inválida. Intenta de nuevo.")
    def iniciar_juego(self):
#Inicia el juego entre el usuario y la máquina.
        print("\n¡Bienvenido a Hundir la Flota!")
        print("A continuación, podrás disparar dentro diferentes coordenadas.")
        print("Las coordenadas van de A1 a J10.")
        
        self.barcos_user = self.crear_barcos_aleatorios(self.tablero_user)
        self.barcos_machine = self.crear_barcos_aleatorios(self.tablero_machine)
        
        print("\nTablero del usuario:")
        self.imprimir_tablero(self.tablero_user)
        
        print("\nTablero de la máquina (escondido):")
        self.imprimir_tablero(self.tablero_machine, ocultar_barcos=True)

        while not self.comprobar_fin_de_juego():
            print("\nTu turno")
            fila, columna = self.obtener_coordenadas_usuario()
            resultado = self.disparar(fila, columna, self.tablero_machine, self.disparos_realizados_user)
            print(f"Resultado: {resultado}")

            print("\nTurno de la máquina")
            fila, columna = random.randint(0, self.dimensiones[0] - 1), random.randint(0, self.dimensiones[1] - 1)
            print(f"La máquina disparó en {string.ascii_uppercase[columna]}{fila+1}")
            resultado = self.disparar(fila, columna, self.tablero_user, self.disparos_realizados_machine)
            print(f"Resultado de la máquina: {resultado}")

            print("\nTablero del usuario:")
            self.imprimir_tablero(self.tablero_user)
            
            print("\nTablero de la máquina (escondido):")
            self.imprimir_tablero(self.tablero_machine, ocultar_barcos=True)

    def comprobar_fin_de_juego(self):
#Comprueba si el juego ha terminado, es decir, si todos los barcos de un jugador han sido destruidos.
        if not np.any(self.tablero_machine == "O"):
            print("¡El usuario ha ganado!")
            return True
        if not np.any(self.tablero_user == "O"):
            print("¡La máquina ha ganado!")
            return True
        return False


                

