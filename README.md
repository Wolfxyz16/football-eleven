# Formalización del problema (PEAS)

Este proyecto se trata de crear alineaciones de 11 jugadores de fútbol
dado un determinado presupuesto máximo. De cada jugador tenemos su
**id**, **nombre**, **equipo**, **rating** (su valor de media),
**posición** y **coste** del fichaje. Contamos, en la versión reducida,
con 492 jugadores de La Liga de la temporada 2023-2024.

## Espacio de búsqueda y codificación de soluciones

### Codificación de soluciones

Las soluciones del problema las codificamos como vectores de 11
posiciones, con los 11 **ids** de los jugadores que formen la plantilla
solución.

[[[$\sigma = \lbrack id_{1},id_{2},\ldots,id_{11}\rbrack$]{.katex-mathml}[[[]{.strut
style="height: 0.43056em; vertical-align: 0em;"}[σ]{.mord .mathnormal
style="margin-right: 0.03588em;"}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 1em; vertical-align: -0.25em;"}[\[]{.mopen}[i]{.mord
.mathnormal}[[d]{.mord .mathnormal}[[[[[[]{.pstrut
style="height: 2.7em;"}[[1]{.mord .mtight}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.301108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[i]{.mord .mathnormal}[[d]{.mord
.mathnormal}[[[[[[]{.pstrut style="height: 2.7em;"}[[2]{.mord
.mtight}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.301108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[...]{.minner}[]{.mspace
style="margin-right: 0.166667em;"}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[i]{.mord .mathnormal}[[d]{.mord
.mathnormal}[[[[[[]{.pstrut style="height: 2.7em;"}[[[11]{.mord
.mtight}]{.mord .mtight}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.301108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[\]]{.mclose}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex--inline}, donde
[[[$id_{k} \in \{ 1,2,\ldots,492\}$]{.katex-mathml}[[[]{.strut
style="height: 0.84444em; vertical-align: -0.15em;"}[i]{.mord
.mathnormal}[[d]{.mord .mathnormal}[[[[[[]{.pstrut
style="height: 2.7em;"}[[k]{.mord .mathnormal .mtight
style="margin-right: 0.03148em;"}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.336108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[]{.mspace
style="margin-right: 0.277778em;"}[∈]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 1em; vertical-align: -0.25em;"}[{]{.mopen}[1]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[2]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[...]{.minner}[]{.mspace
style="margin-right: 0.166667em;"}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[492]{.mord}[}]{.mclose}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex--inline} y
[[[$id_{i} \neq id_{j}$]{.katex-mathml}[[[]{.strut
style="height: 0.88888em; vertical-align: -0.19444em;"}[i]{.mord
.mathnormal}[[d]{.mord .mathnormal}[[[[[[]{.pstrut
style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
.reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[]{.mspace
style="margin-right: 0.277778em;"}[[[[[[]{.strut
style="height: 0.88888em; vertical-align: -0.19444em;"}[[[]{.mrel}]{.mord}]{.inner}[]{.fix}]{.rlap}]{.thinbox}]{.mord
.vbox}]{.mrel}[=]{.mrel}]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 0.980548em; vertical-align: -0.286108em;"}[i]{.mord
.mathnormal}[[d]{.mord .mathnormal}[[[[[[]{.pstrut
style="height: 2.7em;"}[[j]{.mord .mathnormal .mtight
style="margin-right: 0.05724em;"}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.286108em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex--inline} para
[[[$i \neq j$]{.katex-mathml}[[[]{.strut
style="height: 0.88888em; vertical-align: -0.19444em;"}[i]{.mord
.mathnormal}[]{.mspace style="margin-right: 0.277778em;"}[[[[[[]{.strut
style="height: 0.88888em; vertical-align: -0.19444em;"}[[[]{.mrel}]{.mord}]{.inner}[]{.fix}]{.rlap}]{.thinbox}]{.mord
.vbox}]{.mrel}[=]{.mrel}]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 0.85396em; vertical-align: -0.19444em;"}[j]{.mord
.mathnormal style="margin-right: 0.05724em;"}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex--inline}

Según esta codificación, pueden existir soluciones *poco realistas*
(tener 11 defensas, no tener portero, etc.), pero hemos decidido
contarlas como soluciones válidas; ya que esto es algo que la función
objetivo contempla y penaliza, y tampoco hay una formación de
defensas-mediocentros-delanteros única, así que de esta manera nos
permitimos explorar muchas formaciones.

### Espacio de búsqueda/codificación

Como hemos comentado, contamos con **492 jugadores** y queremos formar
plantillas de **11 jugadores**. Los jugadores no se pueden repetir y el
orden de estos no importa, es decir, en cada solución habrá 11 jugadores
distintos y una selección de 11 jugadores en cualquier orden es la misma
solución.

Teniendo esto en cuenta, la cantidad de soluciones posibles en el
espacio de búsqueda es la cantidad de agrupaciones de 11 jugadores que
podemos hacer de un conjunto de 492 jugadores, que viene dada por la
combinación:

[[[[$$C(492,11) = \left( \frac{492}{11} \right) = \frac{492!}{11!(492 - 11)!} = \frac{492 \cdot 491 \cdot 490 \cdot \cdots \cdot 482}{11 \cdot 10 \cdot 9 \cdot \cdots \cdot 1} =$$]{.katex-mathml}[[[]{.strut
style="height: 1em; vertical-align: -0.25em;"}[C]{.mord .mathnormal
style="margin-right: 0.07153em;"}[(]{.mopen}[492]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[11]{.mord}[)]{.mclose}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 2.40003em; vertical-align: -0.95003em;"}[[[(]{.delimsizing
.size3}]{.mopen .delimcenter style="top: 0em;"}[[[[[[]{.pstrut
style="height: 3em;"}[[11]{.mord}]{.mord}]{style="top: -2.314em;"}[[]{.pstrut
style="height: 3em;"}[[492]{.mord}]{.mord}]{style="top: -3.677em;"}]{.vlist
style="height: 1.32144em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.686em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.mfrac}[[)]{.delimsizing .size3}]{.mclose .delimcenter
style="top: 0em;"}]{.mord}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 2.30744em; vertical-align: -0.936em;"}[[]{.mopen
.nulldelimiter}[[[[[[]{.pstrut
style="height: 3em;"}[[11]{.mord}[!]{.mclose}[(]{.mopen}[492]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[11]{.mord}[)!]{.mclose}]{.mord}]{style="top: -2.314em;"}[[]{.pstrut
style="height: 3em;"}[]{.frac-line
style="border-bottom-width: 0.04em;"}]{style="top: -3.23em;"}[[]{.pstrut
style="height: 3em;"}[[492]{.mord}[!]{.mclose}]{.mord}]{style="top: -3.677em;"}]{.vlist
style="height: 1.37144em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.936em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.mfrac}[]{.mclose .nulldelimiter}]{.mord}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 2.00744em; vertical-align: -0.686em;"}[[]{.mopen
.nulldelimiter}[[[[[[]{.pstrut
style="height: 3em;"}[[11]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[10]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[9]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[⋯]{.minner}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[1]{.mord}]{.mord}]{style="top: -2.314em;"}[[]{.pstrut
style="height: 3em;"}[]{.frac-line
style="border-bottom-width: 0.04em;"}]{style="top: -3.23em;"}[[]{.pstrut
style="height: 3em;"}[[492]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[491]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[490]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[⋯]{.minner}[]{.mspace
style="margin-right: 0.222222em;"}[⋅]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[482]{.mord}]{.mord}]{style="top: -3.677em;"}]{.vlist
style="height: 1.32144em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.686em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.mfrac}[]{.mclose .nulldelimiter}]{.mord}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

[[[[$$= 9,152,972,082,554,198,651,676$$]{.katex-mathml}[[[]{.strut
style="height: 0.36687em; vertical-align: 0em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 0.83888em; vertical-align: -0.19444em;"}[9]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[152]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[972]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[082]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[554]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[198]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[651]{.mord}[,]{.mpunct}[]{.mspace
style="margin-right: 0.166667em;"}[676]{.mord}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

Como vemos, es un número muy grande.

El espacio de codificación, como hemos comentado antes que no vamos a
restringir la cantidad de posibles soluciones, es el mismo que el
espacio de búsqueda; aunque dependiendo de la función de vecindario que
usemos (tenemos varias implementadas y por ejemplo una se asegura que de
haya mínimo un portero), habrá combinaciones de jugadores que no
lleguemos a considerar como solución. Pero lo dicho, a priori, toda
combinación es solución válida.

## Función objetivo

La función objetivo busca **maximizar** el rendimiento (rating) de un
equipo de jugadores seleccionados. Para ello, se considera la
combinación de la nota de los jugadores, el cumplimiento de los
requisitos de posiciones y el presupuesto disponible.

### Definiciones:

### Conjuntos y variables:

-   [[[$S$]{.katex-mathml}[[[]{.strut
    style="height: 0.68333em; vertical-align: 0em;"}[S]{.mord
    .mathnormal style="margin-right: 0.05764em;"}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}: Conjunto de IDs de
    los jugadores seleccionados. Es la solución que buscamos optimizar.
-   [[[$players\lbrack i\rbrack$]{.katex-mathml}[[[]{.strut
    style="height: 1em; vertical-align: -0.25em;"}[pl]{.mord .mathnormal
    style="margin-right: 0.01968em;"}[a]{.mord .mathnormal}[yers]{.mord
    .mathnormal}[\[]{.mopen}[i]{.mord
    .mathnormal}[\]]{.mclose}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}: Información del
    jugador [[[$i$]{.katex-mathml}[[[]{.strut
    style="height: 0.65952em; vertical-align: 0em;"}[i]{.mord
    .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline} (posición, valor,
    nota).
-   [[[$P_{i}$]{.katex-mathml}[[[]{.strut
    style="height: 0.83333em; vertical-align: -0.15em;"}[[P]{.mord
    .mathnormal style="margin-right: 0.13889em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.55em; margin-left: -0.13889em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline} : Posición del jugador
    [[[$i$]{.katex-mathml}[[[]{.strut
    style="height: 0.65952em; vertical-align: 0em;"}[i]{.mord
    .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}.
-   [[[$V_{i}$]{.katex-mathml}[[[]{.strut
    style="height: 0.83333em; vertical-align: -0.15em;"}[[V]{.mord
    .mathnormal style="margin-right: 0.22222em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.55em; margin-left: -0.22222em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}: Coste del jugador
    [[[$i$]{.katex-mathml}[[[]{.strut
    style="height: 0.65952em; vertical-align: 0em;"}[i]{.mord
    .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline} (value).
-   [[[$R_{i}$]{.katex-mathml}[[[]{.strut
    style="height: 0.83333em; vertical-align: -0.15em;"}[[R]{.mord
    .mathnormal style="margin-right: 0.00773em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.55em; margin-left: -0.00773em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}: Rating del jugador
    [[[$i$]{.katex-mathml}[[[]{.strut
    style="height: 0.65952em; vertical-align: 0em;"}[i]{.mord
    .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline} (rating).
-   [[[$max$]{.katex-mathml}[[[]{.strut
    style="height: 0.43056em; vertical-align: 0em;"}[ma]{.mord
    .mathnormal}[x]{.mord .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}\_[[[$presupuesto$]{.katex-mathml}[[[]{.strut
    style="height: 0.80952em; vertical-align: -0.19444em;"}[p]{.mord
    .mathnormal}[res]{.mord .mathnormal}[u]{.mord .mathnormal}[p]{.mord
    .mathnormal}[u]{.mord .mathnormal}[es]{.mord .mathnormal}[t]{.mord
    .mathnormal}[o]{.mord .mathnormal}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}: Presupuesto máximo
    disponible.

### Contadores de posiciones:

-   **G**: Número de porteros seleccionados.
-   **D**: Número de defensas seleccionados.
-   **M**: Número de mediocampistas seleccionados.
-   **F**: Número de delanteros seleccionados.

### Presupuesto y nota acumulados:

-   [[[$\text{suma\_presupuesto} = \sum_{i \in S}V_{i}$]{.katex-mathml}[[[]{.strut
    style="height: 0.92508em; vertical-align: -0.31em;"}[[suma_presupuesto]{.mord}]{.mord
    .text}[]{.mspace
    style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
    style="margin-right: 0.277778em;"}]{.base}[[]{.strut
    style="height: 1.07708em; vertical-align: -0.32708em;"}[[∑]{.mop
    .op-symbol .small-op
    style="position: relative; top: -5e-06em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[[i]{.mord .mathnormal .mtight}[∈]{.mrel
    .mtight}[S]{.mord .mathnormal .mtight
    style="margin-right: 0.05764em;"}]{.mord .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.178621em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.32708em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mop}[]{.mspace
    style="margin-right: 0.166667em;"}[[V]{.mord .mathnormal
    style="margin-right: 0.22222em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.55em; margin-left: -0.22222em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}
-   [[[$\text{suma\_nota} = \sum_{i \in S}R_{i}$]{.katex-mathml}[[[]{.strut
    style="height: 0.92508em; vertical-align: -0.31em;"}[[suma_nota]{.mord}]{.mord
    .text}[]{.mspace
    style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
    style="margin-right: 0.277778em;"}]{.base}[[]{.strut
    style="height: 1.07708em; vertical-align: -0.32708em;"}[[∑]{.mop
    .op-symbol .small-op
    style="position: relative; top: -5e-06em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[[i]{.mord .mathnormal .mtight}[∈]{.mrel
    .mtight}[S]{.mord .mathnormal .mtight
    style="margin-right: 0.05764em;"}]{.mord .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.40029em; margin-left: 0em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.178621em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.32708em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mop}[]{.mspace
    style="margin-right: 0.166667em;"}[[R]{.mord .mathnormal
    style="margin-right: 0.00773em;"}[[[[[[]{.pstrut
    style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
    .reset-size6 .size3
    .mtight}]{style="top: -2.55em; margin-left: -0.00773em; margin-right: 0.05em;"}]{.vlist
    style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
    style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
    .vlist-t2}]{.msupsub}]{.mord}]{.base}]{.katex-html
    aria-hidden="true"}]{.katex}]{.katex--inline}

### Penalizaciones:

#### Requisitos de posiciones:

Penalización por no cumplir con el número requerido de jugadores por
posición:

[[[[$${\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_posiciones}} = \left\{ \begin{matrix}
0.1 & {\text{si~}G \neq 1} \\
0.3 & {\text{si~}D < 3\text{~o~}D > 5} \\
0.3 & {\text{si~}M < 2\text{~o~}M > 5} \\
0.3 & {\text{si~}F < 1\text{~o~}F > 5} \\
0 & \text{en~caso~contrario.}
\end{matrix} \right.$$]{.katex-mathml}[[[]{.strut
style="height: 1.00444em; vertical-align: -0.31em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_posiciones]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 7.20004em; vertical-align: -3.35002em;"}[[[[[[[[]{.pstrut
style="height: 3.816em;"}[⎩]{.delimsizinginner
.delim-size4}]{style="top: -1.36599em;"}[[]{.pstrut
style="height: 3.816em;"}[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMC44ODllbSIgaGVpZ2h0PSIxLjgxNTk5OTk5OTk5OTk5OThlbSIgc3R5bGU9IndpZHRoOjAuODg5ZW0iIHZpZXdib3g9IjAgMCA4ODkgMTgxNiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ieE1pbllNaW4iPjxwYXRoIGQ9Ik0zODQgMCBINTA0IFYxODE2IEgzODR6IE0zODQgMCBINTA0IFYxODE2IEgzODR6IiAvPjwvc3ZnPg==)]{style="height: 1.816em; width: 0.889em;"}]{style="top: -1.35799em;"}[[]{.pstrut
style="height: 3.816em;"}[⎨]{.delimsizinginner
.delim-size4}]{style="top: -3.81601em;"}[[]{.pstrut
style="height: 3.816em;"}[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMC44ODllbSIgaGVpZ2h0PSIxLjgxNTk5OTk5OTk5OTk5OThlbSIgc3R5bGU9IndpZHRoOjAuODg5ZW0iIHZpZXdib3g9IjAgMCA4ODkgMTgxNiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ieE1pbllNaW4iPjxwYXRoIGQ9Ik0zODQgMCBINTA0IFYxODE2IEgzODR6IE0zODQgMCBINTA0IFYxODE2IEgzODR6IiAvPjwvc3ZnPg==)]{style="height: 1.816em; width: 0.889em;"}]{style="top: -4.95801em;"}[[]{.pstrut
style="height: 3.816em;"}[⎧]{.delimsizinginner
.delim-size4}]{style="top: -6.76602em;"}]{.vlist
style="height: 3.85002em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 3.35002em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.delimsizing .mult}]{.mopen}[[[[[[[[]{.pstrut
style="height: 3.008em;"}[[0.1]{.mord}]{.mord}]{style="top: -5.85em;"}[[]{.pstrut
style="height: 3.008em;"}[[0.3]{.mord}]{.mord}]{style="top: -4.41em;"}[[]{.pstrut
style="height: 3.008em;"}[[0.3]{.mord}]{.mord}]{style="top: -2.97em;"}[[]{.pstrut
style="height: 3.008em;"}[[0.3]{.mord}]{.mord}]{style="top: -1.53em;"}[[]{.pstrut
style="height: 3.008em;"}[[0]{.mord}]{.mord}]{style="top: -0.09em;"}]{.vlist
style="height: 3.85em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 3.35em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}[]{.arraycolsep
style="width: 1em;"}[[[[[[]{.pstrut
style="height: 3.008em;"}[[[si ]{.mord}]{.mord .text}[G]{.mord
.mathnormal}[]{.mspace style="margin-right: 0.277778em;"}[[[[[[]{.strut
style="height: 0.88888em; vertical-align: -0.19444em;"}[[[]{.mrel}]{.mord}]{.inner}[]{.fix}]{.rlap}]{.thinbox}]{.mord
.vbox}]{.mrel}[=]{.mrel}]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[1]{.mord}]{.mord}]{style="top: -5.85em;"}[[]{.pstrut
style="height: 3.008em;"}[[[si ]{.mord}]{.mord .text}[D]{.mord
.mathnormal style="margin-right: 0.02778em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\<]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[3]{.mord}[[ o ]{.mord}]{.mord
.text}[D]{.mord .mathnormal style="margin-right: 0.02778em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\>]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[5]{.mord}]{.mord}]{style="top: -4.41em;"}[[]{.pstrut
style="height: 3.008em;"}[[[si ]{.mord}]{.mord .text}[M]{.mord
.mathnormal style="margin-right: 0.10903em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\<]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[2]{.mord}[[ o ]{.mord}]{.mord
.text}[M]{.mord .mathnormal style="margin-right: 0.10903em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\>]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[5]{.mord}]{.mord}]{style="top: -2.97em;"}[[]{.pstrut
style="height: 3.008em;"}[[[si ]{.mord}]{.mord .text}[F]{.mord
.mathnormal style="margin-right: 0.13889em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\<]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[1]{.mord}[[ o ]{.mord}]{.mord
.text}[F]{.mord .mathnormal style="margin-right: 0.13889em;"}[]{.mspace
style="margin-right: 0.277778em;"}[\>]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[5]{.mord}]{.mord}]{style="top: -1.53em;"}[[]{.pstrut
style="height: 3.008em;"}[[[en caso contrario.]{.mord}]{.mord
.text}]{.mord}]{style="top: -0.09em;"}]{.vlist
style="height: 3.85em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 3.35em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}]{.mtable}]{.mord}[]{.mclose
.nulldelimiter}]{.minner}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

El valor de la función objetivo se multiplica por
[[[$(1 - {\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_posiciones}})$]{.katex-mathml}[[[]{.strut
style="height: 1em; vertical-align: -0.25em;"}[(]{.mopen}[1]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}]{.base}[[]{.strut
style="height: 1.06em; vertical-align: -0.31em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_posiciones]{.mord}]{.mord
.text}[)]{.mclose}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex--inline}.

#### Presupuesto excedido:

Penalización proporcional por exceso de presupuesto:

[[[[$${\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_presupuesto}} = \left\{ \begin{matrix}
0 & {\text{si~suma\_presupuesto} \leq \text{max\_presupuesto}} \\
{100 - \left( \frac{\text{suma\_presupuesto} \times 100}{\text{max\_presupuesto}} \right)} & {\text{si~suma\_presupuesto} > \text{max\_presupuesto}}
\end{matrix} \right.$$]{.katex-mathml}[[[]{.strut
style="height: 1.00444em; vertical-align: -0.31em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_presupuesto]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 3.24002em; vertical-align: -1.37001em;"}[[[{]{.delimsizing
.size4}]{.mopen .delimcenter style="top: 0em;"}[[[[[[[[]{.pstrut
style="height: 3.15em;"}[[0]{.mord}]{.mord}]{style="top: -4.01201em;"}[[]{.pstrut
style="height: 3.15em;"}[[100]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[[[(]{.delimsizing .size2}]{.mopen
.delimcenter style="top: 0em;"}[[]{.mopen .nulldelimiter}[[[[[[]{.pstrut
style="height: 3em;"}[[[[max_presupuesto]{.mord .mtight}]{.mord .text
.mtight}]{.mord .mtight}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.655em;"}[[]{.pstrut
style="height: 3em;"}[]{.frac-line
style="border-bottom-width: 0.04em;"}]{style="top: -3.23em;"}[[]{.pstrut
style="height: 3em;"}[[[[suma_presupuesto]{.mord .mtight}]{.mord .text
.mtight}[×]{.mbin .mtight}[100]{.mord .mtight}]{.mord .mtight}]{.sizing
.reset-size6 .size3 .mtight}]{style="top: -3.527em;"}]{.vlist
style="height: 0.978108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.562em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.mfrac}[]{.mclose .nulldelimiter}]{.mord}[[)]{.delimsizing
.size2}]{.mclose .delimcenter
style="top: 0em;"}]{.minner}]{.mord}]{style="top: -2.43001em;"}]{.vlist
style="height: 1.87001em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 1.37001em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}[]{.arraycolsep
style="width: 1em;"}[[[[[[]{.pstrut
style="height: 3.15em;"}[[[si ]{.mord}]{.mord
.text}[[suma_presupuesto]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[≤]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[[max_presupuesto]{.mord}]{.mord
.text}]{.mord}]{style="top: -4.01201em;"}[[]{.pstrut
style="height: 3.15em;"}[[[si ]{.mord}]{.mord
.text}[[suma_presupuesto]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[\>]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[[max_presupuesto]{.mord}]{.mord
.text}]{.mord}]{style="top: -2.43001em;"}]{.vlist
style="height: 1.87001em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 1.37001em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}]{.mtable}]{.mord}[]{.mclose
.nulldelimiter}]{.minner}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

### Fórmula final:

La función objetivo final se expresa como:

[[[[$$\text{objective\_function}(S) = \left( \text{suma\_nota} \times (1 - {\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_posiciones}}) \right) + {\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_presupuesto}}$$]{.katex-mathml}[[[]{.strut
style="height: 1.06em; vertical-align: -0.31em;"}[[objective_function]{.mord}]{.mord
.text}[(]{.mopen}[S]{.mord .mathnormal
style="margin-right: 0.05764em;"}[)]{.mclose}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 1.20001em; vertical-align: -0.35001em;"}[[[(]{.delimsizing
.size1}]{.mopen .delimcenter
style="top: 0em;"}[[suma_nota]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.222222em;"}[×]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[(]{.mopen}[1]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_posiciones]{.mord}]{.mord
.text}[)]{.mclose}[[)]{.delimsizing .size1}]{.mclose .delimcenter
style="top: 0em;"}]{.minner}[]{.mspace
style="margin-right: 0.222222em;"}[+]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}]{.base}[[]{.strut
style="height: 1.00444em; vertical-align: -0.31em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_presupuesto]{.mord}]{.mord .text}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

Expresado en detalle:

[[[[$$\text{objective\_function}(S) = \left( \sum\limits_{i \in S}R_{i} \right) \times \left( 1 - {\text{penalizaci}\overset{ˊ}{\text{o}}\text{n\_n\_posiciones}} \right) + \left\{ \begin{matrix}
0 & {\text{si~suma\_presupuesto} \leq \text{max\_presupuesto}} \\
{100 - \left( \frac{\text{suma\_presupuesto} \times 100}{\text{max\_presupuesto}} \right)} & {\text{si~suma\_presupuesto} > \text{max\_presupuesto}}
\end{matrix} \right.$$]{.katex-mathml}[[[]{.strut
style="height: 1.06em; vertical-align: -0.31em;"}[[objective_function]{.mord}]{.mord
.text}[(]{.mopen}[S]{.mord .mathnormal
style="margin-right: 0.05764em;"}[)]{.mclose}[]{.mspace
style="margin-right: 0.277778em;"}[=]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}]{.base}[[]{.strut
style="height: 3.07171em; vertical-align: -1.32171em;"}[[[(]{.delimsizing
.size4}]{.mopen .delimcenter style="top: 0em;"}[[[[[[]{.pstrut
style="height: 3.05em;"}[[[i]{.mord .mathnormal .mtight}[∈]{.mrel
.mtight}[S]{.mord .mathnormal .mtight
style="margin-right: 0.05764em;"}]{.mord .mtight}]{.sizing .reset-size6
.size3 .mtight}]{style="top: -1.85566em; margin-left: 0em;"}[[]{.pstrut
style="height: 3.05em;"}[∑]{.mop .op-symbol
.large-op}]{style="top: -3.05em;"}]{.vlist
style="height: 1.05001em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 1.32171em;"}]{.vlist-r}]{.vlist-t .vlist-t2}]{.mop
.op-limits}[]{.mspace style="margin-right: 0.166667em;"}[[R]{.mord
.mathnormal style="margin-right: 0.00773em;"}[[[[[[]{.pstrut
style="height: 2.7em;"}[[i]{.mord .mathnormal .mtight}]{.sizing
.reset-size6 .size3
.mtight}]{style="top: -2.55em; margin-left: -0.00773em; margin-right: 0.05em;"}]{.vlist
style="height: 0.311664em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.15em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.msupsub}]{.mord}[[)]{.delimsizing .size4}]{.mclose
.delimcenter style="top: 0em;"}]{.minner}[]{.mspace
style="margin-right: 0.222222em;"}[×]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}]{.base}[[]{.strut
style="height: 1.20001em; vertical-align: -0.35001em;"}[[[(]{.delimsizing
.size1}]{.mopen .delimcenter style="top: 0em;"}[1]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[[penalizaci]{.mord}[[[[[[]{.pstrut
style="height: 3em;"}[o]{.mord}]{style="top: -3em;"}[[]{.pstrut
style="height: 3em;"}[[ˊ]{.mord}]{.accent-body
style="left: -0.25em;"}]{style="top: -3em;"}]{.vlist
style="height: 0.69444em;"}]{.vlist-r}]{.vlist-t}]{.mord
.accent}[n_n_posiciones]{.mord}]{.mord .text}[[)]{.delimsizing
.size1}]{.mclose .delimcenter style="top: 0em;"}]{.minner}[]{.mspace
style="margin-right: 0.222222em;"}[+]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}]{.base}[[]{.strut
style="height: 3.24002em; vertical-align: -1.37001em;"}[[[{]{.delimsizing
.size4}]{.mopen .delimcenter style="top: 0em;"}[[[[[[[[]{.pstrut
style="height: 3.15em;"}[[0]{.mord}]{.mord}]{style="top: -4.01201em;"}[[]{.pstrut
style="height: 3.15em;"}[[100]{.mord}[]{.mspace
style="margin-right: 0.222222em;"}[−]{.mbin}[]{.mspace
style="margin-right: 0.222222em;"}[[[(]{.delimsizing .size2}]{.mopen
.delimcenter style="top: 0em;"}[[]{.mopen .nulldelimiter}[[[[[[]{.pstrut
style="height: 3em;"}[[[[max_presupuesto]{.mord .mtight}]{.mord .text
.mtight}]{.mord .mtight}]{.sizing .reset-size6 .size3
.mtight}]{style="top: -2.655em;"}[[]{.pstrut
style="height: 3em;"}[]{.frac-line
style="border-bottom-width: 0.04em;"}]{style="top: -3.23em;"}[[]{.pstrut
style="height: 3em;"}[[[[suma_presupuesto]{.mord .mtight}]{.mord .text
.mtight}[×]{.mbin .mtight}[100]{.mord .mtight}]{.mord .mtight}]{.sizing
.reset-size6 .size3 .mtight}]{style="top: -3.527em;"}]{.vlist
style="height: 0.978108em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 0.562em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.mfrac}[]{.mclose .nulldelimiter}]{.mord}[[)]{.delimsizing
.size2}]{.mclose .delimcenter
style="top: 0em;"}]{.minner}]{.mord}]{style="top: -2.43001em;"}]{.vlist
style="height: 1.87001em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 1.37001em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}[]{.arraycolsep
style="width: 1em;"}[[[[[[]{.pstrut
style="height: 3.15em;"}[[[si ]{.mord}]{.mord
.text}[[suma_presupuesto]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[≤]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[[max_presupuesto]{.mord}]{.mord
.text}]{.mord}]{style="top: -4.01201em;"}[[]{.pstrut
style="height: 3.15em;"}[[[si ]{.mord}]{.mord
.text}[[suma_presupuesto]{.mord}]{.mord .text}[]{.mspace
style="margin-right: 0.277778em;"}[\>]{.mrel}[]{.mspace
style="margin-right: 0.277778em;"}[[max_presupuesto]{.mord}]{.mord
.text}]{.mord}]{style="top: -2.43001em;"}]{.vlist
style="height: 1.87001em;"}[​]{.vlist-s}]{.vlist-r}[[]{.vlist
style="height: 1.37001em;"}]{.vlist-r}]{.vlist-t
.vlist-t2}]{.col-align-l}]{.mtable}]{.mord}[]{.mclose
.nulldelimiter}]{.minner}]{.base}]{.katex-html
aria-hidden="true"}]{.katex}]{.katex-display}]{.katex--display}

## Vecindarios
:::
