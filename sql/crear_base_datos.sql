/* Base de datos del proyecto: Datos Abiertos Colombia */
IF DB_ID(N'DatosAbiertosDB') IS NULL
BEGIN
    CREATE DATABASE DatosAbiertosDB;
END;
GO

USE DatosAbiertosDB;
GO

IF OBJECT_ID(N'dbo.RegistrosAPI', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.RegistrosAPI (
        id INT IDENTITY(1,1) PRIMARY KEY,
        id_api NVARCHAR(300) NOT NULL UNIQUE,
        codigo_municipio NVARCHAR(30) NULL,
        nombre_municipio NVARCHAR(150) NULL,
        nombre_departamento NVARCHAR(150) NULL,
        entidad NVARCHAR(250) NULL,
        tipo_entidad NVARCHAR(150) NULL,
        poblacion NVARCHAR(50) NULL,
        cantidad_usuarios NVARCHAR(50) NULL,
        cantidad_contenido NVARCHAR(50) NULL,
        cantidad_comentarios NVARCHAR(50) NULL,
        json_original NVARCHAR(MAX) NULL,
        fecha_captura DATETIME2 NOT NULL
            CONSTRAINT DF_RegistrosAPI_fecha DEFAULT SYSDATETIME()
    );
END;
GO

/* Verificación rápida de la estructura creada. */
SELECT TOP 5 * FROM dbo.RegistrosAPI ORDER BY id DESC;
GO
