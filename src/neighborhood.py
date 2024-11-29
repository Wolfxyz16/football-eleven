from solution import Solution
class Neighborhood:
    def __init__(self, neighborhood_generator, players):
        self.num_total_players = len(players)
        self.no_visitados = []
        self.players = players

        self.neighborhood_generator = neighborhood_generator
        self.neighborhood_generator.set_neighborhood(self)

        self.current_solution = []

    def set_current_solution(self, solution):
        self.current_solution = solution
        self.reiniciar_vecindario(solution = solution.lineup)

    def reiniciar_vecindario(self, solution = []):
        self.no_visitados = list(range(0, self.num_total_players))
        for jugadores in solution:
            self.no_visitados.remove(jugadores['id'])

    def borrar_elemento_visitado(self, player):
        self.no_visitados.remove(player)

    def get_neighborhood(self, solution, generation_type):
        if(len(self.no_visitados) > 0):
            generation = getattr(self.neighborhood_generator, generation_type)
            neighboors, player =  generation(solution.lineup, self.no_visitados)
            print("player: ", player)
            self.borrar_elemento_visitado(player)
            print(self.no_visitados)
            return neighboors
        else:
            print("error, todos los vecios han sido seleccionados")