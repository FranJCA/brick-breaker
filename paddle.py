#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase Paddle (Barra) para el juego Brick Breaker
"""

import pygame

class Paddle:
    def __init__(self, x, y, screen_width):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.screen_width = screen_width
        self.speed = 8
        self.initial_x = x
        
        # Color del paddle (gris metálico con línea amarilla)
        self.color = (128, 128, 128)
        self.accent_color = (255, 255, 0)
        
    def move_left(self):
        """Mover paddle hacia la izquierda"""
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self):
        """Mover paddle hacia la derecha"""
        if self.x < self.screen_width - self.width:
            self.x += self.speed
    
    def reset(self):
        """Reiniciar posición del paddle"""
        self.x = self.initial_x
    
    def draw(self, screen):
        """Dibujar el paddle"""
        # Dibujar cuerpo principal del paddle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        # Dibujar línea de acento amarilla en la parte superior
        pygame.draw.line(screen, self.accent_color, 
                        (self.x, self.y), 
                        (self.x + self.width, self.y), 3)
        
        # Agregar efecto de sombra para dar profundidad
        pygame.draw.rect(screen, (64, 64, 64), 
                        (self.x, self.y + self.height - 2, self.width, 2))
    
    def get_rect(self):
        """Obtener rectángulo de colisión"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def get_center(self):
        """Obtener centro del paddle"""
        return self.x + self.width // 2, self.y + self.height // 2

