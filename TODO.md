- [ ] `main.py` linea 72, implementar en el menú algún método para cargar el dataset que querramos
- [ ] ¿Qué le pasa al método `solution_generator.baseline_solution`? No funciona :(
- [ ] Problema multiobjetivo. Minimizar dinero y maximizar el rating
    - [ ] Incluir algún algoritmo multiobjetivo
- [ ] Incluir tests para el correcto funcionamiento del código
- [ ] Optimizar nuestro hiperparámetros con Optuna. Del algoritmo genético por ejemplo.
- [ ] Utilizar `numpy` para mejorar el rendimiento
- [ ] Implementar más búsquedas locales
    - [ ] *simulated annealing*
    - [ ] *hill climbing*
- [X] Dentro del dataset de `players-2324.csv` existen jugadores que no tienen un precio y tampoco tienen una posicion asignada. Esto conlleva a que cuando cargamos este dataset y realizamos alguna búsqueda o algoritmo genético, peta porque lee un NaN. Tenemos que sanear el `csv` y eliminar a estos jugadores.
