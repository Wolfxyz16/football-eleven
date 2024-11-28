# Formalización del problema (PEAS)

Este proyecto se trata de crear alineaciones de 11 jugadores de fútbol dado un determinado presupuesto máximo. De cada jugador tenemos su **id**, **nombre**, **equipo**, **rating** (su valor de media), **posición** y **coste** del fichaje. Contamos, en la versión reducida, con 492 jugadores de La Liga de la temporada 2023-2024.

## Estructura del proyecto

```
.
├── data
│   ├── players-2324.csv
│   ├── players-laliga-2324.csv
│   ├── players-premier-2324.csv
│   ├── players-reduced-2324.csv
│   └── players-reduced-laliga-2324.csv
├── README.md
├── src
│   ├── main.py
│   ├── neighbourhood.py
│   ├── problem.py
│   ├── __pycache__
│   │   ├── problem.cpython-312.pyc
│   │   ├── solution.cpython-312.pyc
│   │   └── solution_generator.cpython-312.pyc
│   ├── solution_generator.py
│   └── solution.py
└── tests
    ├── test_problem.py
    └── test.py
```

Dentro de la carpeta `src` se encuentran los archivos donde ejecutamos la lógica del proyecto. 
