# Ficha del conjunto de datos

- **Nombre:** Portales Territoriales Sitios Web
- **Portal:** datos.gov.co
- **ID del recurso:** `cnky-uvcg`
- **Endpoint:** `https://www.datos.gov.co/resource/cnky-uvcg.json`
- **Propósito del proyecto:** consultar datos de portales territoriales y entidades municipales, almacenarlos y permitir su búsqueda.
- **Campos revisados en la ficha pública:** código y nombre de municipio, código y nombre de departamento, entidad, tipo de entidad, URL, cargos de representantes, cantidades de correos, usuarios, contenido y comentarios, población.
- **Campos almacenados por esta aplicación:** código municipal, nombre municipal, departamento, entidad, tipo de entidad, población, cantidad de usuarios, contenido y comentarios.
- **Límite inicial de consulta:** 1000 registros, modificable mediante `API_LIMIT` en `.env`.
- **Ficha pública:** https://www.datos.gov.co/en/en/Ciencia-Tecnolog-a-e-Innovaci-n/Portales-Territoriales-Sitios-Web/cnky-uvcg

Los campos pueden ser nulos en algunos registros. El modelo los admite y conserva la respuesta JSON original.
