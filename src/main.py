import time

from problem import Problem
from solution import Solution 
from solution_generator import SolutionGenerator
from genetic.genetic import genetic_algorithm
from multiobjective.nsga2 import nsga2
from local_search.hill_climbing import HillClimbing
from local_search.simulated_annealing import simulated_annealing
from local_search.neighbourhood_generator import NeighbourhoodGenerator

# TODO: mover este método a otro archivo src/utils.py
def perfomance(problem, sg):
    max = 100000
    # Random solution
    print("Measure random solution generator perfomance ...")
    suma = 0

    inicio = time.time()

    for i in range(max):
        solucion = sg.random_solution(problem)
        suma += problem.objective_function(solucion.lineup)

    fin = time.time()

    tiempo_transcurrido = fin - inicio
    print(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} seconds")
    print(f"Calidad media de las soluciones: {round(suma / max, 2)}\n")

    # Baseline solution
    print("Measuring baseline solution generator perfomance ...")
    suma = 0

    inicio = time.time()

    for i in range(max):
        solucion = sg.baseline_solution(problem)
        suma += problem.objective_function(solucion.lineup)

    fin = time.time()

    tiempo_transcurrido = fin - inicio
    print(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} seconds")
    print(f"Calidad media de las soluciones: {round(suma / max, 2)}\n")


greeting = """
███████  ██████   ██████  ████████ ██████   █████  ██      ██          ███████ ██      ███████ ██    ██ ███████ ███    ██ 
██      ██    ██ ██    ██    ██    ██   ██ ██   ██ ██      ██          ██      ██      ██      ██    ██ ██      ████   ██ 
█████   ██    ██ ██    ██    ██    ██████  ███████ ██      ██          █████   ██      █████   ██    ██ █████   ██ ██  ██ 
██      ██    ██ ██    ██    ██    ██   ██ ██   ██ ██      ██          ██      ██      ██       ██  ██  ██      ██  ██ ██ 
██       ██████   ██████     ██    ██████  ██   ██ ███████ ███████     ███████ ███████ ███████   ████   ███████ ██   ████ 
"""

draw = """
  ___________________________
 |             |             |
 |___          |          ___|
 |_  |         |         |  _|
.| | |.       ,|.       .| | |.
|| | | )     ( | )     ( | | ||
'|_| |'       `|'       `| |_|'
 |___|         |         |___|
 |             |             |
 |_____________|_____________|
"""

# presentacion
print(greeting)
print(draw)
print("a football lineup simulation.")

print()

# [TODO]
# cargamos los datos reducidos de la liga pero deberiamos preguntarle al usuario que datos quiere cargar
# tenemos que imprimir los archivos del directorio data y luego preguntarle al usuario cual quiere usar [premier o la liga]

problem = Problem("players-reduced-laliga-2324.csv")
# problem = Problem("players-2324-good.csv")
sg = SolutionGenerator()

hc = HillClimbing(problem)
neigh_generator = NeighbourhoodGenerator.all_random_neighborhood

solution = sg.random_solution(problem)

# bucle principal
while True:
    print("What do you want to do?")
    print('='*80)
    print("[0] -> Print last solution")
    print('='*80)
    print(f"[1] -> Change max budget. (current {problem.max_presupuesto}€)")
    print("[2] -> Get a random solution")
    print("[3] -> Get a baseline solution")
    print('='*80)
    print("[4] -> Run a HillClimbing")
    print("[5] -> Run a Simulated annealing")
    print('='*80)
    print("[6] -> Run a genetic algorithm")
    print("[7] -> Run a multiobjective algorithm (nsga2)")
    print('='*80)
    print("[8] -> Solution generator perfomance")
    print("[9] -> Exit")

    try:
        option = int(input("Type an option: "))
        print()
    except ValueError:
        print("Error, not an option!\n")
        continue

    if option == 0: # print las solution
        if solution: 
            solution.print()

    elif option == 1:
        user_input = input("Ingresa un número natural: ")
        if user_input.isdigit():  # Verifica si la entrada es un número natural (sin signo negativo)
            number = int(user_input)
            if number >= 0:
                problem.max_presupuesto = number
            else:
                print("El número debe ser natural (mayor o igual a 0). Intenta de nuevo.")
        else:
            print("Entrada no válida. Debes ingresar un número natural. Intenta de nuevo.\n")

    elif option == 2: # Print a random solution
        solution = sg.random_solution(problem)
        solution.print()

    elif option == 3: # Print a baseline solution
        solution = sg.random_solution(problem)
        solution.print()

    elif option == 4: # HillClimbing
        solution = hc.best_first(solution, neigh_generator)
        solution.print()

    elif option == 5: # SimulatedAnnealing
        solution = simulated_annealing(solution, problem, neigh_generator)
        solution.print()

    elif option == 6: # Genetic alg
        inicio = time.time()
        solution = genetic_algorithm(problem, sg)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} seconds")

    elif option == 7: # NSGA2
        inicio = time.time()
        solution = nsga2(problem, sg)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} seconds")

    elif option == 8:
        perfomance(problem, sg)

    elif option == 9 or option == 'exit':
        print("Goodbye!")
        exit()
    else:
        print("Please, choose a valid option\n")

print("Goodbye!")
