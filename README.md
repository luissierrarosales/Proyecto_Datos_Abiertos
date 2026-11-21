# Sistema Web de Consulta y Análisis de Datos Abiertos

**Integrantes:** Luis Sierra, José Maldonado y Juan David Donado  
**Asignatura:** Desarrollo de Aplicaciones con Acceso a Datos  
**Tecnologías:** Python, Flask, API REST (SODA), SQL Server, pyodbc, HTML y CSS.

## 1. Objetivo

Construir una aplicación web que consulte un conjunto de datos abiertos de Colombia mediante una API REST, reciba la información en JSON, almacene los registros en SQL Server y permita consultarlos desde el navegador usando el patrón Modelo–Vista–Controlador (MVC).

## 2. Conjunto de datos seleccionado

- **Nombre:** Portales Territoriales Sitios Web.
- **Portal:** datos.gov.co.
- **Identificador del recurso:** `cnky-uvcg`.
- **Ficha pública:** https://www.datos.gov.co/en/en/Ciencia-Tecnolog-a-e-Innovaci-n/Portales-Territoriales-Sitios-Web/cnky-uvcg
- **Endpoint SODA:** https://www.datos.gov.co/resource/cnky-uvcg.json
- **Propósito:** consultar información publicada sobre portales territoriales y entidades municipales.
- **Campos utilizados:** `codigo_municipio`, `nombre_municipio`, `nombre_departament`, `entidad`, `tipo_entidad`, `poblacion`, `cantidad_usuarios`, `cantidad_contenido` y `cantidad_comentarios`.

El identificador y los nombres de campos corresponden a la ficha pública del conjunto. La API puede cambiar su disponibilidad o contenido; por eso se valida la respuesta JSON al sincronizar.

## 3. Requisitos previos

1. Windows 10/11.
2. Python 3.10 o superior.
3. Microsoft SQL Server instalado y en ejecución.
4. SQL Server Management Studio (SSMS).
5. Microsoft ODBC Driver 18 for SQL Server.
6. Conexión a Internet para consultar datos.gov.co.

## 4. Instalación rápida

### Paso 1. Crear la base de datos

1. Abrir SQL Server Management Studio.
2. Conectarse a la instancia local de SQL Server.
3. Abrir y ejecutar `sql/crear_base_datos.sql`.
4. Confirmar que se creó `DatosAbiertosDB` y la tabla `dbo.RegistrosAPI`.

### Paso 2. Configurar la conexión

1. En la carpeta principal, copiar `.env.example`.
2. Renombrar la copia a `.env`.
3. Ajustar `DB_SERVER` según la instancia instalada:
   - Instancia predeterminada: `localhost`
   - SQL Express: `localhost\\SQLEXPRESS`
4. Para autenticación de Windows, dejar `DB_TRUSTED=yes`.
5. Para autenticación SQL, colocar `DB_TRUSTED=no` y completar `DB_USER` y `DB_PASSWORD`.

No se entrega un `.env` con credenciales porque estas dependen del computador donde se ejecute el proyecto.

### Paso 3. Instalar dependencias

Abrir una terminal en la carpeta del proyecto y ejecutar:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 4. Iniciar la aplicación

```powershell
python app.py
```

Abrir en el navegador: http://127.0.0.1:5000

Pulsar **Consultar API y guardar datos**. Luego se pueden buscar los registros por municipio, departamento o entidad.

## 5. Archivos principales y patrón MVC

| Archivo | Responsabilidad |
|---|---|
| `app.py` | **Controlador:** define rutas Flask, recibe filtros y coordina las operaciones. |
| `api/api_client.py` | Servicio cliente: consume el endpoint externo y convierte la respuesta JSON. |
| `models/datos_model.py` | **Modelo:** conexión pyodbc, inserción controlada y consultas SQL. |
| `templates/index.html` | **Vista:** estructura HTML y presentación de resultados con Jinja2. |
| `static/estilos.css` | Estilos visuales y adaptación a pantallas pequeñas. |
| `sql/crear_base_datos.sql` | Crea la base de datos y la tabla. |

