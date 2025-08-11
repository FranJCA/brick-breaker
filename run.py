#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de ejecución para Brick Breaker Game
Verifica dependencias y ejecuta el juego
"""

import sys
import subprocess
import importlib

def check_dependencies():
    """Verificar que todas las dependencias estén instaladas"""
    required_modules = ['pygame']
    missing_modules = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✓ {module} está instalado")
        except ImportError:
            missing_modules.append(module)
            print(f"✗ {module} NO está instalado")
    
    if missing_modules:
        print(f"\nFaltan las siguientes dependencias: {', '.join(missing_modules)}")
        print("Instalando dependencias...")
        
        for module in missing_modules:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
                print(f"✓ {module} instalado correctamente")
            except subprocess.CalledProcessError:
                print(f"✗ Error instalando {module}")
                return False
    
    return True

def main():
    """Función principal"""
    print("=== Brick Breaker Game ===")
    print("Verificando dependencias...")
    
    if not check_dependencies():
        print("Error: No se pudieron instalar todas las dependencias")
        input("Presiona Enter para salir...")
        return
    
    print("\nIniciando juego...")
    print("Controles:")
    print("- Flechas ← →: Mover barra")
    print("- Flecha ↑: Lanzar bola")
    print("- ESC: Pausar/Reanudar")
    print("- R: Ver récords")
    print("- ENTER: Confirmar en menús")
    print("- ESPACIO: Reiniciar (en game over)")
    print("\n¡Disfruta el juego!")
    
    try:
        # Importar y ejecutar el juego
        from main import BrickBreaker
        game = BrickBreaker()
        game.run()
    except KeyboardInterrupt:
        print("\nJuego interrumpido por el usuario")
    except Exception as e:
        print(f"\nError ejecutando el juego: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()

