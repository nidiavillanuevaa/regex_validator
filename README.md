# Regex Validator

Este proyecto es una aplicación de escritorio en Python para validar y generar expresiones regulares a partir de ejemplos positivos y negativos, con interfaces gráficas amigables.

## Estructura del Proyecto

- **src/**
  - **main.py**: Punto de entrada. Lanza la interfaz principal.
  - **ai/**
    - **heuristics.py**: Genera expresiones regulares heurísticas a partir de ejemplos positivos.
    - **evaluator.py**: Evalúa si una expresión regular cumple con ejemplos positivos y negativos.
  - **automata/**
    - **regex_parser.py, nfa_builder.py, dfa_converter.py, automata_simulator.py, automata_visualizer.py**: Módulos para construir, simular y visualizar autómatas finitos a partir de expresiones regulares.
  - **ui/**
    - **gui_interface_main.py**: Selector de interfaz gráfica.
    - **gui_interface_regex.py**: Interfaz para generar y evaluar regex con ejemplos positivos/negativos.
    - **gui_interface.py**: Interfaz para validar una cadena contra una expresión regular.

- **tests/**
  - **test_heuristics_evaluator.py**: Pruebas unitarias para heuristics y evaluator.

- **requirements.txt**: Dependencias del proyecto.

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/nidiavillanuevaa/regex_validator.git
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

- Ejecuta el archivo principal:
  ```
  python src/main.py
  ```
- O crea el ejecutable:
  ```
  python -m PyInstaller --onefile --windowed src/main.py
  ```
  El ejecutable estará en la carpeta `dist`.

## Funcionalidades

- Generación automática de expresiones regulares a partir de ejemplos positivos.
- Evaluación de expresiones regulares con ejemplos positivos y negativos.
- Simulación y visualización de autómatas finitos (AFN y AFD).
- Interfaz gráfica para facilitar el uso.

## Pruebas

Para ejecutar los tests:
```
python -m unittest tests/test_heuristics_evaluator.py
```

## Dependencias principales
- tkinter
- networkx
- matplotlib
- pyinstaller

## Autoría
- Proyecto desarrollado para la materia de Lenguajes y Autómatas.
