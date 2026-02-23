import numpy as np
from src.board import Board
from src.markov import build_transition_matrix
from src.solvers import solve_exact, solve_iterative, solve_random_walk


def test_solvers_consistency():
    # 1. Preparar el entorno
    board = Board("config/board_config.yaml")
    P = build_transition_matrix(board)

    # 2. Ejecutar los tres métodos
    pi_exact = solve_exact(P)
    pi_iter, _ = solve_iterative(P, tol=1e-6)
    # Usamos menos pasos para que el test corra rápido, pero suficientes para una buena aproximación
    pi_rw, _ = solve_random_walk(P, num_steps=50000)

    # 3. Validar que todos sumen 1.0 (son distribuciones de probabilidad)
    np.testing.assert_allclose(
        np.sum(pi_exact), 1.0, rtol=1e-5, err_msg="El vector exacto no suma 1")
    np.testing.assert_allclose(
        np.sum(pi_iter), 1.0, rtol=1e-5, err_msg="El vector iterativo no suma 1")
    np.testing.assert_allclose(
        np.sum(pi_rw), 1.0, rtol=1e-5, err_msg="El vector random walk no suma 1")

    # 4. Validar que el método iterativo sea casi idéntico al exacto
    np.testing.assert_allclose(
        pi_exact, pi_iter, atol=1e-5, err_msg="El método iterativo difiere del exacto")

    # 5. Validar que el random walk se aproxime al exacto (mayor tolerancia por ser estocástico)
    np.testing.assert_allclose(
        pi_exact, pi_rw, atol=1e-2, err_msg="El random walk está muy lejos del valor teórico")
