import numpy as np
from src.board import Board
from src.markov import build_transition_matrix
from src.metrics import (
    get_transient_matrix,
    calculate_fundamental_matrix,
    expected_game_duration,
    expected_visits_per_game
)


def test_metrics_calculations():
    board = Board("config/board_config.yaml")
    P = build_transition_matrix(board)

    # Para aislar una partida, simulamos matemáticamente que el estado 50 es absorbente
    P_absorb = P.copy()
    P_absorb[49, :] = 0
    P_absorb[49, 49] = 1.0

    Q = get_transient_matrix(P_absorb)
    assert Q.shape == (49, 49), "La matriz Q debe ser de 49x49"

    N = calculate_fundamental_matrix(Q)
    assert N.shape == (49, 49), "La matriz N debe ser de 49x49"

    # La duración esperada debe ser un número positivo razonable
    duration = expected_game_duration(N)
    assert duration > 5.0, "La duración de la partida debería ser mayor a 5 turnos"

    # El vector de visitas debe tener tamaño 50 (49 transitorios + 1 absorbente)
    visits = expected_visits_per_game(N)
    assert len(visits) == 50, "El vector de visitas debe tener 50 elementos"
    assert visits[-1] == 1.0, "El estado 50 se debe visitar exactamente 1 vez para ganar"
