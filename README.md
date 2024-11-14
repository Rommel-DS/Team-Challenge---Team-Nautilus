# Team-Challenge - Team-Nautilus
# Hundir la Flota

Este es un juego de "Hundir la Flota" (también conocido como "Battleship") implementado en Python. El juego permite que un jugador se enfrente a la máquina en un tablero de batalla de 10x10, donde el objetivo es hundir todos los barcos del oponente antes de que lo hagan contigo.

## Requisitos

- Python 3.x
- Biblioteca `numpy` (para manejar el tablero y las operaciones relacionadas con el juego)

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca `numpy` ejecutando:

   ```bash
   pip install numpy

## Descripcion

##### 1. Inicialización de la clase `Tablero` (`__init__`)

- **Objetivo:** Inicializa las dimensiones del tablero, los identificadores para el usuario y la máquina, y los tableros donde se colocarán los barcos.
- **Descripción:**
  - Se establecen las dimensiones del tablero como `(10, 10)` por defecto.
  - Se crea el tablero del usuario (`tablero_user`) y el de la máquina (`tablero_machine`), inicialmente llenos con el carácter `"~"` que indica agua.
  - Se crean conjuntos (`disparos_realizados_user` y `disparos_realizados_machine`) para llevar un registro de las coordenadas en las que el usuario y la máquina han disparado, respectivamente.

##### 2. Colocación de los barcos en el tablero (`colocar_barcos_en_tablero`)

- **Objetivo:** Coloca los barcos en el tablero de acuerdo con las posiciones definidas en un diccionario.
- **Descripción:**
  - Recibe un diccionario `barcos_dict` con las posiciones de los barcos y un `tablero`.
  - Para cada barco (definido por su nombre y lista de posiciones), coloca un barco (representado por `"O"`) en las posiciones especificadas en el tablero.

##### 3. Creación de barcos aleatorios (`crear_barcos_aleatorios`)

- **Objetivo:** Crea barcos de diferentes tamaños de forma aleatoria, asegurándose de que se ajusten al tamaño del tablero y no se superpongan.
- **Descripción:**
  - Toma las esloras (longitudes) de los barcos y sus cantidades como parámetros.
  - Para cada tipo de barco (con una eslora determinada y cantidad de barcos a colocar), intenta colocarlos de forma aleatoria en el tablero usando el método `intentar_colocar_barco`.
  - El método también recibe un parámetro `max_intentos`, que limita el número de intentos para colocar un barco antes de rendirse y no colocar ese barco.

##### 4. Intentar colocar un barco (`intentar_colocar_barco`)

- **Objetivo:** Intenta colocar un barco de una determinada longitud en el tablero, realizando varios intentos si es necesario.
- **Descripción:**
  - El método genera posiciones aleatorias en el tablero y verifica si es posible colocar el barco de acuerdo con su eslora y orientación (norte, sur, este, oeste). Si lo consigue, coloca el barco en el tablero; si no, intenta hasta el número máximo de intentos (100 por defecto).

##### 5. Obtener una posición aleatoria válida (`obtener_posicion_aleatoria`)

- **Objetivo:** Genera una posición aleatoria en el tablero para intentar colocar un barco.
- **Descripción:**
  - Se generan aleatoriamente una fila y una columna dentro de los límites del tablero, y también se selecciona aleatoriamente una de las cuatro orientaciones posibles para colocar el barco.

##### 6. Validar la colocación de un barco (`posicion_valida`)

- **Objetivo:** Verifica si una posición determinada es válida para colocar un barco.
- **Descripción:**
  - Para cada posición que el barco ocuparía, se verifica que no haya otro barco ya colocado en esa casilla (es decir, que la casilla esté vacía) y que no se salga de los límites del tablero.

##### 7. Obtener la siguiente posición de un barco (`siguiente_posicion`)

- **Objetivo:** Dado un barco en una casilla inicial y una orientación, devuelve la siguiente casilla que ocuparía el barco.
- **Descripción:**
  - Según la orientación (norte, sur, este, oeste), calcula la nueva casilla a la que debería moverse el barco.

##### 8. Disparar a una coordenada (`disparar`)

- **Objetivo:** Realiza un disparo en las coordenadas proporcionadas.
- **Descripción:**
  - Comprueba si ya se ha disparado antes en esa casilla.
  - Si no, marca la casilla como "impactada" (`"X"`) si el disparo es exitoso, o como fallido (`"*"`), si el disparo falla.

##### 9. Imprimir el tablero (`imprimir_tablero`)

- **Objetivo:** Imprime el tablero en la consola, mostrando los barcos si no se quiere ocultarlos.
- **Descripción:**
  - Imprime las coordenadas de las filas y columnas del tablero.
  - Si el parámetro `ocultar_barcos` es `True`, oculta los barcos del usuario (representados por `"O"`).

##### 10. Obtener las coordenadas del usuario para disparar (`obtener_coordenadas_usuario`)

- **Objetivo:** Pide al usuario que ingrese las coordenadas para un disparo.
- **Descripción:**
  - Solicita un input del usuario con el formato de coordenadas (como A1, B3, etc.).
  - Convierte las coordenadas al formato de fila y columna en el tablero.

##### 11. Iniciar el juego (`iniciar_juego`)

- **Objetivo:** Gestiona el ciclo principal del juego, alternando turnos entre el usuario y la máquina.
- **Descripción:**
  - Crea los barcos para el usuario y la máquina de manera aleatoria.
  - Muestra los tableros de ambos jugadores (el tablero del usuario se muestra completo, y el de la máquina con los barcos ocultos).
  - Alterna turnos de disparo entre el usuario y la máquina.
  - Al final de cada turno, muestra los tableros actualizados.
  - El juego termina cuando uno de los jugadores destruye todos los barcos del contrario.

##### 12. Comprobar fin de juego (`comprobar_fin_de_juego`)

- **Objetivo:** Comprueba si el juego ha terminado.
- **Descripción:**
  - Si todos los barcos de la máquina han sido destruidos, el usuario gana.
  - Si todos los barcos del usuario han sido destruidos, la máquina gana.
  - Si ninguno de los dos ha ganado, el juego sigue.
