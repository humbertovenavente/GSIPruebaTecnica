from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "Pruebatecnica"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
tareas_collection = database["tareas"]
