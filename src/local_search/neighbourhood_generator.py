from neighbourhood import Neighbourhood

class NeighbourhoodGenerator:
    """
    Clase que se usa para almacenar los métodos que generan vecindarios. Todos estos métodos devuelven una instancia de tipo Neighbourhood

    Métodos:
        neighbourhood_same_position(solution, problem): Genera un vecindario cambiando los jugadores por otros de su misma posición.
        random_neighborhood(solution, problem): Genera un vecindario seleccionando un jugador aleatorio que no esté en la solución y lo inserta en la nueva solución.
        full_random_neighborhood(solution, problem): Genera un vecindario cambiando los once jugadores por todos los demás jugadores.
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
        # Recorremos los ids de los jugadores desde el current_player hasta el final.
        for id, new_player in enumerate(problem.total_players, start = current_player["id"]):
            if current_player["position"] == new_player["position"] and new_player not in solution.lineup:
                # Hemos encontrado otro jugador con la misma posición
                new_solution = solution.copy()
                new_solution[id] = new_player
                break
            
        neighbourhood.append(new_solution)

    return neighbourhood

    # NO FUNCIONA
    def random_neighborhood(self, solution, neighborhood_generator):
    """
    Genera once soluciones cogiendo un jugador aleatorio e insertando en cada elemento del vector el jugador.

    Args:
        Players(list): Lista de todos los jugadores de nuestro dataset
        Solution(list): Lista de un estado solución actual con los id de todos los jugadores

    Returns:
        neighborhoods(List): Lista de once soluciones. Una por cada inserción.
    """
    encontrado = False
    neighboors = []
    no_visitados = neighborhood_generator.no_visitados.copy()
    idx = random.randint(0, len(no_visitados)-1)
    new_player = neighborhood_generator.players[idx]['id']
    neighborhood_generator.borrar_elemento_visitado(idx)
    for i in range(len(solution)):
        new_solution = solution.copy()
        new_solution[i] = new_player
        neighboors.append(new_solution)

    return neighboors
