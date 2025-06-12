"""Módulo que define las rutas principales de la API usando FastAPI/Flask."""
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno

app = FastAPI(title="Mi API Python", version="0.1.0")

@app.get("/")
def read_root():
    """
    Endpoint principal que devuelve un mensaje de bienvenida.
    Returns:
        dict: Mensaje JSON de bienvenida con estructura:
            {"message": "Bienvenido a mi API"}
    """
    return {"message": "Bienvenido a mi API"}