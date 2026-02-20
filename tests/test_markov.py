import numpy as np
from src.board import Board
from src.markov import build_transition_matrix

def test_transition_matrix_is_stochastic():
    board = Board("config/board_config.yaml")
    P = build_transition_matrix(board)
    
    # Verificamos la forma de la matriz
    assert P.shape == (50, 50), "La matriz debe ser de 50x50"
    
    # Verificamos que todas las filas sumen 1 (con una pequeña tolerancia por redondeo de coma flotante)
    row_sums = np.sum(P, axis=1)
    np.testing.assert_allclose(row_sums, 1.0, rtol=1e-5, err_msg="Las filas de la matriz no suman 1")
    
    # Verificamos el reinicio de partida (Fila 50 va al índice 0)
    assert P[49, 0] == 1.0, "El estado 50 debe transicionar determinísticamente al estado 1"