#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase AudioManager para manejar los sonidos del juego Brick Breaker
"""

import pygame
import os

class AudioManager:
    def __init__(self):
        self.sounds = {}
        self.music_playing = False
        self.volume = 0.8
        self.sound_enabled = True
        self.music_enabled = True
        
        # Inicializar mixer
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # Cargar sonidos (crear sonidos sintéticos si no existen archivos)
        self.load_sounds()
    
    def load_sounds(self):
        """Cargar o crear sonidos para el juego"""
        # Crear sonidos sintéticos básicos si no hay archivos de audio
        self.create_synthetic_sounds()
    
    def create_synthetic_sounds(self):
        """Crear sonidos sintéticos básicos"""
        # Frecuencias para diferentes sonidos
        frequencies = {
            "bounce": 440,      # La
            "brick_break": 880, # La alto
            "life_lost": 220,   # La bajo
            "game_over": 110    # La muy bajo
        }
        
        # Duración de los sonidos (en segundos)
        duration = 0.3
        
        for sound_name, frequency in frequencies.items():
            # Crear sonido sintético
            sample_rate = 22050
            num_samples = int(sample_rate * duration)
            
            # Generar onda sinusoidal
            import math
            import numpy as np
            
            # Crear array de muestras
            t = np.linspace(0, duration, num_samples)
            amplitude = 4096 * np.exp(-t * 3)  # Decaimiento exponencial
            samples = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.int16)
            
            # Convertir a formato de audio (estéreo)
            stereo_samples = np.column_stack((samples, samples))
            
            # Crear sonido
            sound = pygame.sndarray.make_sound(stereo_samples)
            
            self.sounds[sound_name] = sound
    
    def play_sound(self, sound_name):
        """Reproducir un sonido"""
        if not self.sound_enabled:
            return
        
        if sound_name in self.sounds:
            self.sounds[sound_name].set_volume(self.volume)
            self.sounds[sound_name].play()
    
    def play_music(self, music_file=None):
        """Reproducir música de fondo"""
        if not self.music_enabled:
            return
        
        if music_file and os.path.exists(music_file):
            try:
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.set_volume(self.volume * 0.5)  # Música más baja
                pygame.mixer.music.play(-1)  # Loop infinito
                self.music_playing = True
            except:
                pass
    
    def stop_music(self):
        """Detener música de fondo"""
        pygame.mixer.music.stop()
        self.music_playing = False
    
    def pause_music(self):
        """Pausar música de fondo"""
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        """Reanudar música de fondo"""
        pygame.mixer.music.unpause()
    
    def set_volume(self, volume):
        """Establecer volumen (0.0 a 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        
        # Actualizar volumen de todos los sonidos
        for sound in self.sounds.values():
            sound.set_volume(self.volume)
        
        # Actualizar volumen de música
        if self.music_playing:
            pygame.mixer.music.set_volume(self.volume * 0.5)
    
    def toggle_sound(self):
        """Alternar sonidos"""
        self.sound_enabled = not self.sound_enabled
    
    def toggle_music(self):
        """Alternar música"""
        self.music_enabled = not self.music_enabled
        if not self.music_enabled:
            self.stop_music()
    
    def get_volume(self):
        """Obtener volumen actual"""
        return self.volume
    
    def is_sound_enabled(self):
        """Verificar si los sonidos están habilitados"""
        return self.sound_enabled
    
    def is_music_enabled(self):
        """Verificar si la música está habilitada"""
        return self.music_enabled
