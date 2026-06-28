# Informe: Función de Utilidad Heurística — Knight Energy

**Universidad del Valle — Inteligencia Artificial 2026-I**

---

## 1. Introducción

El algoritmo **Minimax con poda alfa-beta** requiere una función de evaluación
(heurística) para estimar el valor de los estados no terminales que se encuentran
al alcanzar el límite de profundidad del árbol. Esta función debe capturar qué tan
favorable es un estado del juego para la máquina (jugador MAX, caballo blanco) sin
necesidad de explorar todos los movimientos hasta el final de la partida.

---

## 2. Definición de la función heurística

La función de utilidad $h(s)$ para el estado $s$ se define como:

$$
h(s) = w_1 \cdot \Delta P + w_2 \cdot \Delta E + w_3 \cdot \Delta M + w_4 \cdot \text{Prox}
$$

donde:

| Componente | Símbolo | Descripción |
|-----------|---------|-------------|
| Diferencia de puntos | $\Delta P$ | $\text{puntos\_blanco} - \text{puntos\_negro}$ |
| Diferencia de energía | $\Delta E$ | $\text{energía\_blanco} - \text{energía\_negro}$ |
| Diferencia de movilidad | $\Delta M$ | $\text{movimientos\_blanco} - \text{movimientos\_negro}$ |
| Proximidad a casilla de alto valor | $\text{Prox}$ | $(d_{\text{negro}} - d_{\text{blanco}}) \times v_{\text{max}} \times 0.1$ |

Los pesos usados son: $w_1 = 1.0$, $w_2 = 0.5$, $w_3 = 0.3$, $w_4 = 0.4$.

Valores **positivos** favorecen a la máquina; valores **negativos** favorecen al humano.

---

## 3. Justificación de cada componente

### 3.1 Diferencia de puntos ($\Delta P$, peso 1.0)

Es el objetivo principal del juego: acumular más puntos que el adversario. Se
le asigna el mayor peso porque refleja directamente el criterio de victoria.

### 3.2 Diferencia de energía ($\Delta E$, peso 0.5)

La energía determina cuántos movimientos futuros puede realizar cada jugador.
Un jugador sin energía pierde el turno y recibe una penalización de −3 puntos.
Tener más energía que el oponente otorga una ventaja estratégica considerable,
aunque es menos importante que la diferencia de puntos acumulados.

### 3.3 Diferencia de movilidad ($\Delta M$, peso 0.3)

Cuantos más movimientos válidos tenga la máquina respecto al humano, mayor
es su capacidad de elección y, por tanto, mayor su control del tablero. Este
componente incentiva a la IA a mantener posiciones con alta movilidad y a
restringir la del oponente.

### 3.4 Proximidad a la casilla de máximo valor ($\text{Prox}$, peso 0.4)

Se calcula como la diferencia entre la distancia de Chebyshev del caballo negro y
del caballo blanco a la casilla de puntos más valiosa restante en el tablero.
Si la máquina está más cerca de esa casilla, el término es positivo; si el humano
está más cerca, es negativo. Se escala con el valor de la casilla para priorizar
casillas de alto valor. La distancia de Chebyshev se usa por su eficiencia
computacional como aproximación a la alcanzabilidad del caballo.

---

## 4. Casos terminales

| Condición | Valor |
|-----------|-------|
| Gana la máquina | $+\infty$ |
| Gana el humano  | $-\infty$ |
| Empate          | $0$       |

---

## 5. Limitaciones y posibles mejoras

- **Distancia de Chebyshev** es una aproximación; la distancia real en
  movimientos de caballo (BFS) sería más precisa pero más costosa.
- Los pesos pueden ajustarse mediante búsqueda de hiperparámetros o aprendizaje.
- Se podría añadir un componente que penalice acercarse al caballo contrario
  cuando este tiene mucha energía (evitar bloqueos).
