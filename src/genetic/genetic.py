# src/genetic/genetic.py

import heapq
import random
from population import Population
from solution import Solution

# Constantes
MAX_POPULATION = 10000
MUTANT_PROB = 0.1

def truncation_selection(pop, threshold):
    """
    Se eligen los k mejores individuos de la poblacion. Se devuelven los índices de los individuos seleccionados
    """
    assert isinstance(threshold, int) and threshold >= 0
    return heapq.nlargest(threshold, pop.solutions)
    
def one_point_crossover(lineup1, lineup2, problem):
    """
    Devuelve dos hijos (objetos solution) aplicando el one-point crossover. Necesitamos el objeto problem para evaluar a las soluciones hijas
    que creamos.

    Se podría mejorar este crossover para que tuviese en cuenta por lo menos el mantener una buena estructura del equipo o mantener un portero
    """
    point = 5

    new_lineup1 = lineup1[:point] + lineup2[:point]
    new_lineup2 = lineup2[:point] + lineup1[:point]

    offspring1 = Solution(new_lineup1, problem.objective_function(new_lineup1))
    offspring2 = Solution(new_lineup2, problem.objective_function(new_lineup2))

    return offspring1, offspring2

def manager_crossover(lineup1, lineup2, problem):
    """
    [TODO]
    Crea (una or dos) solucion(es) intentando mantener un mínimo de sentido a la hora de generar los hijos
    """
    pass

def genetic_algorithm(problem, sol_gen, gen = 100000):
    import heapq
    import random
    # Creamos una poblacion inicial y las evaluamos
    pop = Population()
    pop.initialize_random(problem, sol_gen, MAX_POPULATION)

    for _ in range(gen):
        # Criterio de seleccion
        threshold = int(MAX_POPULATION * 0.1)
        pop_selected = truncation_selection(pop, threshold)

        # Creamos una poblacion de hijos
        offsprings = Population(max_population = threshold * 2)

        # Cruce y mutacion
        for parent1, parent2 in zip(pop_selected[::2], pop_selected[1::2]):
            offspring1, offspring2 = one_point_crossover(parent1.lineup, parent2.lineup, problem)

            # Lanzamos un dado para ver si tenemos que mutar
            if random.random() > MUTANT_PROB:
                problem.mutate_same_position_solution(offspring1)
                problem.mutate_same_position_solution(offspring2)

            offsprings.add_solution(offspring1)
            offsprings.add_solution(offspring2)

        # Reemplazo, elegimos las mejores soluciones entre padres e hijos
        comb = pop.solutions + offsprings.solutions
        pop.solutions = heapq.nlargest(MAX_POPULATION, comb)

    print(pop)
    return pop.best_solution()
