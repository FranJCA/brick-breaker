#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase UI para manejar las interfaces de usuario del juego Brick Breaker
"""

import pygame

class UI:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        
        # Colores
        self.title_color = (255, 255, 255)
        self.button_color = (100, 100, 100)
        self.button_hover_color = (150, 150, 150)
        self.text_color = (255, 255, 255)
        self.accent_color = (255, 255, 0)
        
        # Fuentes
        self.title_font = pygame.font.Font(None, 72)
        self.button_font = pygame.font.Font(None, 36)
        self.text_font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Botones del menú principal
        self.play_button = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
        self.records_button = pygame.Rect(width // 2 - 100, height // 2 + 70, 200, 50)
        
        # Botones de game over
        self.restart_button = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
        self.menu_button = pygame.Rect(width // 2 - 100, height // 2 + 120, 200, 50)
        
        # Estado para entrada de récord
        self.record_input_active = False
        self.record_input_text = ""
        self.record_input_rect = pygame.Rect(width // 2 - 150, height // 2 + 50, 300, 40)
        
    def draw_menu(self):
        """Dibujar menú principal"""
        # Título
        title_text = self.title_font.render("BRICK BREAKER", True, self.title_color)
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(title_text, title_rect)
        
        # Subtítulo
        subtitle_text = self.text_font.render("¡Rompe todos los ladrillos!", True, self.text_color)
        subtitle_rect = subtitle_text.get_rect(center=(self.width // 2, self.height // 3 + 50))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Botón Jugar
        pygame.draw.rect(self.screen, self.button_color, self.play_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.play_button, 2)
        play_text = self.button_font.render("JUGAR", True, self.text_color)
        play_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_rect)
        
        # Botón Récords
        pygame.draw.rect(self.screen, self.button_color, self.records_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.records_button, 2)
        records_text = self.button_font.render("RÉCORDS", True, self.text_color)
        records_rect = records_text.get_rect(center=self.records_button.center)
        self.screen.blit(records_text, records_rect)
        
        # Instrucciones
        instructions = [
            "Controles:",
            "← → Mover barra",
            "↑ Lanzar bola",
            "ESC Pausar",
            "R Ver récords"
        ]
        
        for i, instruction in enumerate(instructions):
            instruction_text = self.small_font.render(instruction, True, (128, 128, 128))
            instruction_rect = instruction_text.get_rect(center=(self.width // 2, self.height - 100 + i * 20))
            self.screen.blit(instruction_text, instruction_rect)
    
    def draw_pause_screen(self):
        """Dibujar pantalla de pausa"""
        # Overlay semi-transparente
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Texto de pausa
        pause_text = self.title_font.render("PAUSA", True, self.title_color)
        pause_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(pause_text, pause_rect)
        
        # Instrucciones
        instruction_text = self.text_font.render("Presiona ESC para continuar", True, self.text_color)
        instruction_rect = instruction_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(instruction_text, instruction_rect)
    
    def draw_game_over(self, score, lives):
        """Dibujar pantalla de game over"""
        # Título
        game_over_text = self.title_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Puntuación
        score_text = self.button_font.render(f"Puntuación: {score}", True, self.text_color)
        score_rect = score_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(score_text, score_rect)
        
        # Vidas restantes
        lives_text = self.text_font.render(f"Vidas restantes: {lives}", True, self.text_color)
        lives_rect = lives_text.get_rect(center=(self.width // 2, self.height // 2 + 30))
        self.screen.blit(lives_text, lives_rect)
        
        # Botón Reiniciar
        pygame.draw.rect(self.screen, self.button_color, self.restart_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.restart_button, 2)
        restart_text = self.button_font.render("REINICIAR", True, self.text_color)
        restart_rect = restart_text.get_rect(center=self.restart_button.center)
        self.screen.blit(restart_text, restart_rect)
        
        # Botón Menú
        pygame.draw.rect(self.screen, self.button_color, self.menu_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.menu_button, 2)
        menu_text = self.button_font.render("MENÚ", True, self.text_color)
        menu_rect = menu_text.get_rect(center=self.menu_button.center)
        self.screen.blit(menu_text, menu_rect)
    
    def draw_records(self, records):
        """Dibujar pantalla de récords"""
        # Título
        title_text = self.title_font.render("RÉCORDS", True, self.title_color)
        title_rect = title_text.get_rect(center=(self.width // 2, 50))
        self.screen.blit(title_text, title_rect)
        
        # Tabla de récords
        headers = ["Pos", "Nombre", "Puntuación"]
        header_y = 120
        
        # Encabezados
        for i, header in enumerate(headers):
            header_text = self.button_font.render(header, True, self.accent_color)
            header_rect = header_text.get_rect(center=(self.width // 2 - 150 + i * 150, header_y))
            self.screen.blit(header_text, header_rect)
        
        # Línea separadora
        pygame.draw.line(self.screen, self.accent_color, 
                        (50, header_y + 30), (self.width - 50, header_y + 30), 2)
        
        # Récords
        for i, record in enumerate(records[:10]):  # Top 10
            y_pos = header_y + 60 + i * 30
            
            # Posición
            pos_text = self.text_font.render(f"{i + 1}", True, self.text_color)
            pos_rect = pos_text.get_rect(center=(self.width // 2 - 150, y_pos))
            self.screen.blit(pos_text, pos_rect)
            
            # Nombre
            name_text = self.text_font.render(record["name"], True, self.text_color)
            name_rect = name_text.get_rect(center=(self.width // 2, y_pos))
            self.screen.blit(name_text, name_rect)
            
            # Puntuación
            score_text = self.text_font.render(str(record["score"]), True, self.text_color)
            score_rect = score_text.get_rect(center=(self.width // 2 + 150, y_pos))
            self.screen.blit(score_text, score_rect)
        
        # Instrucciones
        instruction_text = self.text_font.render("Presiona ESC para volver al menú", True, (128, 128, 128))
        instruction_rect = instruction_text.get_rect(center=(self.width // 2, self.height - 50))
        self.screen.blit(instruction_text, instruction_rect)
    
    def show_record_input(self, score):
        """Mostrar pantalla de entrada de récord"""
        # Overlay semi-transparente
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Título
        title_text = self.title_font.render("¡NUEVO RÉCORD!", True, self.accent_color)
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(title_text, title_rect)
        
        # Puntuación
        score_text = self.button_font.render(f"Puntuación: {score}", True, self.text_color)
        score_rect = score_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(score_text, score_rect)
        
        # Campo de entrada
        pygame.draw.rect(self.screen, (255, 255, 255), self.record_input_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.record_input_rect, 2)
        
        # Texto de entrada
        input_text = self.text_font.render(self.record_input_text, True, (0, 0, 0))
        input_rect = input_text.get_rect(center=self.record_input_rect.center)
        self.screen.blit(input_text, input_rect)
        
        # Instrucciones
        instruction_text = self.text_font.render("Ingresa tu nombre y presiona ENTER", True, self.text_color)
        instruction_rect = instruction_text.get_rect(center=(self.width // 2, self.height // 2 + 80))
        self.screen.blit(instruction_text, instruction_rect)
    
    def is_play_button_clicked(self, pos):
        """Verificar si se hizo clic en el botón jugar"""
        return self.play_button.collidepoint(pos)
    
    def is_records_button_clicked(self, pos):
        """Verificar si se hizo clic en el botón récords"""
        return self.records_button.collidepoint(pos)
    
    def is_restart_button_clicked(self, pos):
        """Verificar si se hizo clic en el botón reiniciar"""
        return self.restart_button.collidepoint(pos)
    
    def is_menu_button_clicked(self, pos):
        """Verificar si se hizo clic en el botón menú"""
        return self.menu_button.collidepoint(pos)
    
    def handle_record_input(self, event):
        """Manejar entrada de texto para récord"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return self.record_input_text
            elif event.key == pygame.K_BACKSPACE:
                self.record_input_text = self.record_input_text[:-1]
            elif event.key == pygame.K_ESCAPE:
                return None
            else:
                # Solo permitir letras y números
                if event.unicode.isalnum() and len(self.record_input_text) < 10:
                    self.record_input_text += event.unicode
        return None

