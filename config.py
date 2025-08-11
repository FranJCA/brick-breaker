#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo de configuración para Brick Breaker Game
Contiene todas las constantes y configuraciones del juego
"""

# Configuración de la ventana
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
WINDOW_TITLE = "Brick Breaker"
FPS = 60

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
DARK_GREEN = (0, 128, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (64, 64, 64)

# Configuración del paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 8
PADDLE_COLOR = GRAY
PADDLE_ACCENT_COLOR = YELLOW

# Configuración de la bola
BALL_RADIUS = 8
BALL_INITIAL_SPEED = 5
BALL_MAX_SPEED = 15
BALL_COLOR = (100, 150, 255)
BALL_HIGHLIGHT_COLOR = (150, 200, 255)

# Configuración de los ladrillos
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_MARGIN = 10
BRICKS_PER_ROW = 5
BRICK_ROWS = 2
TOTAL_BRICKS = 10

# Colores de los ladrillos
BRICK_COLORS = [
    RED,        # Rojo
    GREEN,      # Verde
    BLUE,       # Azul
    YELLOW,     # Amarillo
    PURPLE,     # Fucsia
    CYAN,       # Cian
    ORANGE,     # Naranja
    PURPLE,     # Púrpura
    PINK,       # Rosa
    DARK_GREEN, # Verde oscuro
]

# Estados de daño de los ladrillos
DAMAGE_COLORS = [
    WHITE,           # Blanco (sin daño)
    (255, 255, 200), # Amarillo claro
    (255, 200, 100), # Naranja claro
    (255, 150, 50),  # Naranja
    (255, 100, 50),  # Rojo claro
    (255, 50, 50),   # Rojo
    (200, 50, 50),   # Rojo oscuro
    (150, 50, 50),   # Rojo muy oscuro
    (100, 50, 50),   # Marrón rojizo
    (50, 50, 50),    # Gris oscuro
]

# Configuración del juego
INITIAL_LIVES = 3
POINTS_PER_BRICK = 100
INITIAL_LEVEL = 1

# Posiciones
PADDLE_Y = WINDOW_HEIGHT - 50
BALL_Y = WINDOW_HEIGHT - 70
DOTTED_LINE_Y = WINDOW_HEIGHT - 55
DEATH_ZONE_Y = WINDOW_HEIGHT - 30

# Configuración de la línea punteada
DASH_LENGTH = 5
GAP_LENGTH = 5
DASH_WIDTH = 2

# Configuración de audio
SAMPLE_RATE = 22050
SOUND_DURATION = 0.3

# Frecuencias de sonidos
SOUND_FREQUENCIES = {
    "bounce": 440,      # La
    "brick_break": 880, # La alto
    "life_lost": 220,   # La bajo
    "game_over": 110    # La muy bajo
}

# Configuración de UI
TITLE_FONT_SIZE = 72
BUTTON_FONT_SIZE = 36
TEXT_FONT_SIZE = 24
SMALL_FONT_SIZE = 18

# Configuración de datos
DATA_FILE = "game_data.json"
DEFAULT_RECORDS = [
    {"name": "proo", "score": 10000},
    {"name": "tester", "score": 500},
    {"name": "noob", "score": 100}
]

DEFAULT_SETTINGS = {
    "volume": 0.8,
    "sound_enabled": True,
    "music_enabled": True,
    "difficulty": 1
}

# Configuración de física
BOUNCE_ANGLE_RANGE = 60  # Grados
SPEED_INCREASE_FACTOR = 0.5

