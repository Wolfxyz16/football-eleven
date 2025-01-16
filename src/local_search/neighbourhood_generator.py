import random
import copy
from solution import Solution

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
        Genera una lista del conjunto de vecinos en los que cada nuevo vecino es un swap de cada jugador
        de la solución inicial por el jugador con id superior más cercano al actual que juegue en la misma posición.
    
        Args:
            solution(Solution): Solucion original de la que se generarán los vecinos.
            problem(Problem): Lista con todos los jugadores de nuestro problema.

        Returns:
            neighbourhood(Neighbourhood): Instancia de tipo Neighbourhood de la selección de los ids de los jugadores que forman parte de la solución.
        """
        player_id = list(range(0, problem.total_players))  # Lista con los IDs de los jugadores

        for player in solution.lineup:
            player_id.remove(player['id'])  # Remueve los IDs de los jugadores que ya están en la solución

        neighbours = []  # Inicializar la lista de soluciones vecinas

        # Iterar sobre los jugadores que no están en la solución
        for pl in player_id:
            new_player = problem.players[pl]  # Obtener el jugador a insertar en la solución
            # Buscar los vecinos con la misma posición
            for i in range(len(solution.lineup)):
                if solution.lineup[i]['position'] == new_player['position']:
                    new_solution = copy.deepcopy(solution)
                    new_solution.lineup[i] = new_player
                    new_solution.update(problem.objective_function(new_solution.lineup))
                    neighbours.append(new_solution)
            yield neighbours

    def all_random_neighborhood(self, solution, problem):
        player_id = list(range(0, problem.total_players))
        for i in range(len(solution.lineup)):
            player_id.remove(solution.lineup[i]['id'] - 1)
        random.shuffle(player_id)
        for pl in player_id:
            new_player = problem.players[pl]
            neighbours = []
            for i in range(len(solution.lineup)):
                new_solution = copy.deepcopy(solution)
                new_solution.lineup[i] = new_player
                new_solution.update(problem.objective_function(new_solution.lineup))
                neighbours.append(new_solution)
            yield neighbours

