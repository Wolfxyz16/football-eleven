from problem import Problem
from solution import Solution
from neighborhood import Neighborhood

def local_search(problem, constructive_function, neighborhood, generation_type, max_iterations = 20):
    solution = constructive_function(problem)
    neighborhood.set_current_solution(solution)
    local_optima = False
    mejor_encontrado = False
    i = 0
    while i < max_iterations and not(local_optima):
        neighboors = neighborhood.get_neighborhood(solution, generation_type)
        for elem in neighboors:
            if elem.value > solution.value:
                solution = elem
                mejor_encontrado = True
                solution.print()
                neighborhood.set_current_solution(solution)
                break
        if len(neighborhood.no_visitados) == 0 and not(mejor_encontrado):
            local_optima = True
        else:
            mejor_encontrado = False
    return solution
        

            

