#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase DataManager para manejar la persistencia de datos del juego Brick Breaker
"""

import json
import os

class DataManager:
    def __init__(self):
        self.data_file = "game_data.json"
        self.default_records = [
            {"name": "proo", "score": 10000},
            {"name": "tester", "score": 500},
            {"name": "noob", "score": 100}
        ]
        self.default_settings = {
            "volume": 0.8,
            "sound_enabled": True,
            "music_enabled": True,
            "difficulty": 1
        }
        
        # Cargar datos existentes o crear nuevos
        self.load_data()
    
    def load_data(self):
        """Cargar datos desde archivo"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.records = data.get("records", self.default_records)
                    self.settings = data.get("settings", self.default_settings)
            else:
                # Crear archivo con datos por defecto
                self.records = self.default_records.copy()
                self.settings = self.default_settings.copy()
                self.save_data()
        except Exception as e:
            print(f"Error cargando datos: {e}")
            self.records = self.default_records.copy()
            self.settings = self.default_settings.copy()
    
    def save_data(self):
        """Guardar datos en archivo"""
        try:
            data = {
                "records": self.records,
                "settings": self.settings
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def get_records(self):
        """Obtener lista de récords"""
        return self.records
    
    def is_new_record(self, score):
        """Verificar si una puntuación es un nuevo récord"""
        if len(self.records) < 10:
            return True
        
        # Verificar si la puntuación es mayor que el último récord
        return score > self.records[-1]["score"]
    
    def add_record(self, name, score):
        """Agregar nuevo récord"""
        # Crear nuevo récord
        new_record = {"name": name, "score": score}
        
        # Insertar en la posición correcta
        inserted = False
        for i, record in enumerate(self.records):
            if score > record["score"]:
                self.records.insert(i, new_record)
                inserted = True
                break
        
        # Si no se insertó, agregar al final
        if not inserted:
            self.records.append(new_record)
        
        # Mantener solo los top 10
        self.records = self.records[:10]
        
        # Guardar datos
        self.save_data()
    
    def get_settings(self):
        """Obtener configuraciones"""
        return self.settings
    
    def update_setting(self, key, value):
        """Actualizar una configuración"""
        self.settings[key] = value
        self.save_data()
    
    def get_volume(self):
        """Obtener volumen"""
        return self.settings.get("volume", 0.8)
    
    def set_volume(self, volume):
        """Establecer volumen"""
        self.update_setting("volume", volume)
    
    def is_sound_enabled(self):
        """Verificar si el sonido está habilitado"""
        return self.settings.get("sound_enabled", True)
    
    def set_sound_enabled(self, enabled):
        """Establecer si el sonido está habilitado"""
        self.update_setting("sound_enabled", enabled)
    
    def is_music_enabled(self):
        """Verificar si la música está habilitada"""
        return self.settings.get("music_enabled", True)
    
    def set_music_enabled(self, enabled):
        """Establecer si la música está habilitada"""
        self.update_setting("music_enabled", enabled)
    
    def get_difficulty(self):
        """Obtener dificultad"""
        return self.settings.get("difficulty", 1)
    
    def set_difficulty(self, difficulty):
        """Establecer dificultad"""
        self.update_setting("difficulty", difficulty)
    
    def reset_records(self):
        """Reiniciar récords a valores por defecto"""
        self.records = self.default_records.copy()
        self.save_data()
    
    def reset_settings(self):
        """Reiniciar configuraciones a valores por defecto"""
        self.settings = self.default_settings.copy()
        self.save_data()
    
    def export_data(self, filename):
        """Exportar datos a un archivo"""
        try:
            data = {
                "records": self.records,
                "settings": self.settings
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error exportando datos: {e}")
            return False
    
    def import_data(self, filename):
        """Importar datos desde un archivo"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.records = data.get("records", self.default_records)
                self.settings = data.get("settings", self.default_settings)
                self.save_data()
            return True
        except Exception as e:
            print(f"Error importando datos: {e}")
            return False

