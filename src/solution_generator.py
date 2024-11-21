# src/solution-generator.py
from solution import Solution 

class SolutionGenerator():
    """
    Clase que se encarga de almacenar los distintos métodos de generación de soluciones

    """
    import random

    def __init_(self):
        pass

    def random_solution(self, problem):
        """
        Dados unos datos de los jugadores, devuelve una solución de 11 jugadores aleatorios

        Args:
            problem (Problem): Objeto de tipo Problem que contiene todos los jugadores y funciones de utilidad
        """
        players = []
        num_players = len(players)
        max_players = problem.total_players

        # Genereamos 11 jugadores random y los metemos en la solucion
        while num_players != 11:
            id = self.random.randint(1, max_players)
            player = problem.players[id]
            if player not in players:
                num_players += 1
                players.append(player)

        value = problem.objective_function(players)
        
        solution = Solution(players, value)

        return solution
