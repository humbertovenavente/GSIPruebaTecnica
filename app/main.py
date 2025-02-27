from fastapi import FastAPI
from app.routes.tareas import router as tareas_router

app = FastAPI(title="Tareas GSI Kanban")

app.include_router(tareas_router, prefix="/api")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a GSI Kanban"}