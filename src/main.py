import time

from problem import Problem
from solution import Solution 
from solution_generator import SolutionGenerator
from genetic.genetic import genetic_algorithm

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

print('=' * 80)

# [TODO]
# cargamos los datos reducidos de la liga pero deberiamos preguntarle al usuario que datos quiere cargar
# tenemos que imprimir los archivos del directorio data y luego preguntarle al usuario cual quiere usar [premier o la liga]

# problem = Problem("players-reduced-laliga-2324.csv")
problem = Problem("players-2324-good.csv")
sg = SolutionGenerator()
solution = None

# bucle principal
while True:
    print("What do you want to do?")
    print("[0] -> Print last solution")
    print("[1] -> Get a random solution")
    print("[2] -> Get a baseline solution")
    print("[3] -> Solution generator perfomance")
    print("[4] -> Run a genetic algorithm")
    print("[9] -> Exit")

    try:
        option = int(input("Type an option: "))
    except ValueError:
        print("Error, not an option!\n")
        continue

    if option == 0: # print las solution
        if solution: 
            solution.print()

    if option == 1: # Print a random solution
        solution = sg.random_solution(problem)
        solution.print()

    elif option == 2: # Print a baseline solution
        solution = sg.random_solution(problem)
        solution.short_print()

    elif option == 3:
        perfomance(problem, sg)

    elif option == 4:
        inicio = time.time()
        solution = genetic_algorithm(problem, sg, gen = 1000)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} seconds")

    elif option == 9 or option == 'exit':
        print("Goodbye!")
        exit()
    else:
        print("Please, choose a valid option\n")

print("Goodbye!")
