# src/population.py

class Population:
    """
    Clase que representa un conjunto de soluciones junto a distintos metodos utiles

    Atributos:
        solutions (List): Lista que contiene las soluciones de la población
        max_population (int): Indica la población máxima, si se deja en None no hay población máxima
        size (int): Indica la población actual

    Métodos:
        add_solution(solution)
        best_solution()
        initizalize_random(problem, sol_generator, max_population)
        print()

    """
    def __init__(self, max_population = None):
        self.solutions = []
        self.max_population = max_population
        self.size = 0

    def add_solution(self, solution):
        """
        Adds a given solution to the solutions list. Then it updates de size
        """
        if self.max_population:
            self.solutions.append(solution)
            self.size += 1
            return self.size
        else:
            raise Exception("Population is full.")

    def best_solution(self):
        """
        Returns the best solution from the population
        """
        if not self.solutions:
            raise Exception("There are none solutions.")

        return max(self.solutions, key = lambda s: s.value)

    def initialize_random(self, problem, sol_generator, max_population):
        """
        Initizalize a random population of individuals
        """
        self.solutions = []
        self.max_population = max_population

        for _ in range(max_population):
            # por cada posicion en la lista generemos una solucion baseline
            new_solution = sol_generator.baseline_solution(problem)
            self.solutions.append(new_solution)
            self.size += 1

    def __str__(self):
        # TODO, poner esto más bonito
        return f"There are {self.size} solutions in the population"
