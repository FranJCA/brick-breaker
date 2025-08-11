#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase Brick (Ladrillo) para el juego Brick Breaker
"""

import pygame
import random
import math

class Brick:
    def __init__(self, x, y, width, height, color, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.initial_health = health
        self.health = health
        self.color = color
        self.initial_color = color
        
        # Estados de daño
        self.damage_states = [
            (255, 255, 255),  # Blanco (sin daño)
            (255, 255, 200),  # Amarillo claro
            (255, 200, 100),  # Naranja claro
            (255, 150, 50),   # Naranja
            (255, 100, 50),   # Rojo claro
            (255, 50, 50),    # Rojo
            (200, 50, 50),    # Rojo oscuro
            (150, 50, 50),    # Rojo muy oscuro
            (100, 50, 50),    # Marrón rojizo
            (50, 50, 50),     # Gris oscuro
        ]
        
        # Efectos visuales
        self.damage_animation = 0
        self.damage_animation_speed = 0.3
        
    def take_damage(self):
        """Recibir daño"""
        self.health -= 1
        self.damage_animation = 1.0  # Iniciar animación de daño
        
        # Cambiar color según el daño
        damage_ratio = 1 - (self.health / self.initial_health)
        damage_index = int(damage_ratio * (len(self.damage_states) - 1))
        damage_index = min(damage_index, len(self.damage_states) - 1)
        
        self.color = self.damage_states[damage_index]
    
    def is_destroyed(self):
        """Verificar si el ladrillo está destruido"""
        return self.health <= 0
    
    def update(self):
        """Actualizar animaciones"""
        if self.damage_animation > 0:
            self.damage_animation -= self.damage_animation_speed
            if self.damage_animation < 0:
                self.damage_animation = 0
    
    def draw(self, screen):
        """Dibujar el ladrillo"""
        # Calcular color con efecto de daño
        if self.damage_animation > 0:
            # Efecto de parpadeo durante el daño
            flash_intensity = abs(math.sin(self.damage_animation * 10))
            flash_color = (255, 255, 255)
            current_color = tuple(int(c1 + (c2 - c1) * flash_intensity) 
                               for c1, c2 in zip(self.color, flash_color))
        else:
            current_color = self.color
        
        # Dibujar sombra
        shadow_offset = 2
        pygame.draw.rect(screen, (50, 50, 50), 
                        (self.x + shadow_offset, self.y + shadow_offset, 
                         self.width, self.height))
        
        # Dibujar ladrillo principal
        pygame.draw.rect(screen, current_color, 
                        (self.x, self.y, self.width, self.height))
        
        # Dibujar borde
        border_color = tuple(max(0, c - 50) for c in current_color)
        pygame.draw.rect(screen, border_color, 
                        (self.x, self.y, self.width, self.height), 2)
        
        # Dibujar highlight para efecto 3D
        highlight_color = tuple(min(255, c + 30) for c in current_color)
        highlight_rect = pygame.Rect(self.x + 2, self.y + 2, 
                                   self.width - 4, self.height // 3)
        pygame.draw.rect(screen, highlight_color, highlight_rect)
        
        # Mostrar vida restante si es mayor a 1
        if self.health > 1:
            font = pygame.font.Font(None, 20)
            health_text = font.render(str(self.health), True, (0, 0, 0))
            text_rect = health_text.get_rect(center=(self.x + self.width // 2, 
                                                   self.y + self.height // 2))
            screen.blit(health_text, text_rect)
    
    def get_rect(self):
        """Obtener rectángulo de colisión"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def get_center(self):
        """Obtener centro del ladrillo"""
        return self.x + self.width // 2, self.y + self.height // 2