El HTML no contiene consultas SQL ni conexiones a la base de datos. La vista recibe los datos del controlador y el modelo se encarga de SQL Server.

## 6. Flujo de funcionamiento

1. El usuario pulsa el botón de sincronización.
2. Flask ejecuta la ruta `POST /sincronizar`.
3. `APIClient` realiza una petición HTTP GET al endpoint de datos.gov.co.
4. La API responde con una lista de objetos JSON.
5. El modelo procesa los registros y los inserta en SQL Server.
6. La columna `id_api` tiene restricción `UNIQUE` y la inserción verifica que no exista previamente.
7. La página principal consulta SQL Server y muestra los registros.
8. El formulario de búsqueda aplica un filtro sobre municipio, departamento o entidad.

## 7. Prevención de duplicados

La clave del registro se construye con `codigo_municipio` y `entidad` cuando la fuente no ofrece un campo `id` o `codigo`. SQL Server refuerza la prevención mediante la restricción `UNIQUE` de `id_api`. Al repetir la sincronización no se deben insertar de nuevo las claves existentes.

## 8. Pruebas y evidencias

Ejecutar el flujo y guardar capturas reales en `evidencias/`:

- `01_respuesta_api.png` o `respuesta_api.json`: respuesta JSON recibida.
- `02_registros_sql.png`: filas visibles en SQL Server Management Studio.
- `03_pagina_principal.png`: página web con registros.
- `04_busqueda_filtrada.png`: resultado de una búsqueda.
- `05_segunda_sincronizacion.png`: segunda sincronización sin duplicados.

El proyecto incluye `probar_api.py` para generar `evidencias/respuesta_api.json` y revisar el consumo de la API. Las capturas deben tomarse en el computador donde se ejecute el sistema; no se incluyen capturas simuladas.

## 9. Solución de errores comunes

- **ModuleNotFoundError:** activar el entorno virtual e instalar `requirements.txt`.
- **Data source name not found:** instalar ODBC Driver 18 y revisar `DB_DRIVER`.
- **Login failed:** comprobar instancia y método de autenticación de SQL Server.
- **Invalid object name:** ejecutar el script SQL y confirmar la base de datos seleccionada.
- **HTTP 404:** revisar `API_RESOURCE_ID` y la ficha del conjunto.
- **HTTP 429:** reducir `API_LIMIT` y esperar antes de volver a consultar.
- **No aparecen registros:** revisar la conexión, la respuesta de la API y los nombres de campos del JSON.

## 10. Seguridad y alcance

- No se incluye contraseña real ni archivo `.env`.
- Las consultas SQL usan parámetros.
- `debug=True` está habilitado únicamente para desarrollo local.
- No se implementa CRUD completo, autenticación de usuarios ni despliegue público, porque no hacen parte del alcance reducido de la guía.
- Se conserva `json_original` para mantener la respuesta completa recibida de la fuente.

## 11. Distribución del trabajo

| Integrante | Responsabilidad principal |
|---|---|
| Luis Sierra | Consumo de API, revisión del JSON y documentación del conjunto de datos. |
| José Maldonado | SQL Server, modelo de datos, integración Flask y vista web. |
| Juan David Donado | Integrante del equipo; responsabilidad específica pendiente de confirmar. |
| Ambos | Integración, pruebas, documentación y sustentación del flujo completo. |

El equipo queda conformado por los tres integrantes indicados. La responsabilidad específica de Juan David Donado debe completarse según el trabajo que haya realizado.

## 12. Guion breve para la sustentación

“Desarrollamos una aplicación web que consulta un conjunto de datos abiertos de Colombia mediante una API REST. El cliente API realiza la petición HTTP y recibe los datos en formato JSON. Después, el Modelo utiliza pyodbc para conectarse a SQL Server y almacenar los registros, evitando duplicados mediante una clave única. El Controlador, implementado con Flask, coordina las solicitudes y llama al modelo. Finalmente, la Vista presenta la información y permite buscar registros. Aplicamos MVC para separar la presentación, la coordinación y el acceso a los datos. El alcance se concentra en consultar la API, almacenar y consultar la información, sin implementar un CRUD completo.”
