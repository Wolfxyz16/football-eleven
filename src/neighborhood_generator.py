from solution import Solution
from problem import Problem
import random
class Neighborhood_generator:
    def __init__(self, problem):
        self.neighborhood = None
        self.problem = problem

    def set_neighborhood(self, neighborhood):
        self.neighborhood = neighborhood

    def random_search(self, solution, no_visitados):
        """
        Genera once soluciones cogiendo un jugador aleatorio e insertando en cada elemento del vector el jugador.

        Args:
            Players(list): Lista de todos los jugadores de nuestro dataset
            Solution(list): Lista de un estado solución actual con los id de todos los jugadores

        Returns:
            neighborhoods(List): Lista de once soluciones. Una por cada inserción.
        """
        
        neighboors = []
        
        
        idx = random.randint(0, len(no_visitados)-1)
        pl_id = no_visitados[idx]
        new_player = self.neighborhood.players[pl_id]
        
        for i in range(len(solution)):
            new_solution = solution.copy()
            new_solution[i] = new_player
            cost = self.problem.objective_function(new_solution)
            new_sol = Solution(new_solution, cost)
            neighboors.append(new_sol)

        return neighboors, new_player['id']

    def neighbourhood_same_position(self, solution, no_visitados):
        """
        Genera una lista del conjunto de vecinos en los que cada nuevo vecino es un swap de cada jugador de la solución inicial por el jugador con id superior más cercano al actual
        que juegue en la misma posición

        Args:
            solution(list): Solución actual de once jugadores que será alterada
        Returns:
            neighbourhood(list): Lista de vecinos de la selección de los ids de los jugadores que forman parte de la solución
        """

        neighbourhood = []
        no_visitados = self.neighborhood.no_visitados.copy()
        jugadores_visitados = []
        posiciones_visitadas = []
        i = 0
        while i < len(no_visitados) and len(posiciones_visitadas) < 4:
            jugador = no_visitados[i]
            new_player = self.neighborhood.players[idx]
            position = new_player['position']
            if position not in posiciones_visitadas:
                self.neighboors.borrar_elemento_visitado(idx)
                posiciones_visitadas.append(position)
                for j in range(len(solution)):
                    if position == solution[j]['position']:
                        new_solution = solution.copy()
                        new_solution[j] = new_player
                        cost = problem.objective_function(new_solution)
                        new_sol = Solution(new_solution, cost)
                        neighborhood.append(new_sol)
            i += 1
        return neighbourhood
