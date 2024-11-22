# src/solution-generator.py

from solution import Solution 

class SolutionGenerator():
    """
    Clase que se encarga de almacenar los distintos métodos de generación de soluciones

    Métodos:
        random_solution(problem):       Devuelve una solución de 11 jugadores aleatorios
        baseline_solution(problem):     Intenta construir una solución decente y la devuelve

    """
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
            player = problem.get_random_player()
            if player not in players:
                num_players += 1
                players.append(player)

        value = problem.objective_function(players)
        
        solution = Solution(players, value)

        return solution
    
    def baseline_solution(self, problem):
        """
        Genera una solución de once jugadores respetando que haya un único portero, que la formación sea válida y que no se pase del presupuesto

        Args:
            problem (Problem): Instancia de Problem donde encontramos los jugadores, presupuesto máximo, etc.

        Returns:
            solution (Solution): Instancia de Solution donde encontramos los jugadores alineados y su valor, entre otros
        """
        solution = []
        maxPlayers = problem.total_players - 1
        contador_posiciones = {'G': 1, 'D': 0, 'M': 0, 'F': 0}
        suma_presupuesto = 0
        hayPortero = False

        # generamos un portero
        while not hayPortero:
            player = problem.get_random_player()
            if player["position"] == 'G':
                suma_presupuesto += player["value"]
                hayPortero = True
                solution.append(player)

        posicion_anterior = 'G'

        while sum(contador_posiciones.values()) != 11:
            player = problem.get_random_player()
            player_position = player["position"]
            player_value = player["value"]

            if (
                player not in solution                                          # Si no está en la solución
                and contador_posiciones[player_position] < 5                    # Si en su posición hay menos de 5 jugadores
                and suma_presupuesto + player_value < problem.max_presupuesto   # Si el presupuesto me lo permite
                and player_position != 'G'                                      # Si no es portero
                and posicion_anterior != player_position                        # Si el jugador que hemos metido antes tiene diferente posición
            ):
                contador_posiciones[player_position] += 1
                solution.append(player)
                posicion_anterior = player_position
        
        value = problem.objective_function(solution)

        return Solution(solution, value)

