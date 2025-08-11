<<<<<<< HEAD
# brick-breaker
Respositorio de un juego de brick breaker en pygame
=======
# Brick Breaker Game

Un juego clásico de Breakout desarrollado con Pygame, donde el jugador controla una barra para rebotar una bola y destruir ladrillos.

## Características

- **Gameplay clásico**: Mecánicas tradicionales de Breakout
- **10 ladrillos**: Con diferentes vidas y colores
- **Sistema de vidas**: 3 vidas por partida
- **Puntuación**: +100 puntos por ladrillo destruido
- **Récords**: Sistema de récords persistentes
- **Efectos visuales**: Animaciones y efectos de daño
- **Sonidos**: Efectos de sonido sintéticos
- **Interfaz completa**: Menús, pausa, game over

## Requisitos

- Python 3.7 o superior
- Pygame 2.5.0 o superior

## Instalación

1. Clona o descarga el proyecto
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo jugar

1. Ejecuta el juego:
   ```bash
   python main.py
   ```

2. Controles:
   - **Flechas ← →**: Mover la barra
   - **Flecha ↑**: Lanzar la bola
   - **ESC**: Pausar/Reanudar
   - **R**: Ver récords
   - **ENTER**: Confirmar en menús
   - **ESPACIO**: Reiniciar (en game over)

## Estructura del proyecto

```
brick-breaker/
├── main.py              # Archivo principal
├── game.py              # Lógica principal del juego
├── paddle.py            # Clase de la barra
├── ball.py              # Clase de la bola
├── brick.py             # Clase de los ladrillos
├── ui.py                # Interfaz de usuario
├── audio.py             # Gestión de sonidos
├── data.py              # Persistencia de datos
├── requirements.txt     # Dependencias
├── game_data.json      # Datos guardados (se crea automáticamente)
└── README.md           # Este archivo
```

## Características técnicas

### Configuración
- Resolución: 500x400 píxeles
- FPS: 60
- Título: "Brick Breaker"

### Ladrillos
- 10 ladrillos totales
- 5 con vida fija = 1 impacto
- 5 con vida aleatoria entre 1 y 10
- Efectos visuales de daño progresivo
- Colores predefinidos y aleatorios

### Física
- Rebotes realistas en paredes y paddle
- Velocidad progresiva
- Ángulo de rebote basado en punto de impacto

### Sistema de récords
- Top 10 récords persistentes
- Entrada de nombre para nuevos récords
- Almacenamiento en JSON

### Audio
- Sonidos sintéticos generados dinámicamente
- Efectos de rebote, destrucción, pérdida de vida
- Control de volumen

## Desarrollo

El proyecto está estructurado en módulos separados para facilitar el mantenimiento y extensión:

- **main.py**: Controlador principal y bucle del juego
- **game.py**: Lógica de gameplay y gestión de objetos
- **paddle.py**: Comportamiento de la barra
- **ball.py**: Física de la bola
- **brick.py**: Lógica de los ladrillos
- **ui.py**: Todas las pantallas e interfaces
- **audio.py**: Gestión de sonidos y música
- **data.py**: Persistencia de datos y récords

## Licencia

Los recursos gráficos están bajo licencia Creative Commons Zero (CC0) de ImagineLabs.Rocks.

## Créditos

- Desarrollado con Pygame
- Recursos gráficos: ImagineLabs.Rocks
- Sonidos sintéticos generados dinámicamente

## Contribuir

Siéntete libre de contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Changelog

### v1.0.0
- Implementación completa del juego
- Sistema de récords
- Efectos de sonido
- Interfaz completa
- Persistencia de datos
>>>>>>> 77e27b5 (update)
