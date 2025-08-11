#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demostración para Brick Breaker Game
Muestra las características principales del juego
"""

import pygame
import sys
import time

def show_demo():
    """Mostrar demostración del juego"""
    pygame.init()
    
    # Configurar pantalla
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Brick Breaker - Demo")
    
    # Fuentes
    title_font = pygame.font.Font(None, 48)
    text_font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)
    
    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    
    # Estados de la demostración
    states = [
        {
            "title": "Brick Breaker Game",
            "subtitle": "Un juego clásico de Breakout",
            "features": [
                "• 10 ladrillos con diferentes vidas",
                "• Sistema de vidas (3 vidas)",
                "• Puntuación progresiva",
                "• Efectos de sonido",
                "• Récords persistentes"
            ],
            "duration": 3
        },
        {
            "title": "Controles",
            "subtitle": "Cómo jugar",
            "features": [
                "• Flechas ← →: Mover barra",
                "• Flecha ↑: Lanzar bola",
                "• ESC: Pausar/Reanudar",
                "• R: Ver récords",
                "• ENTER: Confirmar en menús"
            ],
            "duration": 3
        },
        {
            "title": "Características",
            "subtitle": "Lo que hace especial este juego",
            "features": [
                "• Física realista de rebotes",
                "• Efectos visuales de daño",
                "• Sonidos sintéticos",
                "• Interfaz completa",
                "• Persistencia de datos"
            ],
            "duration": 3
        },
        {
            "title": "¡Listo para jugar!",
            "subtitle": "Presiona ESPACIO para comenzar",
            "features": [
                "• Ejecuta: python main.py",
                "• O usa: python run.py",
                "• ¡Disfruta el juego!",
                "",
                "¡Gracias por tu atención!"
            ],
            "duration": 5
        }
    ]
    
    current_state = 0
    start_time = time.time()
    
    running = True
    while running:
        current_time = time.time()
        elapsed = current_time - start_time
        
        # Cambiar estado si ha pasado el tiempo
        if elapsed >= states[current_state]["duration"]:
            current_state = (current_state + 1) % len(states)
            start_time = current_time
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        
        # Limpiar pantalla
        screen.fill(BLACK)
        
        # Dibujar estado actual
        state = states[current_state]
        
        # Título
        title_text = title_font.render(state["title"], True, WHITE)
        title_rect = title_text.get_rect(center=(250, 100))
        screen.blit(title_text, title_rect)
        
        # Subtítulo
        subtitle_text = text_font.render(state["subtitle"], True, GREEN)
        subtitle_rect = subtitle_text.get_rect(center=(250, 150))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Características
        for i, feature in enumerate(state["features"]):
            feature_text = text_font.render(feature, True, WHITE)
            feature_rect = feature_text.get_rect(center=(250, 200 + i * 25))
            screen.blit(feature_text, feature_rect)
        
        # Indicador de progreso
        progress = elapsed / state["duration"]
        progress_width = 400
        progress_height = 10
        progress_x = (500 - progress_width) // 2
        progress_y = 350
        
        # Fondo del progreso
        pygame.draw.rect(screen, (64, 64, 64), 
                        (progress_x, progress_y, progress_width, progress_height))
        
        # Barra de progreso
        pygame.draw.rect(screen, GREEN, 
                        (progress_x, progress_y, progress_width * progress, progress_height))
        
        # Instrucciones
        instruction_text = small_font.render("Presiona ESPACIO para saltar", True, (128, 128, 128))
        instruction_rect = instruction_text.get_rect(center=(250, 380))
        screen.blit(instruction_text, instruction_rect)
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    show_demo()

