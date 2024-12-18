# src/solution.py

class Solution:
    """
    Clase Solution que representa una alineación de once jugadores. La solución debe de tener un valor de la función objetivo.

    Atributos:
        lineup (list):          Lista de diccionarios con once jugadores pertenecientes a la alineacion
        value (int):            Valor que le da la función objetivo.
        rating_sum (int):       Suma de las notas de la alineación.
        rating_mean (float):    Media de las notas de la alineación.
        cost (int):             Indica cuánto dinero (€) cuesta la plantilla.

    Métodos:
        print():            Imprime en forma de tabla la solución.
        short_print():      Imprime en forma comprimida
        change_players(current_player, new_player):   Recibe un jugador de la solución y lo cambia por el nuevo jugador.
    """

    def __init__(self, lineup, value):
        self.lineup = lineup
        self.value = value
        self.rating_sum = 0
        self.rating_mean = 0
        self.cost = 0

        for player in lineup:
            self.rating_sum += player["rating"]
            self.cost += player["value"]

        self.rating_mean = self.rating_sum / 11

    def change_players(current_player, new_player):
        """
             
        """
        pass


    def print(self):
        """
        Imprime en formato de tabla una solución, mostrando su nombre, nota, posición, precio y equipo

        Args:
            solution (list): Los ids de los jugadores que forman parte de la solución
            players (list): Estadísticas de todos los jugadores
        """

        orden = ['G', 'D', 'M', 'F']

        solution = sorted(self.lineup, key = lambda x: orden.index(x['position']))

        formacion = {'G': 0, 'D': 0, 'M': 0, 'F': 0}

        coste = 0
        nota = 0
        print('-' * 88)
        print(f"| {'NOMBRE':^30} | {'NOTA':^4} | {'POS':^3} | {'PRECIO € ':^15} | {'EQUIPO':^20} |")
        print('-' * 88)

        for player in solution:
            coste += player["value"]
            nota += player["rating"]
            formacion[player["position"]] += 1
            print(f'| {player["name"]:^30} | {player["rating"]:^4} | {player["position"]:^3} | {player["value"]:^15,} | {player["team"]:^20} |')

        print('-' * 88)
        print(f'Coste total de la plantilla {self.cost:,} €')
        print(f'Media de la plantilla {round(self.rating_mean, 2)}')
        print(f'VALOR de la plantilla {round(self.value, 2)}')
        print(f'Formación: {formacion["D"]}-{formacion["M"]}-{formacion["F"]}  \n')

    def short_print(self):
        """
        Imprime de manera comprimida para mostrar solo los id y la función objetivo
        """
        
        print("[ ", end = '')

        for player in self.lineup:
            print(player['id'], end = " ")

        print(']')

        print(f"value: {round(self.value, 2)}")
