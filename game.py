#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase principal del juego Brick Breaker
"""

import pygame
import random
import math
from paddle import Paddle
from ball import Ball
from brick import Brick

class Game:
    def __init__(self, screen, width, height, audio_manager):
        self.screen = screen
        self.width = width
        self.height = height
        self.audio_manager = audio_manager
        
        # Configuración del juego
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        
        # Crear objetos del juego
        self.paddle = Paddle(width // 2, height - 50, width)
        self.ball = Ball(width // 2, height - 70)
        self.bricks = []
        
        # Línea verde punteada
        self.dotted_line_y = height - 55
        
        # Zona de muerte
        self.death_zone_y = height - 30
        
        # Inicializar ladrillos
        self.create_bricks()
        
        # Estado del juego
        self.ball_launched = False
        self.paused = False
        
    def create_bricks(self):
        """Crear los 10 ladrillos según especificaciones"""
        self.bricks = []
        
        # Configuración de ladrillos
        brick_width = 80
        brick_height = 30
        margin = 10
        bricks_per_row = 5
        rows = 2
        
        # Posición inicial
        start_x = (self.width - (bricks_per_row * brick_width + (bricks_per_row - 1) * margin)) // 2
        start_y = 50
        
        # Colores predefinidos (sprites 01-20)
        colors = [
            (255, 0, 0),    # Rojo
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 255, 0),  # Amarillo
            (255, 0, 255),  # Fucsia
            (0, 255, 255),  # Cian
            (255, 165, 0),  # Naranja
            (128, 0, 128),  # Púrpura
            (255, 192, 203), # Rosa
            (0, 128, 0),    # Verde oscuro
        ]
        
        brick_count = 0
        for row in range(rows):
            for col in range(bricks_per_row):
                x = start_x + col * (brick_width + margin)
                y = start_y + row * (brick_height + margin)
                
                # Determinar vida del ladrillo
                if brick_count < 5:
                    # 5 ladrillos con vida fija = 1
                    health = 1
                else:
                    # 5 ladrillos con vida aleatoria entre 1 y 10
                    health = random.randint(1, 10)
                
                # Asignar color
                color = colors[brick_count % len(colors)]
                
                # Crear ladrillo
                brick = Brick(x, y, brick_width, brick_height, color, health)
                self.bricks.append(brick)
                brick_count += 1
                
                if brick_count >= 10:
                    break
            if brick_count >= 10:
                break
    
    def update(self):
        """Actualizar lógica del juego"""
        if self.game_over:
            return "GAME_OVER"
        
        # Manejar entrada del teclado
        keys = pygame.key.get_pressed()
        
        # Mover paddle
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
        
        # Lanzar bola
        if keys[pygame.K_UP] and not self.ball_launched:
            self.ball_launched = True
            self.ball.launch()
        
        # Actualizar bola
        if self.ball_launched:
            self.ball.update()
            
            # Verificar colisión con paredes
            self.check_wall_collision()
            
            # Verificar colisión con paddle
            self.check_paddle_collision()
            
            # Verificar colisión con ladrillos
            self.check_brick_collision()
            
            # Verificar zona de muerte
            if self.ball.y >= self.death_zone_y:
                self.lose_life()
        
        return "CONTINUE"
    
    def check_wall_collision(self):
        """Verificar colisión con paredes"""
        if self.ball.x <= 0 or self.ball.x >= self.width:
            self.ball.bounce_x()
            self.audio_manager.play_sound("bounce")
        
        if self.ball.y <= 0:
            self.ball.bounce_y()
            self.audio_manager.play_sound("bounce")
    
    def check_paddle_collision(self):
        """Verificar colisión con paddle"""
        if (self.ball.y + self.ball.radius >= self.paddle.y and 
            self.ball.y - self.ball.radius <= self.paddle.y + self.paddle.height and
            self.ball.x + self.ball.radius >= self.paddle.x and 
            self.ball.x - self.ball.radius <= self.paddle.x + self.paddle.width):
            
            # Calcular punto de impacto en el paddle
            paddle_center = self.paddle.x + self.paddle.width // 2
            ball_center = self.ball.x
            impact_point = (ball_center - paddle_center) / (self.paddle.width // 2)
            
            # Ajustar ángulo según punto de impacto
            angle = impact_point * 60  # ±60 grados máximo
            self.ball.set_angle(math.radians(angle))
            
            # Aumentar velocidad gradualmente
            self.ball.increase_speed()
            
            self.audio_manager.play_sound("bounce")
    
    def check_brick_collision(self):
        """Verificar colisión con ladrillos"""
        for brick in self.bricks[:]:  # Copia de la lista para evitar problemas al eliminar
            if (self.ball.x + self.ball.radius >= brick.x and 
                self.ball.x - self.ball.radius <= brick.x + brick.width and
                self.ball.y + self.ball.radius >= brick.y and 
                self.ball.y - self.ball.radius <= brick.y + brick.height):
                
                # Determinar dirección del rebote
                ball_center_x = self.ball.x
                ball_center_y = self.ball.y
                brick_center_x = brick.x + brick.width // 2
                brick_center_y = brick.y + brick.height // 2
                
                # Calcular distancia desde el centro del ladrillo
                dx = abs(ball_center_x - brick_center_x)
                dy = abs(ball_center_y - brick_center_y)
                
                # Determinar si el rebote es horizontal o vertical
                if dx / (brick.width // 2) > dy / (brick.height // 2):
                    self.ball.bounce_x()
                else:
                    self.ball.bounce_y()
                
                # Dañar ladrillo
                brick.take_damage()
                
                if brick.is_destroyed():
                    self.bricks.remove(brick)
                    self.score += 100
                    self.audio_manager.play_sound("brick_break")
                else:
                    self.audio_manager.play_sound("bounce")
                
                # Verificar si todos los ladrillos están destruidos
                if len(self.bricks) == 0:
                    self.next_level()
                
                break  # Solo una colisión por frame
    
    def lose_life(self):
        """Perder una vida"""
        self.lives -= 1
        self.audio_manager.play_sound("life_lost")
        
        if self.lives <= 0:
            self.game_over = True
            self.audio_manager.play_sound("game_over")
        else:
            # Reposicionar bola
            self.ball.reset(self.paddle.x + self.paddle.width // 2, self.paddle.y - 10)
            self.ball_launched = False
    
    def next_level(self):
        """Pasar al siguiente nivel"""
        self.level += 1
        self.create_bricks()
        self.ball.reset(self.paddle.x + self.paddle.width // 2, self.paddle.y - 10)
        self.ball_launched = False
        self.ball.reset_speed()
    
    def reset(self):
        """Reiniciar juego"""
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.ball_launched = False
        self.create_bricks()
        self.ball.reset(self.paddle.x + self.paddle.width // 2, self.paddle.y - 10)
        self.paddle.reset()
    
    def draw(self):
        """Dibujar todos los elementos del juego"""
        # Fondo negro
        self.screen.fill((0, 0, 0))
        
        # Dibujar línea verde punteada
        self.draw_dotted_line()
        
        # Dibujar zona de muerte
        pygame.draw.rect(self.screen, (0, 0, 0), 
                        (0, self.death_zone_y, self.width, self.height - self.death_zone_y))
        
        # Dibujar ladrillos
        for brick in self.bricks:
            brick.draw(self.screen)
        
        # Dibujar paddle
        self.paddle.draw(self.screen)
        
        # Dibujar bola
        self.ball.draw(self.screen)
        
        # Dibujar UI
        self.draw_ui()
    
    def draw_dotted_line(self):
        """Dibujar línea verde punteada"""
        dash_length = 5
        gap_length = 5
        x = 0
        
        while x < self.width:
            end_x = min(x + dash_length, self.width)
            pygame.draw.line(self.screen, (0, 255, 0), (x, self.dotted_line_y), 
                           (end_x, self.dotted_line_y), 2)
            x += dash_length + gap_length
    
    def draw_ui(self):
        """Dibujar interfaz de usuario"""
        font = pygame.font.Font(None, 36)
        
        # Puntuación
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        # Vidas
        lives_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))
        
        # Nivel
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.blit(level_text, (10, 70))
        
        # Controles
        controls_font = pygame.font.Font(None, 24)
        controls_text = controls_font.render("← → Move | ↑ Launch | ESC Pause", True, (128, 128, 128))
        self.screen.blit(controls_text, (self.width - 300, self.height - 30))
    
    def get_score(self):
        """Obtener puntuación actual"""
        return self.score
    
    def get_lives(self):
        """Obtener vidas restantes"""
        return self.lives

