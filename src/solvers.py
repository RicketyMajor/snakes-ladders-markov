import numpy as np

def solve_exact(P):
    """
    Método i: Sistema Lineal Exacto.
    Resuelve el sistema pi * P = pi, sujeto a la restricción sum(pi) = 1.
    Matemáticamente es equivalente a resolver (P^T - I) * pi^T = 0.
    """
    n = P.shape[0]
    # Construimos (P^T - I)
    A = P.T - np.eye(n)
    
    # Reemplazamos la última fila para incluir la restricción de que las probabilidades sumen 1
    A[-1] = np.ones(n)
    b = np.zeros(n)
    b[-1] = 1.0
    
    # Resolvemos el sistema de ecuaciones lineales
    pi = np.linalg.solve(A, b)
    return pi

def solve_iterative(P, tol=1e-6, max_iter=10000):
    """
    Método ii: Multiplicación Matriz-Vector (Power Iteration).
    Criterio de término: La norma L2 de la diferencia entre iteraciones consecutivas 
    debe ser menor a una tolerancia (tol).
    """
    n = P.shape[0]
    pi = np.ones(n) / n  # Iniciamos con una distribución uniforme
    history = [pi.copy()]
    
    for _ in range(max_iter):
        pi_next = np.dot(pi, P)
        history.append(pi_next.copy())
        
        # Criterio de parada: convergencia
        if np.linalg.norm(pi_next - pi, ord=2) < tol:
            break
            
        pi = pi_next
        
    return pi_next, history

def solve_random_walk(P, num_steps=100000):
    """
    Método iii: Simulación Random Walk (Monte Carlo).
    Criterio de término: Número fijo de pasos (num_steps). La Ley de los Grandes Números
    garantiza que las frecuencias relativas convergerán a pi.
    """
    n = P.shape[0]
    visits = np.zeros(n)
    current_state = 0  # Iniciamos en la casilla 1 (índice 0)
    history = []
    
    for step in range(1, num_steps + 1):
        visits[current_state] += 1
        
        # Guardamos la distribución empírica cada 1000 pasos para graficar después
        if step % 1000 == 0:
            history.append((visits / step).copy())
            
        # Transición al siguiente estado usando las probabilidades de la fila actual de P
        current_state = np.random.choice(n, p=P[current_state])
        
    pi = visits / num_steps
    return pi, history