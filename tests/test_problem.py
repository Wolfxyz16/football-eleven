# test/test_problem.py

from src.problem import Problem

# Simulamos datos para hacer los tests
test_players = [

    # Coste total de la plantilla 63,259,999 €
    # Media de la plantilla 6.93
    # VALOR de la plantilla 76.25
    # Formación: 4-3-3  

    {'id': 18, 'name': 'inaki-pena', 'team': 'barcelona', 'rating': 6.64, 'position': 'G', 'value': 7300000},
    {'id': 175, 'name': 'julian-araujo', 'team': 'las-palmas', 'rating': 6.99, 'position': 'D', 'value': 8199999},
    {'id': 394, 'name': 'alvaro-lemos', 'team': 'las-palmas', 'rating': 6.58, 'position': 'D', 'value': 735000},
    {'id': 144, 'name': 'adria-pedrosa', 'team': 'sevilla', 'rating': 6.89, 'position': 'D', 'value': 5800000},
    {'id': 443, 'name': 'jesus-vazquez', 'team': 'valencia', 'rating': 6.58, 'position': 'D', 'value': 4200000},
    {'id': 373, 'name': 'jonathan-viera', 'team': 'almeria', 'rating': 7.17, 'position': 'M', 'value': 725000},
    {'id': 382, 'name': 'omar-mascarell', 'team': 'mallorca', 'rating': 6.66, 'position': 'M', 'value': 1000000},
    {'id': 280, 'name': 'isco', 'team': 'real-betis', 'rating': 7.52, 'position': 'M', 'value': 8300000},
    {'id': 137, 'name': 'raul-de-tomas', 'team': 'rayo-vallecano', 'rating': 6.73, 'position': 'F', 'value': 1100000},
    {'id': 321, 'name': 'iago-aspas', 'team': 'celta-vigo', 'rating': 7.54, 'position': 'F', 'value': 2900000},
    {'id': 440, 'name': 'youssef-en-nesyri', 'team': 'sevilla', 'rating': 6.95, 'position': 'F', 'value': 23000000},
]

class MockProblem(Problem):
    def read_players(self, filename):
        self.players = test_players
        self.total_players = len(self.players)

def test_read_players():
    problem = MockProblem("")
    assert problem.total_players == 11, "Test failed, error reading the number of players"
    assert problem.players[0]["name"] == "inaki-pena", "Test failed, first player name mismatch"

def test_objective_function():
    problem = MockProblem("")
    solution = test_players
    assert problem.objective_function(solution) > 0, "Test failed, wrong objective function"

def test_get_random_player():
    problem = MockProblem("")
    player = problem.get_random_player()
    assert player in test_players, "Test failed, random player not generated or not in the database"

if __name__ == "__main__":
    test_read_players()
    test_objective_function()
    test_get_random_player()
