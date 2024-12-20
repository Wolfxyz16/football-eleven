# src/genetic/genetic.py

from src.population import Population
from src.problem import Problem
import heapq
import random

# Constantes
MAX_POPULATION = 10
MUTANT_PROB = 0.1

def truncation_selection(pop, threshold):
    """
    Se eligen los k mejores individuos de la poblacion. Se devuelven los índices de los individuos seleccionados
    """
    assert is_instance(threshold, int) and threshold >= 0
    return heapq.nlargest(threshold, pop.solutions)
    
def one_point_crossover(lineup1, lineup2, problem):
    """
    Devuelve dos hijos aplicando el one-point crossover. Necesitamos el objetivo problem para evaluar a las soluciones hijas
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
    Crea (una or dos) solucion(es) intentando mantener un mínimo de sentido a la hora de generar los hijos
    """
    pass


def mutate(lineup1):
    pass

def genetic_algorithm(problem, sol_gen):

    # Creamos una poblacion inicial y las evaluamos
    pop = Population()
    pop.initialize_random(problem, sol_gen, MAX_POPULATION)

    # Criterio de seleccion
    int(threshold) = MAX_POPULATION * 0.1
    pop_selected = truncation_selection(pop, threshold)

    # Cruce y mutacion
    for i in range(0, len(pop_selected), 2):
        offspring1, offspring2 = one_point_crossover(pop_selected[i].lineup, pop_selected[i+1].lineup)

        # Lanzamos un dado para ver si tenemos que mutar
        if random.random() > MUTANT_PROB:
            mutate()


    # Reemplazo
    
    # iteramos hasta un criterio
    while True:
    
        # Cruzamos los hijos
        while hijos < 10:
            # 1. Seleccionamos a dos padres
            # 2. Aplicamos el cruce
            # 3. Aplicamos la mutación
            # 4. Insertamos los nuevos hijos en la poblacion
            pass

        # Evaluamos la nueva poblacion

        # Seleccionamos la mejor poblacion

        # Devolvemos el mejor individuo
