#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo de pruebas para Brick Breaker Game
Verifica que todos los componentes funcionen correctamente
"""

import pygame
import sys
import os

def test_imports():
    """Probar que todos los módulos se importen correctamente"""
    print("Probando importaciones...")
    
    try:
        import pygame
        print("✓ pygame importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando pygame: {e}")
        return False
    
    try:
        from game import Game
        print("✓ game.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando game.py: {e}")
        return False
    
    try:
        from paddle import Paddle
        print("✓ paddle.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando paddle.py: {e}")
        return False
    
    try:
        from ball import Ball
        print("✓ ball.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando ball.py: {e}")
        return False
    
    try:
        from brick import Brick
        print("✓ brick.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando brick.py: {e}")
        return False
    
    try:
        from ui import UI
        print("✓ ui.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando ui.py: {e}")
        return False
    
    try:
        from audio import AudioManager
        print("✓ audio.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando audio.py: {e}")
        return False
    
    try:
        from data import DataManager
        print("✓ data.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando data.py: {e}")
        return False
    
    return True

def test_pygame_init():
    """Probar inicialización de pygame"""
    print("\nProbando inicialización de pygame...")
    
    try:
        pygame.init()
        print("✓ pygame inicializado correctamente")
        
        # Probar creación de pantalla
        screen = pygame.display.set_mode((500, 400))
        print("✓ Pantalla creada correctamente")
        
        pygame.quit()
        return True
    except Exception as e:
        print(f"✗ Error inicializando pygame: {e}")
        return False

def test_game_components():
    """Probar componentes del juego"""
    print("\nProbando componentes del juego...")
    
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    
    try:
        # Probar paddle
        from paddle import Paddle
        paddle = Paddle(250, 350, 500)
        print("✓ Paddle creado correctamente")
        
        # Probar ball
        from ball import Ball
        ball = Ball(250, 330)
        print("✓ Ball creada correctamente")
        
        # Probar brick
        from brick import Brick
        brick = Brick(100, 100, 80, 30, (255, 0, 0), 3)
        print("✓ Brick creado correctamente")
        
        # Probar UI
        from ui import UI
        ui = UI(screen, 500, 400)
        print("✓ UI creada correctamente")
        
        # Probar AudioManager
        from audio import AudioManager
        audio = AudioManager()
        print("✓ AudioManager creado correctamente")
        
        # Probar DataManager
        from data import DataManager
        data = DataManager()
        print("✓ DataManager creado correctamente")
        
        pygame.quit()
        return True
    except Exception as e:
        print(f"✗ Error probando componentes: {e}")
        pygame.quit()
        return False

def test_data_persistence():
    """Probar persistencia de datos"""
    print("\nProbando persistencia de datos...")
    
    try:
        from data import DataManager
        data = DataManager()
        
        # Probar obtención de récords
        records = data.get_records()
        print(f"✓ Récords cargados: {len(records)} registros")
        
        # Probar verificación de nuevo récord
        is_new = data.is_new_record(5000)
        print(f"✓ Verificación de récord: {is_new}")
        
        # Probar configuración
        settings = data.get_settings()
        print(f"✓ Configuraciones cargadas: {len(settings)} configuraciones")
        
        return True
    except Exception as e:
        print(f"✗ Error probando persistencia: {e}")
        return False

def test_audio():
    """Probar sistema de audio"""
    print("\nProbando sistema de audio...")
    
    try:
        from audio import AudioManager
        audio = AudioManager()
        
        # Probar reproducción de sonidos
        audio.play_sound("bounce")
        print("✓ Sonido de rebote reproducido")
        
        # Probar control de volumen
        audio.set_volume(0.5)
        print("✓ Volumen ajustado correctamente")
        
        return True
    except Exception as e:
        print(f"✗ Error probando audio: {e}")
        return False

def run_all_tests():
    """Ejecutar todas las pruebas"""
    print("=== PRUEBAS DE BRICK BREAKER GAME ===\n")
    
    tests = [
        ("Importaciones", test_imports),
        ("Inicialización de Pygame", test_pygame_init),
        ("Componentes del juego", test_game_components),
        ("Persistencia de datos", test_data_persistence),
        ("Sistema de audio", test_audio)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            print(f"✓ {test_name} PASÓ")
            passed += 1
        else:
            print(f"✗ {test_name} FALLÓ")
    
    print(f"\n=== RESULTADOS ===")
    print(f"Pruebas pasadas: {passed}/{total}")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El juego está listo para usar.")
        return True
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

