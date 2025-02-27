# Kanban Backend con FastAPI 

Esta prueba es un CRUD básico para una aplicación tipo Kanban, desarrollado con **FastAPI** y **MongoDB**.

En dado caso que **MongoDB Compass** me causa problemas con lo que es la visualización o coneión con la base de datos, tengo opcion de también usar **mongosh** para poder interactuar con MongoDB directamente gracias a su flexibilidad.

Cabe recalcar que se usó lo que **venv** y **uvicorn** para poder ejecutar FastAPI, venv se uso para poder tener un entorno aislado para poder instalar los paquetes deseados sin causar errores con otros proyectos que tengo en VS

Ahora bien uvicorn me ayudará a poder ejecutar la API y hacer las conexiones HTTP, ayudando a poder manejar las peticiones asíncronamente

Por lo que para poder crear el entorno virtual nuevo, hacerlo con **python -m venv venv** y lluego activarlo con **venv\Scripts\Activate**, una vez instalado, se instala las dependecias que se tienen con **pip install -r requirements.txt**

Una vez todo eso se ejecute, se puede abrir uvicorn con **uvicorn app.main:app --reload**

es muy importante correrlo con 
##  Endpoints disponibles
- `POST /api/tareas` → Crear una nueva tarea
- `GET /api/tareas` → Obtener todas las tareas
- `GET /api/tareas/{id}` → Obtener una tarea en espifico 
- `PUT /api/tareas/{id}` → Actualizar una tarea
- `DELETE /api/tareas/{id}` → Eliminar una tarea

##  GITHUB
1. Clona el repositorio aqui:
   git clone https://github.com/TU_USUARIO/kanban-backend-fastapi.git
