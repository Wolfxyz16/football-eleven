import random
from local_search.neighbourhood_generator import NeighbourhoodGenerator
import math as mt

def simulated_annealing(initial_solution, problem, generator, num_iterations = 100000, cool_rate = 0.95, temp = 1000):
    current_sol = initial_solution
    best_sol = initial_solution
    for i in range(num_iterations):
        find = False
        for neighbors in generator(None, current_sol, problem):
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




