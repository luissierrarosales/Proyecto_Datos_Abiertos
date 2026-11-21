import os
import requests
from dotenv import load_dotenv

load_dotenv()


class APIClient:
    """Cliente sencillo para consultar el conjunto de datos de datos.gov.co."""

    def __init__(self):
        recurso = os.getenv("API_RESOURCE_ID", "cnky-uvcg").strip()
        if not recurso:
            raise ValueError("Falta configurar API_RESOURCE_ID en el archivo .env")
        self.url = f"https://www.datos.gov.co/resource/{recurso}.json"

    def obtener_registros(self, limite=None):
        """Solicita JSON a la API y devuelve una lista de registros."""
        cantidad = int(limite or os.getenv("API_LIMIT", "100"))
        respuesta = requests.get(
            self.url,
            params={"$limit": cantidad},
            timeout=25,
        )
        respuesta.raise_for_status()
        datos = respuesta.json()

        if not isinstance(datos, list):
            raise ValueError("La API no devolvió una lista JSON como se esperaba.")
        return datos
