# src/neighbourhood.py

class Neighbourhood:
    """
    Clase Neighbourhood que se encarga de almacenar el vecindario y sus diferentes métodos de generación

    """
    
    def __init__(self, solution):
        self.solution = solution
        self.neighbours = []
        self.num_neighbours = len(neighbours)

    def clean_neighborhood(self):
        """
        Limpia los atributos del vecindario
        """
        self.neighbours = []
        self.num_neighbours = 0

    def random_neighborhood(self, problem):
        """
        Genera once soluciones cogiendo un jugador aleatorio e insertando en cada elemento del vector el jugador.

        Args:
            problem (Problem): Instancia de tipo Problem que representa a todos los jugadores y demás datos
        """
        encontrado = False

        while not encontrado:
            player = problem.get_random_player()
            if player not in self.solution:
                new_player = player
                encontrado = True

        for i in range(len(solution)):
            new_solution = solution.deepcopy()
            new_solution[i] = new_player
            self.neighbours.append(new_solution)

        return neighboors
