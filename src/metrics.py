import numpy as np


def get_transient_matrix(P):
    """
    Extrae la matriz Q de estados transitorios.
    Asumimos que el último estado (índice 49) es el estado absorbente
    para calcular métricas por una sola partida.
    """
    # La matriz Q excluye la última fila y última columna (estado 50)
    Q = P[:-1, :-1]
    return Q


def calculate_fundamental_matrix(Q):
    """
    Calcula la Matriz Fundamental N = (I - Q)^-1
    """
    n = Q.shape[0]
    I = np.eye(n)
    try:
        N = np.linalg.inv(I - Q)
        return N
    except np.linalg.LinAlgError:
        raise ValueError(
            "La matriz (I - Q) no es invertible. Revisa la definición de transitorios.")


def expected_game_duration(N):
    """
    Calcula el vector de tiempos esperados de absorción t = N * 1.
    Retorna la duración esperada empezando desde el primer estado (índice 0).
    """
    ones = np.ones(N.shape[0])
    t = np.dot(N, ones)
    return t[0]  # Duración esperada desde la casilla 1


def expected_visits_per_game(N):
    """
    Retorna el vector de visitas esperadas a cada casilla en una partida 
    que inicia en la casilla 1 (índice 0).
    """
    # La primera fila de N contiene las visitas esperadas a los estados transitorios
    visits = N[0, :]

    # Agregamos un 1.0 al final. ¿Por qué? Porque el estado absorbente (casilla 50)
    # se visita exactamente 1 vez al terminar (ganar) la partida.
    return np.append(visits, 1.0)
