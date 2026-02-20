import numpy as np
from src.board import Board

def build_transition_matrix(board: Board):
    n = board.size
    A = np.zeros((n, n)) # Transiciones que terminan el turno
    B = np.zeros((n, n)) # Transiciones que continúan el turno (sacar 6 y no caer en trampa)
    
    # Probabilidad de cada cara del dado
    p_roll = 1.0 / board.die_faces
    
    for i in range(n):
        # Regla de encadenamiento: 50 -> 1 (índice 49 -> índice 0)
        if i == n - 1:
            A[i, 0] = 1.0
            continue
            
        for roll in range(1, board.die_faces + 1):
            dest, triggered_trap = board.get_destination(i, roll)
            
            # Regla: Si sale 6 y NO activas trampa, repites turno
            if roll == 6 and not triggered_trap:
                B[i, dest] += p_roll
            else:
                A[i, dest] += p_roll
                
    # Cálculo matricial P = (I - B)^-1 * A
    I = np.eye(n)
    try:
        I_minus_B_inv = np.linalg.inv(I - B)
        P = np.dot(I_minus_B_inv, A)
    except np.linalg.LinAlgError:
        raise ValueError("La matriz (I - B) no es invertible. Revisa la configuración del tablero.")
        
    return P