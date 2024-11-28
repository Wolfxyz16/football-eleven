# Formalización del problema (PEAS)

Este proyecto se trata de crear alineaciones de 11 jugadores de fútbol dado un determinado presupuesto máximo. De cada jugador tenemos su **id**, **nombre**, **equipo**, **rating** (su valor de media), **posición** y **coste** del fichaje. Contamos, en la versión reducida, con 492 jugadores de La Liga de la temporada 2023-2024.

## Espacio de búsqueda y codificación de soluciones

### Codificación de soluciones

Las soluciones del problema las codificamos como vectores de 11 posiciones, con los 11 **ids** de los jugadores que formen la plantilla solución. 

$\sigma = [id_1, id_2, \dots, id_{11}]$, donde $id_k \in \{1, 2, \dots, 492\}$ y $id_i \neq id_j$ para $i \neq j$

Según esta codificación, pueden existir soluciones _poco realistas_ (tener 11 defensas, no tener portero, etc.), pero hemos decidido contarlas como soluciones válidas; ya que esto es algo que la función objetivo contempla y penaliza,  y tampoco hay una formación de defensas-mediocentros-delanteros única, así que de esta manera nos permitimos explorar muchas formaciones.

### Espacio de búsqueda/codificación

Como hemos comentado, contamos con **492 jugadores** y queremos formar plantillas de **11 jugadores**. Los jugadores no se pueden repetir y el orden de estos no importa, es decir, en cada solución habrá 11 jugadores distintos y una selección de 11 jugadores en cualquier orden es la misma solución. 

Teniendo esto en cuenta, la cantidad de soluciones posibles en el espacio de búsqueda es la cantidad de agrupaciones de 11 jugadores que podemos hacer de un conjunto de 492 jugadores, que  viene dada por la combinación: 

$$C(492, 11) = \binom{492}{11} = \frac{492!}{11!(492-11)!} = \frac{492 \cdot 491 \cdot 490 \cdot \dots \cdot 482}{11 \cdot 10 \cdot 9 \cdot \dots \cdot 1} = $$

$$= 9,152,972,082,554,198,651,676$$

Como vemos, es un número muy grande.

El espacio de codificación, como hemos comentado antes que no vamos a restringir la cantidad de posibles soluciones, es el mismo que el espacio de búsqueda; aunque dependiendo de la función de vecindario que usemos (tenemos varias implementadas y por ejemplo una se asegura que de haya mínimo un portero), habrá combinaciones de jugadores que no lleguemos a considerar como solución. Pero lo dicho, a priori, toda combinación es solución válida.

## Función objetivo

La función objetivo busca **maximizar** el rendimiento (rating) de un equipo de jugadores seleccionados. Para ello, se considera la combinación de la nota de los jugadores, el cumplimiento de los requisitos de posiciones y el presupuesto disponible.

### Definiciones:

### Conjuntos y variables:

- `S`: Conjunto de IDs de los jugadores seleccionados. Es la solución que buscamos optimizar.
- `players[i]`: Información del jugador `i` (posición, valor o nota).
- `P_i`: Posición del jugador `i`.
- `V_i`: Coste del jugador `i` (*value*).
- `R_i`: Rating del jugador `i` (*rating*).
- `max_presupuesto`: Presupuesto máximo disponible.

### Contadores de posiciones:

- **G**: Número de porteros seleccionados.
- **D**: Número de defensas seleccionados.
- **M**: Número de mediocampistas seleccionados.
- **F**: Número de delanteros seleccionados.

### Presupuesto y nota acumulados:

$suma\_presupuesto = \sum_{i \in S} V_i$

$suma\_nota = \sum_{i \in S} R_i$

### Penalizaciones:

#### Requisitos de posiciones:

Penalización por no cumplir con el número requerido de jugadores por posición:

$$ \text{penalización\_n\_posiciones} = \begin{cases} 0.1 & \text{si } G \neq 1 \\ 0.3 & \text{si } D < 3 \text{ o } D > 5 \\ 0.3 & \text{si } M < 2 \text{ o } M > 5 \\ 0.3 & \text{si } F < 1 \text{ o } F > 5 \\ 0 & \text{en caso contrario.} \end{cases} $$

El valor de la función objetivo se multiplica por $(1 - \text{penalización\_n\_posiciones})$.

#### Presupuesto excedido:

Penalización proporcional por exceso de presupuesto:

$$
\text{penalización\_n\_presupuesto} =
\begin{cases}
0 & \text{si } \text{suma\_presupuesto} \leq \text{max\_presupuesto} \\
100 - \left( \frac{\text{suma\_presupuesto} \times 100}{\text{max\_presupuesto}} \right) & \text{si } \text{suma\_presupuesto} > \text{max\_presupuesto}
\end{cases}
$$

### Fórmula final:

La función objetivo final se expresa como:

$$
\text{objective\_function}(S) = \left( \text{suma\_nota} \times (1 - \text{penalización\_n\_posiciones}) \right) + \text{penalización\_n\_presupuesto}
$$

Expresado en detalle:

$$
\text{objective\_function}(S) = \left( \sum_{i \in S} R_i \right) \times \left( 1 - \text{penalización\_n\_posiciones} \right) + 
\begin{cases}
0 & \text{si } \text{suma\_presupuesto} \leq \text{max\_presupuesto} \\
100 - \left( \frac{\text{suma\_presupuesto} \times 100}{\text{max\_presupuesto}} \right) & \text{si } \text{suma\_presupuesto} > \text{max\_presupuesto}
\end{cases}
$$

## Vecindarios
