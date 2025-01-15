from src.problem import Problem
from src.solution import Solution
from src.solution_generator import SolutionGenerator
from src.local_search.neighbourhood_generator import NeighbourhoodGenerator
import numpy as np
import random

class HillClimbing():
    def __init__(self, generation_type, problem, initial_solution, num_iterations = 1000):
        '''
        Params:
            problem: Objeto de la clase problem
            initial_solution: Solución inicial por donde se empezará la búsqueda local
            neighborhood_generator: generador de vecindarios de la clase NeighborhoodGenerator
            generarion_type: Tipo de generación ('same_position, random')
        '''
        self.problem = problem
        self.initial_solution = initial_solution
        self.neighborhood_generator = NeighbourhoodGenerator()
        self.__set_generation(generation_type)
        self.num_iterations = num_iterations
    def __set_generation(self, generation_type):
        if generation_type == 'same_position':
            self.generation = self.neighborhood_generator.neighbourhood_same_position
        elif generation_type =='random':
            self.generation = self.neighborhood_generator.all_random_neighborhood
        else:
            raise NameError(f'El nombre {generation_type} no es válido. Nombres válidos same_position o random')

    def change_initial_solution(self, initial_solution):
        self.initial_solution = initial_solution
    def change_generation_type(self, generation_type):
        self.__set_generation(generation_type)

    def best_first(self):
        '''

        Returns:
            Mejor solución con mejor valor de función objetibo obtenido
        '''
        current_sol = self.initial_solution
        i = 0
        for i in range(self.num_iterations):
            better_find = False
            for neighbors in self.generation(current_sol, self.problem):
                for sol in neighbors:
                    if sol.value > current_sol.value:
                        current_sol = sol
                        current_sol.update_solution()
                        better_find = True
                        break
                if better_find:
                    break
            if not better_find:
                break
        return current_sol

    def greedy(self):
        current_sol = self.initial_solution
        best_sol = self.initial_solution
        for i in range(self.num_iterations):
            better_find = False
            for neighbors in self.generation(current_sol, self.problem):
                for sol in neighbors:
                    if sol.value > best_sol.value:
                        best_sol = sol
                        best_sol.update_solution()
                        better_find = True

            if not better_find:
                break
            else:
                current_sol = best_sol
        return current_sol







