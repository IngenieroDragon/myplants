from fastapi import HTTPException, APIRouter
from pymongo import MongoClient
from models.venta import Venta
from datetime import datetime
from urllib.parse import quote_plus

venta_router = APIRouter()

client = MongoClient("mongodb+srv://ventas_coral:Q0hl5qJTsqCaroaH@clusterventas.kobx2.mongodb.net/?retryWrites=true&w=majority&appName=ClusterVentas")

db = client["myplants"]
collection = db["ventas_coral"]

@venta_router.get("/")
async def root():
    return {"message": "Hola Diego"}

@venta_router.post("/ventas_coral", response_model = Venta)
async def crear_venta(venta: Venta):
    venta_dict = venta.dict()
    venta_dict["fecha"] = datetime.now()
    
    collection.insert_one(venta_dict)
    return venta

@venta_router.get("/ventas_coral")
async def obten_ventas():
    ventas = []
    for venta in collection.find():
        ventas.append(Venta(**venta))
    return ventas

@venta_router.get("/ventas_coral/{fecha}", response_model=Venta)
async def obten_venta(fecha: datetime):
    venta = collection.find_one({"fecha": fecha})
    if venta:
        return Venta(**venta)
    else: 
        raise HTTPException(status_code=404, detail="No se han encontrado ventas para esta fecha")
    
@venta_router.put("/venta/{fecha}", response_model=Venta)
async def actualiza_venta(fecha: datetime, venta: Venta):
    venta_dict = venta.dict()
    collection.update_one({"fecha": fecha}, {"$set": venta_dict})
    return venta

@venta_router.delete("/ventas_coral/{fecha}")
async def elimina_venta(fecha: datetime):
    collection.delete_one({"fecha": fecha})
    return HTTPException(status_code=400, detail="Se ha eliminado correctamente la venta.")