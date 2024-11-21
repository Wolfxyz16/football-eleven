import time

from problem import Problem
from solution import Solution 
from solution_generator import SolutionGenerator

laliga_reduced = Problem("players-reduced-laliga-2324.csv")
sg = SolutionGenerator()

random_sol = sg.random_solution(laliga_reduced)

random_sol.print()
