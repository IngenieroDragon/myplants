from fastapi import FastAPI
from pymongo import MongoClient
from schema.schema_venta import venta_router
from urllib.parse import quote_plus



app = FastAPI()
app.include_router(venta_router)


username = "ventas_coral"
password = "Q0hl5qJTsqCaroaH"

# Escapar credenciales
username_escaped = quote_plus(username)
password_escaped = quote_plus(password)

client = MongoClient("mongodb+srv://{username_escaped}:{password_escaped}@clusterventas.kobx2.mongodb.net/?retryWrites=true&w=majority&appName=ClusterVentas")


db = client["myplants"]
collection = db["ventas_coral"]


