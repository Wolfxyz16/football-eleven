# src/multiobjective/nsga2.py

import random
from problem import Problem
from population import Population
from genetic.genetic import one_point_crossover, manager_crossover

def dominate(sol1, sol2):
    """ Returns boolean indicating if the sol1 dominates over the sol2 """
    """ sol1 domina a sol2 si es mejor o igual en todas las soluciones y al menos en una estrictamente mejor """
    if sol1.cost >= sol2.cost and sol1.rating > sol2.rating:
        return True
    elif sol1.cost > sol2.cost and sol1.rating >= sol2.rating:
        return True
    else:
        return False

def sort_in_fronts(population, size):
    # Ordenamos las soluciones en las fronteras
    fronts = []
    # contador para saber dominancias entre soluciones
    cont = {}

    for i, sol1 in enumerate(population):
        cont[i] = 0
        for sol2 in population:
            # sol1 domina a sol2
            if dominate(sol2, sol1):
                cont[i] += 1
    
    # Ahora tenemos un diccionario donde indica cuantas veces es una solucion dominada
    # Tenemos que buscar las soluciones que tengan 0, esas seran las soluciones no dominadas
    procesed_solutions = 0
    while procesed_solutions < size:
        new_front = []
        for key, value in cont.items():
            if value == 0:
                new_front.append(population[key])
                procesed_solutions += 1
            else:
                value -= 1
        fronts.append(new_front)

    return fronts, cont

def calculate_distances(front):
    min_cost, max_cost = min(sol.cost for sol in front), max(sol.cost for sol in front)
    min_rating, max_rating = min(sol.rating for sol in front), max(sol.rating for sol in front)

    dif_cost = ( max_cost - min_cost ) 
    dif_rating = ( max_rating - min_rating ) 

    dif_cost = dif_cost if dif_cost != 0 else 1
    dif_rating = dif_rating if dif_rating != 0 else 1

    # Inicializamos las distancias de las soluciones a cero
    distances = [0.0] * len(front)
    distances[0] = distances[-1] = float('inf')

    for i in range(1, len(front) - 1):
        distances[i] += ( (front[i + 1].cost - front[i - 1].cost) / dif_cost )
        distances[i] += ( (front[i + 1].rating - front[i - 1].rating) / dif_rating )

    return distances

def selection(population):
    i1, i2 = random.sample(range(len(population.solutions)), 2)
    sol1 = population.solutions[i1]
    sol2 = population.solutions[i2]

    if dominate(sol1, sol2):
        return i1
    elif dominate(sol2, sol1):
        return i2
    # Estan en la misma frontera, deberiamos comprobar su crowding_distance
    else:
        return i1


def nsga2(problem, solution_generator):

    POP_SIZE = 100
    MAX_GEN = 50
    MUTANT_PROB = 0.1

    # Inicializamos la poblacion
    population = Population(max_population = POP_SIZE)
    population.initialize_random(problem, solution_generator, POP_SIZE)

    print(population)

    gen_no = 0
    while gen_no < MAX_GEN:
        # 1. Non dominated sorting
        fronts, cont = sort_in_fronts(population.solutions, POP_SIZE)

        # 2. Calculation of crowding distance
        distances = [calculate_distances(front) for front in fronts]

        # 3. Selection parents for crossover
        parents = [selection(population) for _ in range(int( POP_SIZE / 2 ))]
        # mezclamos los padres para que sea aleatorio
        random.shuffle(parents)

        # 4 Application of Crossover and Mutation Operators
        offsprings = []

        for index_parent1, index_parent2 in zip(parents[::2], parents[1::2]):
            parent1, parent2 = population.solutions[index_parent1], population.solutions[index_parent2]
            offspring1, offspring2 = manager_crossover(parent1.lineup, parent2.lineup, problem)

            # Lanzamos un dado para ver si tenemos que mutar
            if random.random() > MUTANT_PROB:
                problem.mutate_same_position_solution(offspring1)
                problem.mutate_same_position_solution(offspring2)

            offsprings.append(offspring1)
            offsprings.append(offspring2)

        # 5. Creation of next gen

        # juntamos a los hijos con los padres
        mix = [*population.solutions, *offsprings]

        fronts, cont = sort_in_fronts(mix, POP_SIZE)

        new_pop = Population(max_population = POP_SIZE)

        inserted = 0

        for clave in sorted(cont, key=cont.get):
            new_pop.add_solution(mix[clave])
            inserted += 1
            if inserted == POP_SIZE: break

        population = new_pop
        gen_no += 1

    population.best_solution().print()
