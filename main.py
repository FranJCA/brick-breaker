#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brick Breaker Game
Desarrollado con Pygame
"""

import pygame
import sys
import os
import random
import json
from game import Game
from ui import UI
from audio import AudioManager
from data import DataManager

class BrickBreaker:
    def __init__(self):
        pygame.init()
        
        # Configuración de la ventana
        self.WIDTH = 500
        self.HEIGHT = 400
        self.FPS = 60
        
        # Configurar pantalla
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Brick Breaker")
        
        # Inicializar componentes
        self.clock = pygame.time.Clock()
        self.data_manager = DataManager()
        self.audio_manager = AudioManager()
        self.ui = UI(self.screen, self.WIDTH, self.HEIGHT)
        self.game = Game(self.screen, self.WIDTH, self.HEIGHT, self.audio_manager)
        
        # Estado del juego
        self.game_state = "MENU"  # MENU, PLAYING, PAUSED, GAME_OVER, RECORDS
        
    def run(self):
        """Bucle principal del juego"""
        running = True
        
        while running:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event.pos)
            
            # Actualizar y renderizar según el estado
            if self.game_state == "MENU":
                self.update_menu()
            elif self.game_state == "PLAYING":
                self.update_game()
            elif self.game_state == "PAUSED":
                self.update_paused()
            elif self.game_state == "GAME_OVER":
                self.update_game_over()
            elif self.game_state == "RECORDS":
                self.update_records()
            
            # Limitar FPS
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()
    
    def handle_keydown(self, key):
        """Manejar eventos de teclado"""
        if key == pygame.K_ESCAPE:
            if self.game_state == "PLAYING":
                self.game_state = "PAUSED"
            elif self.game_state == "PAUSED":
                self.game_state = "PLAYING"
            elif self.game_state == "GAME_OVER":
                self.game_state = "MENU"
        
        elif key == pygame.K_RETURN:
            if self.game_state == "MENU":
                self.game_state = "PLAYING"
                self.game.reset()
            elif self.game_state == "GAME_OVER":
                self.game_state = "MENU"
        
        elif key == pygame.K_r:
            if self.game_state == "MENU":
                self.game_state = "RECORDS"
        
        elif key == pygame.K_SPACE:
            if self.game_state == "GAME_OVER":
                self.game_state = "PLAYING"
                self.game.reset()
    
    def handle_mouse_click(self, pos):
        """Manejar clics del mouse"""
        if self.game_state == "MENU":
            # Verificar clics en botones del menú
            if self.ui.is_play_button_clicked(pos):
                self.game_state = "PLAYING"
                self.game.reset()
            elif self.ui.is_records_button_clicked(pos):
                self.game_state = "RECORDS"
        
        elif self.game_state == "GAME_OVER":
            # Verificar clics en botones de game over
            if self.ui.is_restart_button_clicked(pos):
                self.game_state = "PLAYING"
                self.game.reset()
            elif self.ui.is_menu_button_clicked(pos):
                self.game_state = "MENU"
    
    def update_menu(self):
        """Actualizar pantalla del menú principal"""
        self.screen.fill((0, 0, 0))  # Fondo negro
        self.ui.draw_menu()
        pygame.display.flip()
    
    def update_game(self):
        """Actualizar pantalla del juego"""
        # Actualizar lógica del juego
        game_result = self.game.update()
        
        if game_result == "GAME_OVER":
            self.game_state = "GAME_OVER"
            # Verificar si hay nuevo récord
            score = self.game.get_score()
            if self.data_manager.is_new_record(score):
                self.ui.show_record_input(score)
        
        # Renderizar
        self.game.draw()
        pygame.display.flip()
    
    def update_paused(self):
        """Actualizar pantalla pausada"""
        self.screen.fill((0, 0, 0))
        self.game.draw()  # Dibujar estado actual del juego
        self.ui.draw_pause_screen()
        pygame.display.flip()
    
    def update_game_over(self):
        """Actualizar pantalla de game over"""
        self.screen.fill((0, 0, 0))
        self.ui.draw_game_over(self.game.get_score(), self.game.get_lives())
        pygame.display.flip()
    
    def update_records(self):
        """Actualizar pantalla de récords"""
        self.screen.fill((0, 0, 0))
        self.ui.draw_records(self.data_manager.get_records())
        pygame.display.flip()

if __name__ == "__main__":
    game = BrickBreaker()
    game.run()

