import json
from pathlib import Path

from api.api_client import APIClient

# Guarda una muestra real de la respuesta para usarla como evidencia.
datos = APIClient().obtener_registros(limite=5)
salida = Path("evidencias/respuesta_api.json")
salida.parent.mkdir(exist_ok=True)

salida.write_text(
    json.dumps(datos, ensure_ascii=False, indent=4),
    encoding="utf-8",
)

print(f"Registros recibidos: {len(datos)}")
print(f"Evidencia guardada en: {salida}")
if datos:
    print("Campos encontrados:", ", ".join(datos[0].keys()))
    print("Primer registro:", json.dumps(datos[0], ensure_ascii=False, indent=2))
