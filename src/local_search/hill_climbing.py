from problem import Problem
from solution import Solution
from solution_generator import SolutionGenerator
import numpy as np
import random

class HillClimbing():
    def __init__(self, problem, num_iterations = 1000):
        '''
        Params:
            problem: Objeto de la clase problem
            initial_solution: Solución inicial por donde se empezará la búsqueda local
            neighborhood_generator: generador de vecindarios de la clase NeighborhoodGenerator
            generarion_type: Tipo de generación ('same_position, random')
        '''
        self.problem = problem
        self.num_iterations = num_iterations

    def best_first(self, initial_solution, generator):
        '''
        Returns:
            Mejor solución con mejor valor de función objetibo obtenido
        '''
        current_sol = initial_solution
        i = 0
        for i in range(self.num_iterations):
            better_find = False
            for neighbors in generator(None, current_sol, self.problem):
                for sol in neighbors:
                    if sol.value > current_sol.value:
                        current_sol = sol
                        better_find = True
                        break
                if better_find:
                    break
            if not better_find:
                break
        return current_sol

    def greedy(self, initial_solution, generator):
        current_sol = initial_solution
        best_sol = initial_solution
        for i in range(self.num_iterations):
            better_find = False
            for neighbors in generator(None, current_sol, self.problem):
                for sol in neighbors:
                    if sol.value > best_sol.value:
                        best_sol = sol
                        better_find = True

            if not better_find:
                break
            else:
                current_sol = best_sol
        yield current_sol

