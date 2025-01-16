# src/neighbourhood.py

class Neighbourhood:
    """
    Clase Neighbourhood que se encarga de almacenar el vecindario y sus diferentes métodos de generación

    """
    
    def __init__(self, solution):
        self.solution = solution
        self.neighbours = []
        self.num_neigh = len(neighbours)

    def clean_neighborhood(self):
        """
        Limpia los atributos del vecindario
        """
        self.neighbours = []
        self.num_neighbours = 0

