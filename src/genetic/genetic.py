# src/genetic/genetic.py

import heapq
import random
from population import Population
from solution import Solution

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

    return [offspring1, offspring2]

def simple_crossover(lineup1, lineup2, problem):
    """
    Devuelve un hijo mezclando las dos soluciones
    """
    new_lineup = []
    combined = [*lineup1, *lineup2]

    # Separar porteros
    goalkeepers = [player for player in combined if player['position'] == 'G']
    assert len(goalkeepers) == 2, "Debe haber exactamente dos porteros en los equipos iniciales."
    
    new_lineup.append(random.choice(goalkeepers))
    combined = [player for player in combined if player['position'] != 'G']

    # Mezclamos los jugadores
    random.shuffle(combined)

    for player in combined:
        if player not in new_lineup and len(new_lineup) < 11:
            new_lineup.append(player)

    offspring = Solution(new_lineup, problem.objective_function(new_lineup))

    return [offspring]


def manager_crossover(lineup1, lineup2, problem):
    """
    Crea (una o dos) soluciones intentando mantener un mínimo de sentido a la hora de generar los hijos.
    """
    new_lineup1 = []
    new_lineup2 = []

    combined = [*lineup1, *lineup2]

    # Separar porteros
    goalkeepers = [player for player in combined if player['position'] == 'G']
    assert len(goalkeepers) == 2, "Debe haber exactamente dos porteros en los equipos iniciales."
    
    new_lineup1.append(goalkeepers.pop())
    new_lineup2.append(goalkeepers.pop())
    combined = [player for player in combined if player['position'] != 'G']

    # Mezclamos los jugadores
    random.shuffle(combined)

    # Asignar jugadores a los equipos
    for player in combined:
        if player not in new_lineup1 and len(new_lineup1) < 11:
            new_lineup1.append(player)
        elif player not in new_lineup2 and len(new_lineup2) < 11:
            new_lineup2.append(player)

    # Asegurarnos de que ambos equipos tienen 11 jugadores
    assert len(new_lineup1) == 11 and len(new_lineup2) == 11, (
        f"Error en la asignación: lineup1={len(new_lineup1)}, lineup2={len(new_lineup2)}"
    )

    # Crear soluciones
    offspring1 = Solution(new_lineup1, problem.objective_function(new_lineup1))
    offspring2 = Solution(new_lineup2, problem.objective_function(new_lineup2))

    return [offspring1, offspring2]

def genetic_algorithm(problem, sol_gen, gen = 100000):
    import heapq
    import random

    # Constantes
    MAX_POPULATION = 1000
    MUTANT_PROB = 0.1

    # Creamos una poblacion inicial y las evaluamos
    pop = Population()
    pop.initialize_random(problem, sol_gen, MAX_POPULATION)

    for gen_no in range(gen):
        # Criterio de seleccion
        threshold = int(MAX_POPULATION * 0.1)
        pop_selected = truncation_selection(pop, threshold)

        # Creamos una poblacion de hijos
        offsprings = Population(max_population = threshold * 2)

        # Cruce y mutacion
        for parent1, parent2 in zip(pop_selected[::2], pop_selected[1::2]):
            childs = simple_crossover(parent1.lineup, parent2.lineup, problem)

            # Lanzamos un dado para ver si tenemos que mutar
            if random.random() > MUTANT_PROB:
                for child in childs:
                    problem.mutate_same_position_solution(child)

            for child in childs:
                offsprings.add_solution(child)

        # Reemplazo, elegimos las mejores soluciones entre padres e hijos
        comb = pop.solutions + offsprings.solutions
        pop.solutions = heapq.nlargest(MAX_POPULATION, comb)

        if gen_no % 10000 == 0:
            print(f"Iteracion {gen_no}")

    print(pop)

    # print("BEST SOLUTIONS")
    # pop.solutions[0].print()
    # pop.solutions[1].print()
    # pop.solutions[2].print()

    return pop.best_solution()
