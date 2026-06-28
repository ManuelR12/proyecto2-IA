# Knight Energy

Juego de ajedrez por turnos entre un jugador humano y la IA, implementado con el algoritmo **Minimax con poda alfa-beta** y decisiones imperfectas.

## Reglas del juego

- Tablero de ajedrez 8×8.
- Cada jugador controla un caballo y empieza con **7 unidades de energía**.
- Cada movimiento cuesta **1 de energía**.
- **Casillas de puntos** (valores 2, 3, 4, 5, 6, 8, 9): sumar puntos al caer en ellas.
- **Casillas de energía** (valores 2, 3, 4, 5): recuperar energía al caer en ellas.
- Sin energía para mover → pierde turno y −3 puntos.
- Fin del juego: sin casillas de puntos restantes **o** ningún jugador puede mover.
- Gana quien acumule más puntos.

## Niveles de dificultad

| Nivel        | Profundidad Minimax |
|-------------|---------------------|
| Principiante | 2                   |
| Amateur      | 4                   |
| Experto      | 6                   |

## Estructura del proyecto

```
proyecto2-IA/
├── main.py               # Punto de entrada
├── requirements.txt
├── .gitignore
├── src/
│   ├── game/
│   │   ├── board.py      # Tablero y posicionamiento aleatorio
│   │   ├── knight.py     # Movimientos del caballo
│   │   ├── game_state.py # Estado del juego
│   │   └── rules.py      # Validación de reglas
│   ├── ai/
│   │   ├── minimax.py    # Algoritmo Minimax con alfa-beta
│   │   └── heuristic.py  # Función heurística de utilidad
│   └── ui/
│       └── display.py    # Visualización en consola
├── tests/
│   ├── test_board.py
│   ├── test_minimax.py
│   └── test_game.py
└── docs/
    └── informe.md        # Informe de la función heurística
```

## Ejecución

```bash
pip install -r requirements.txt
python main.py
```

## Equipo

| Integrante | Responsabilidad principal |
|-----------|--------------------------|
| Persona 1 | Lógica del juego (tablero, reglas, caballos) |
| Persona 2 | IA: Minimax, heurística e informe |
| Persona 3 | Estado del juego, UI, integración y pruebas |
