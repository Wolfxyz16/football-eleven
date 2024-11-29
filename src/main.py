import time

from problem import Problem
from solution import Solution 
from solution_generator import SolutionGenerator
from neighborhood_generator import Neighborhood_generator
from neighborhood import Neighborhood
from local_search import local_search

laliga_reduced = Problem("players-reduced-laliga-2324.csv")
sg = SolutionGenerator()

random_sol = sg.random_solution(laliga_reduced)

random_sol.print()

neigh_generator = Neighborhood_generator(laliga_reduced)
neigh = Neighborhood(players = laliga_reduced.players, neighborhood_generator = neigh_generator)


solution = SolutionGenerator()

sol = local_search(problem = laliga_reduced, constructive_function = solution.random_solution, neighborhood = neigh, generation_type = 'random_search')

sol.print()