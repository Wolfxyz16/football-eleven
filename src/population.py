# src/population.py

class Population:
    """
    Clase que representa un conjunto de soluciones
    """
    def __init__(self, solutions = None, max_population = None):
        self.solutions = solutions
        self.max_population = max_population
        if solutions == None:
            self.size = 0
        else:
            self.size = len(solutions)

    def add_solution(self, solution):
        """
        Adds a given solution to the solutions list. Then it updates de size
        """
        if max_population:
            self.solutions.append(solution)
            self.size += 1
            return self.size
        else:
            raise Exception("Population is full.")

    def best_solution(self, evaluation_function):
        """
        Returns the best solution from the population
        """
        if not self.solutions:
            raise Exception("There are none solutions.")

        return max(self.solutions, key = evaluation_function)
