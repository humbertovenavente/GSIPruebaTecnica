from fastapi import APIRouter, HTTPException
from app.database.db import tareas_collection
from app.models.tarea import TareaSchema
from bson import ObjectId
from datetime import datetime

router = APIRouter()

def tarea_serializable(tarea):
    """Convierte _id de MongoDB a string para evitar errores en FastAPI"""
    tarea["_id"] = str(tarea["_id"])
    return tarea

@router.post("/tareas")
async def crear_tarea(tarea: TareaSchema):
    """Aqui se puede crear una nueva tarea"""
    nueva_tarea = tarea.dict()
    nueva_tarea["fecha_creacion"] = datetime.now()
    nueva_tarea["fecha_actualizacion"] = datetime.now()
    resultado = await tareas_collection.insert_one(nueva_tarea)
    nueva_tarea["_id"] = str(resultado.inserted_id)
    return nueva_tarea

@router.get("/tareas")
async def obtener_tareas():
    """Obtiene todas las tareas almacenadas en MongoDB"""
    tareas = await tareas_collection.find().to_list(100)
    return [tarea_serializable(tarea) for tarea in tareas]

@router.get("/tareas/{id}")
async def obtener_tarea(id: str):
    """Obtiene una tarea específica por su ID"""
    id = id.strip()  
    try:
        object_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail=f"ID de tarea inválido: {id}")

    tarea = await tareas_collection.find_one({"_id": object_id})
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_serializable(tarea)

@router.put("/tareas/{id}")
async def actualizar_tarea(id: str, tarea: TareaSchema):
    """Actualiza una tarea por su ID"""
    id = id.strip()  
    try:
        object_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail=f"ID de tarea inválido: {id}")

    tarea_actualizada = tarea.dict()
    tarea_actualizada["fecha_actualizacion"] = datetime.now()

    resultado = await tareas_collection.update_one({"_id": object_id}, {"$set": tarea_actualizada})

    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o sin cambios")
    
    return {"mensaje": "Tarea actualizada"}

@router.delete("/tareas/{id}")
async def eliminar_tarea(id: str):
    """Elimina una tarea por su ID"""
    id = id.strip()  
    try:
        object_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail=f"ID de tarea inválido: {id}")

    resultado = await tareas_collection.delete_one({"_id": object_id})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return {"mensaje": "Tarea eliminada"}
