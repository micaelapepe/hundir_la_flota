# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:** (nombres)

**Herramientas usadas:** (ChatGPT, Claude, Gemini, Copilot, autocompletado de VS Code... o ninguna)

Claude Code

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|---|---|---|---|---|
| `variables.py` | Victor & Micaela| 0 | 0 | |
| `clases.py` | Daniel | 1| 1  | si |
| `funciones.py` | Raul | 1 | 1 | si |
| `main.py` | Raul | 1 | 1 | si |
| `README.md` | Victor & Micaela | 0 | 0| |

## Registro de prompts

- Identifica lugares donde deberíamos usar numpy en vez de python plano.
- Escribe las Docstrings del proyecto

### Prompt 1

- **Objetivo:** Inicialmente usamos python plano. Queríamos identificar donde nos colamos para usar numpy.
- **Prompt:** Identifica lugares donde deberíamos usar numpy en vez de python plano.
- **Respuesta relevante:** 
```
`clases.py`
- Cambiar la lista de listas `casillas` por dos arrays de NumPy: `tablero` (barcos y disparos) y `disparos` (solo disparos).
- `recibir_disparo`: indexar con `[fila, columna]` y marcar el resultado en los dos arrays.
- `mostrar`: pintar `tablero` o `disparos` según `mostrar_barcos`.
- `_hay_barco_cerca`: usar una submatriz de 3×3 en lugar de dos bucles.
- `puede_colocar` / `colocar_barco`: comprobar y escribir el barco como un trozo de fila o de columna.
- `colocar_barco_aleatorio`: usar el generador aleatorio de NumPy en lugar de `random`.
- `todos_hundidos`: comparar todo el array de una vez.

 `funciones.py`
- `disparo_maquina`: sacar con NumPy las casillas sin disparar del array `disparos`, elegir una al azar y quitar `import random`.
```

- **Cambios:** clases.py y funciones.py commit 39c4e953ef75eca15f60f571ba2bf38333553db5
Notese que no se amplicaron los cambios sugeridos tal cual. Mantuvimos nuestra estructura inicial con self.casillas, self.barcos y self.ocupadas 

- **Comprobación:** Ejecutando el código tras modificarlo a mano
- **Decisión propia:** la implementación real con numpy

### Prompt 2

- **Objetivo:** Nos faltan muchas docstrings y es un trabajo largo y monótono.
- **Prompt:** Haz docstrings para todo el codigo
- **Respuesta relevante:** 
- **Cambios:** clases.py, funciones.py y main.py Commit 445956f4d08d888fad5920c696c44f43e12b4e97
- **Comprobación:** Ejecutando el código tras modificarlo a mano
- **Decisión propia:** la implementación real con numpy
