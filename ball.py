#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase Ball (Bola) para el juego Brick Breaker
"""

import pygame
import math

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.initial_x = x
        self.initial_y = y
        
        # Velocidad y dirección
        self.speed = 5
        self.initial_speed = 5
        self.max_speed = 15
        self.angle = -math.pi / 2  # Hacia arriba por defecto
        
        # Velocidad en componentes x e y
        self.dx = 0
        self.dy = 0
        
        # Color de la bola (azul brillante)
        self.color = (100, 150, 255)
        self.highlight_color = (150, 200, 255)
        
        # Estado
        self.launched = False
        
    def launch(self):
        """Lanzar la bola"""
        self.launched = True
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)
    
    def update(self):
        """Actualizar posición de la bola"""
        if self.launched:
            self.x += self.dx
            self.y += self.dy
    
    def bounce_x(self):
        """Rebotar en dirección X"""
        self.dx = -self.dx
    
    def bounce_y(self):
        """Rebotar en dirección Y"""
        self.dy = -self.dy
    
    def set_angle(self, angle):
        """Establecer ángulo de la bola"""
        self.angle = angle
        speed = math.sqrt(self.dx**2 + self.dy**2)
        self.dx = speed * math.cos(angle)
        self.dy = speed * math.sin(angle)
    
    def increase_speed(self):
        """Aumentar velocidad gradualmente"""
        if self.speed < self.max_speed:
            self.speed += 0.5
            # Recalcular componentes de velocidad
            current_angle = math.atan2(self.dy, self.dx)
            self.dx = self.speed * math.cos(current_angle)
            self.dy = self.speed * math.sin(current_angle)
    
    def reset_speed(self):
        """Restablecer velocidad inicial"""
        self.speed = self.initial_speed
        if self.launched:
            current_angle = math.atan2(self.dy, self.dx)
            self.dx = self.speed * math.cos(current_angle)
            self.dy = self.speed * math.sin(current_angle)
    
    def reset(self, x, y):
        """Reiniciar posición de la bola"""
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.launched = False
        self.speed = self.initial_speed
    
    def draw(self, screen):
        """Dibujar la bola"""
        # Dibujar sombra
        pygame.draw.circle(screen, (50, 50, 50), 
                          (self.x + 2, self.y + 2), self.radius)
        
        # Dibujar bola principal
        pygame.draw.circle(screen, self.color, 
                          (self.x, self.y), self.radius)
        
        # Dibujar highlight para efecto 3D
        highlight_radius = self.radius - 3
        highlight_x = self.x - 2
        highlight_y = self.y - 2
        pygame.draw.circle(screen, self.highlight_color, 
                          (highlight_x, highlight_y), highlight_radius)
        
        # Dibujar borde
        pygame.draw.circle(screen, (255, 255, 255), 
                          (self.x, self.y), self.radius, 1)
    
    def get_rect(self):
        """Obtener rectángulo de colisión"""
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                          self.radius * 2, self.radius * 2)
    
    def is_launched(self):
        """Verificar si la bola está lanzada"""
        return self.launched

