import random
from src.local_search.neighbourhood_generator import NeighbourhoodGenerator
import math as mt


def simulated_annealing(initial_solution, problem, num_iterations, generation_type, cool_rate = 0.95, temp = 1000):
    neighbourhood_generator = NeighbourhoodGenerator()
    if generation_type == 'random':
        generation = neighbourhood_generator.all_random_neighborhood
    elif generation_type == 'same_position':
        generation = neighbourhood_generator.neighbourhood_same_position
    else:
        raise NameError(f'El nombre {generation_type} no es válido. Nombres válidos same_position o random')

    current_sol = initial_solution
    best_sol = initial_solution
    for i in range(num_iterations):
        find = False
        for neighbors in generation(current_sol, problem):
            for sol in neighbors:
                energy = sol.value - current_sol.value
                if energy > 0 or random.uniform(0, 1) < mt.exp(energy/temp):
                    current_sol = sol
                    find = True
                    if best_sol.value < current_sol.value:
                        best_sol = current_sol
                    break
            if find:
                break
        temp *= cool_rate
        if not find:
            break
    return best_sol




