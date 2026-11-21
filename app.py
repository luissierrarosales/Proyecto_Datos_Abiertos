import os
from flask import Flask, flash, redirect, render_template, request, url_for

from api.api_client import APIClient
from models.datos_model import (
    consultar_registros,
    obtener_estadisticas,
    guardar_registros,
)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "clave-local-cambiar-antes-de-publicar")


@app.route("/", methods=["GET"])
def inicio():
    filtro = request.args.get("q", "").strip()
    registros = consultar_registros(filtro)
    estadisticas = obtener_estadisticas()
    return render_template(
        "index.html",
        registros=registros,
        estadisticas=estadisticas,
        filtro=filtro,
    )


@app.route("/sincronizar", methods=["POST"])
def sincronizar():
    try:
        cliente = APIClient()
        datos = cliente.obtener_registros()
        cantidad = guardar_registros(datos)
        flash(
            f"Sincronización terminada. Registros recibidos: {len(datos)}. "
            f"Registros nuevos guardados: {cantidad}.",
            "success",
        )
    except Exception as error:
        app.logger.exception("Error durante la sincronización")
        flash(f"No fue posible completar la sincronización: {error}", "error")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    # Servidor local para desarrollo académico.
    app.run(host="127.0.0.1", port=5000, debug=True)
