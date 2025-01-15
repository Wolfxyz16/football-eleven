from src.problem import Problem
from src.solution_generator import SolutionGenerator
from src.local_search.neighbourhood_generator import NeighbourhoodGenerator
from src.local_search.hill_climbing import HillClimbing
from src.local_search.simulated_annealing import simulated_annealing

problem = Problem('players-reduced-laliga-2324.csv')
sg = SolutionGenerator()

initial_solution = sg.random_solution(problem)
initial_solution.short_print()

hill_climbing = HillClimbing(generation_type='random', problem=problem, initial_solution=initial_solution)

greedy_solution = hill_climbing.greedy()
greedy_solution.short_print()

best_first_solution = hill_climbing.best_first()
best_first_solution.short_print()

sa_solution = simulated_annealing(initial_solution= initial_solution, problem=problem, num_iterations=1000, generation_type='random')
sa_solution.short_print()

sa_solution.print()
