from neighbourhood import Neighbourhood

class NeighbourhoodGenerator:
    """
    Clase que se usa para almacenar los métodos que generan vecindarios. Todos estos métodos devuelven una instancia de tipo Neighbourhood

    Métodos:
        neighbourhood_same_position(solution, problem): Genera un vecindario cambiando los jugadores por otros de su misma posición.
    """
    
    def neighbourhood_same_position(self, solution, problem):
    """
    Genera una lista del conjunto de vecinos en los que cada nuevo vecino es un swap de cada jugador de la solución inicial por el jugador 
    con id superior más cercano al actual que juegue en la misma posición.

    Args:
        solution(Solution): Solucion original de la que se generarán los vecinos.
        problem(Problem): Lista con todos los jugadores de nuestro problema.

    Returns:
        neighbourhood(Neighbourhood): Instancia de tipo Neighbourhood de la selección de los ids de los jugadores que forman parte de la solución.
    """

    neighbourhood = Neighbourhood(solution)

    # Por cada jugador en la solución actual.
    for current_player in solution.lineup:

        # Recorremos los ids de los jugadores hasta el final.
        for id in range( current_player["id"] + 1, problem.total_players ):
            new_player = problem.players[id]
            if current_player["position"] == new_player["position"] and new_player not in solution.lineup:
                # Hemos encontrado otro jugador con la misma posición
                new_solution = solution.copy()
                new_solution[i] = players[j]["id"]
                break
            
        neighbourhood.append(new_solution)

    return neighbourhood
