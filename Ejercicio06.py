#Lab02 Python Funcional IAPP-2026-01
#Ejercicio 6 - Minimax

#Dado el juego conocido como NIM, implementar una solución a este usando el algoritmo minimax visto en clase

#En este juego hay una pila de piedras (por ejemplo 10).

#En cada turno un jugador puede quitar 1, 2 o 3 piedras.

#Pierde el jugador que no puede mover (porque ya no quedan piedras).

#MAX = Computadora

#MIN = Humano

#Dado lo anterior y el algoritmo visto en clase, modelar el juego y simularlo donde MAX sera la cpu y MIN el humado el cual interactua mediante el input, el primer turno sera el de MIN


# ---------------------------------------------------------
#   Jugador MAX = "CPU"
#   Jugador MIN = "Jugador"
# ---------------------------------------------------------

# Configuración inicial
QUANTITY = 10
BOARD = [0] * QUANTITY 

# ---------------------------------------------------------
#   Mostrar tablero
# ---------------------------------------------------------
def print_board(board):
    print(board)

# ---------------------------------------------------------
#   Jugadas legales
#   Devuelve [1, 2, 3], ajustándose si quedan menos piedras
# ---------------------------------------------------------
def legal_moves(board):
    return list(range(1, min(3, len(board)) + 1))

# ---------------------------------------------------------
#   Aplicar un movimiento
#   Elimina en masa la cantidad de piedras indicada por 'move'
# ---------------------------------------------------------
def apply_move(board, move):
    new_board = board.copy()
    new_board = new_board[move:]
    return new_board

# ---------------------------------------------------------
#   Estado terminal
#   El juego acaba cuando no quedan piedras (tablero vacío)
# ---------------------------------------------------------
def terminal(board):
    return len(board) == 0

# ---------------------------------------------------------
#   Función de utilidad
#   Evalúa quién perdió según a quién le tocaba mover
# ---------------------------------------------------------
def utility(maximizing):
    if maximizing:
        # Es turno de la CPU, pero no hay piedras -> Pierde la CPU -> Gana Jugador
        return -1
    else:
        # Es turno del Jugador, no hay piedras -> Pierde Jugador -> Gana CPU
        return 1

# ---------------------------------------------------------
#   ALGORITMO MINIMAX
#   maximizing = True  → turno de la CPU (MAX)
#   maximizing = False → turno del Jugador (MIN)
# ---------------------------------------------------------
def minimax(board, maximizing):

    # Caso base: estado final
    if terminal(board):
        return utility(maximizing)

    # Turno de MAX (CPU)
    if maximizing:
        best_value = float('-inf')
        for move in legal_moves(board):
            value = minimax(apply_move(board, move), False) # Simula jugada y pasa turno a MIN
            best_value = max(best_value, value)
        return best_value

    # Turno de MIN (Jugador)
    else:
        best_value = float('inf')
        for move in legal_moves(board):
            value = minimax(apply_move(board, move), True) # Simula jugada y pasa turno a MAX
            best_value = min(best_value, value)
        return best_value

# ---------------------------------------------------------
#   Seleccionar la mejor jugada para la CPU (MAX)
# ---------------------------------------------------------
def best_move(board):
    best_value = float('-inf')
    move_chosen = None

    for move in legal_moves(board):
        # La CPU evalúa qué pasa si elige este movimiento
        value = minimax(apply_move(board, move), False)
        if value > best_value:
            best_value = value
            move_chosen = move

    return move_chosen



# ---------------------------------------------------------
#   DEMO INTERACTIVA
# ---------------------------------------------------------
if __name__ == "__main__":
    board = [0] * 10
    print("--- ¡BIENVENIDO AL JUEGO DEL NIM! ---")
    print("Regla: Pierde el que se quede sin piedras para mover.\n")

    while not terminal(board):
        print(f"\nPiedras restantes en la mesa ({len(board)}):")
        print_board(board)

        # ---------------------------------------------------------
        # Turno de MIN (Jugador)
        # ---------------------------------------------------------
        try:
            move = int(input(f"Tu turno. ¿Cuántas piedras quitas? {legal_moves(board)}: "))
            
            # Validamos que el movimiento sea realmente legal en este momento
            if move not in legal_moves(board):
                print(f"¡Movimiento inválido! Solo puedes quitar {legal_moves(board)} piedras.")
                continue
                
            board = apply_move(board, move)
            
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            continue

        # Si el jugador dejó el tablero vacío, la CPU se queda sin movimientos y pierde.
        if terminal(board):
            print("\n===============================")
            print("¡Felicidades! ¡Le ganaste a la CPU!")
            print("===============================")
            break

        # ---------------------------------------------------------
        # Turno de MAX (CPU)
        # ---------------------------------------------------------
        print("\nLa computadora está pensando...")
        cpu_move = best_move(board)
        
        if cpu_move is not None:
            print(f"La CPU decide quitar {cpu_move} piedras.")
            board = apply_move(board, cpu_move)

        # Si la CPU dejó el tablero vacío, el jugador se queda sin movimientos y pierde.
        if terminal(board):
            print_board(board)
            print("\n===============================")
            print("La CPU te ha ganado. ¡Su algoritmo es perfecto!")
            print("===============================")
            break
