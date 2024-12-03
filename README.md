 # To-Do Flask App

Esta es una aplicación de gestión de tareas (To-Do) creada con Flask. Permite realizar operaciones CRUD sobre tareas, asignar tareas a empleados y generar reportes de tareas pendientes agrupadas por empleado.

## Características

1. **Gestión de tareas**:
   - Crear, leer, actualizar y eliminar tareas.
   - Cada tarea incluye:
     - Título
     - Descripción
     - Estado (Pendiente, En progreso, Completada)
     - Fecha límite

2. **Gestión de empleados**:
   - Agregar empleados con nombre y correo electrónico.
   - Asignar tareas a empleados específicos.

3. **Generación de reportes**:
   - Mostrar un reporte de todas las tareas pendientes agrupadas por empleado.

## Requisitos previos

- **Python 3.8 o superior**: Asegúrate de tener Python instalado.
- **Pip**: Para gestionar las dependencias.
- **Virtualenv**: Para gestionar el entorno virtual (opcional pero recomendado).

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/todo-flask.git
   cd prueba
2. **Se debe generar el entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

(para linux)

pip install -r requirements.txt

3. **Migraciones de BD **:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   
5. **Ejecutar **:

 flask run

export FLASK_APP=run.py  # En Windows usa: set FLASK_APP=run.py



