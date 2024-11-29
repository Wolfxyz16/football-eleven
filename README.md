# Football eleven

Este proyecto se trata de crear alineaciones de 11 jugadores de fútbol dado un determinado presupuesto máximo. De cada jugador tenemos su **id**, **nombre**, **equipo**, **rating** (su valor de media), **posición** y **coste** del fichaje. Contamos, en la versión reducida, con 492 jugadores de La Liga de la temporada 2023-2024.

## ¿Qué es Football Eleven?

*Football eleven* se trata de un programa que se encarga de encontrar la mejor alineación de futbolistas de una temporada. Utilizaremos diferentes métodos heurísticos como búsquedas locales, búsquedas genéticas, etc.

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
│   ├── genetic
│   │   └── genetic.py
│   ├── local_search
│   │   ├── neighbourhood_generator.py
│   │   └── neighbourhood.py
│   ├── main.py
│   ├── problem.py
│   ├── solution_generator.py
│   └── solution.py
└─── tests
    ├── test_problem.py
    └── test.py
```

Dentro de la carpeta `tests` se encuentran los tests que aseguran el correcto funcionamiento del proyecto. Cada archivo de test asegura una funcionalidad concreta del proyecto estando está indicada en su nombre. Por ejemplo, el archivo `test_problem.py` se encarga de asegurar la funcionalidad de la clase `Problem` que se encuentra en el archivo `src/problem.py`. Para hacer una comprobación del funcionamiento general del proyecto ejecutar el archivo `test.py`.

Dentro de la carpeta `src` se encuentran los archivos donde ejecutamos la lógica del proyecto. 

## Finalidad

Programa creado por alumnos de la EHU/UPV para la asignatura de *heurísticos de búsqueda*.

- David Laguillo Alonso

- Ander Amigorena Montes

- Sergio Hernández Redondo

- [Yeray Li Loaiza](https://github.com/Wolfxyz16)
