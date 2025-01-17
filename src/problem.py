# src/problem.py 

class Problem:
    """
    Objeto de la clase problema que contiene diversos atributos y métodos útiles a la hora de implementar las búsquedas heurísticas

    Atributos:
        players (list):                 Contiene los jugadores con sus estadísticas

    Métodos:
        read_players(filename):         Lee el archivo con el nombre filename y carga los jugadores
        objective_function(solution):   Dada una solución devuelve el valor que le da.
        get_random_player():            Devuelve un jugador aleatorio de su base de jugadores
        mutate_solution(solution):      Dada una solucion muta un jugador aleatorio por otro de su posición
    """

    import random
    import pandas as pd
    
    def __init__(self, filename):
        self.filename = filename
        self.players = []
        self.max_presupuesto = 100000000
        self.read_players(filename)
        self.total_players = len(self.players)

    def read_players(self, filename):
        """
        Lee un archivo de la carpeta data y carga los jugadores en la lista players

        Args:
            filename (str): Nombre del archivo que queremos cargar
        
        Files:
            players-2324.csv
            players-laliga-2324.csv
            players-reduced-laliga-2324.csv
            players-premier-2324.csv
            players-reduced-premier-2324.csv
        """
        df = self.pd.read_csv(f"data/{filename}")
        self.players = df.to_dict(orient = "records")

    def get_team_price(self, solution):
        """
        Devuelve el costo total de la plantilla
        """
        return sum(player['value'] for player in solution.lineup)


    def get_team_rating(self, solution):
        """
        Devuelve la media de la valoracion de la alineacion
        """
        return ( sum(player['rating'] for player in solution.lineup) / 11 )

    def objective_function(self, solucion):
        """
        Calcula la media de las notas de los jugadores de la posicion y si nos hemos pasado del presupuesto máximo sufrimos
        una penalización.

        Args:
            solution (list): Lista de los jugadores (diccionarios) que forman parte de la solución
            
        Returns:
            suma_nota (int): Puntuación que tiene la solución dada
        """

        # El orden de las posiciones en G -> D -> M -> F
        contador_posiciones = {'G': 0, 'D': 0, 'M': 0, 'F': 0}
        suma_presupuesto = 0
        suma_nota = 0

        for player in solucion:
            # Sumamos al contador dependiendo de la posicion del jugador
            contador_posiciones[player['position']] += 1

            suma_presupuesto += player['value']
            suma_nota += player['rating']

        # Después del for penalizamos por no tener los jugadores adecuados
        if contador_posiciones['G'] != 1:
            # Tenemos más de uno o cero porteros
            suma_nota = suma_nota * 0.1
        elif contador_posiciones['D'] < 3 or contador_posiciones['D'] > 5:
            # Tenemos demasiados o insuficientes defensas
            suma_nota = suma_nota * 0.3
        elif contador_posiciones['M'] < 2 or contador_posiciones['M'] > 5:
            # Tenemos demasiados o insuficientes mediocentros
            suma_nota = suma_nota * 0.3
        elif contador_posiciones['F'] < 1 or contador_posiciones['F'] > 5:
            # Tenemos demasiados o insuficientes delanteros
            suma_nota = suma_nota * 0.3

        # Si nos hemos pasado del presupuesto penalizamos con la parte proporcional que nos hemos pasado
        if suma_presupuesto > self.max_presupuesto:
            suma_nota = suma_nota + (100 - ( suma_presupuesto * 100 / self.max_presupuesto))

        return suma_nota

    def get_random_player(self):
        """
        Devuelve un jugador aleatorio de toda la lista de jugadores

        Returns:
            Un diccionario que representa al jugador elegido
        """

        # Comprobamos que existan jugadores
        if len(self.players) == 0: 
            raise Exception("Players list is empty.")

        id = self.random.randint(0, self.total_players - 1)

        return self.players[id]

    def mutate_same_position_solution(self, solution):
        """
        Dada una solución cambia un jugador aleatorio por otro de la misma posicion
        """
        encontrado = False

        # Es el jugador que tendremos que sustituir
        banquillo = solution.get_random_player()

        # Buscamos un jugador aleatorio de su misma posicion
        while not encontrado:
            new_player = self.get_random_player()
            # si comparten posicion y el nuevo jugador no esta en la solucion
            if new_player['position'] == banquillo['position'] and new_player not in solution.lineup:
                solution.change_players(banquillo, new_player)
                encontrado = True

