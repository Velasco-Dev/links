# Directorio de Chats y Bitacoras Tecnicas | NOX Links Suite

> **Documento Maestro de Control de Gestion:** Este directorio centraliza todas las bitacoras de desarrollo, sesiones de diseno, decisiones de arquitectura y especificaciones tecnicas del repositorio [`Velasco-Dev/links`](https://github.com/Velasco-Dev/links).

---

## 1. Proposito del Directorio

En consonancia con los estandares de ingenieria del ecosistema NOX, el directorio `Chats/` cumple una funcion de **Single Source of Truth (SSOT)** historica y funcional:

1. **Trazabilidad de Cambios:** Registro detallado de cada version, parche y actualizacion aplicada al codigo fuente.
2. **Documentacion de Arquitectura:** Explicacion modulo a modulo de cada componente del repositorio, facilitando el mantenimiento a largo plazo.
3. **Memoria de Decisiones de Diseno:** Registro de compromisos tecnicos, integraciones con terceros, elecciones de protocolos (redirecciones HTTP, generacion de codigos QR, estructura de GitHub Pages).
4. **Preservacion de Artefactos:** Almacenamiento de planes de accion, diagramas de flujo y recursos de diseno dentro de la subcarpeta dedicada [`Chats/artifacts/`](artifacts/).

---

## 2. Estructura del Directorio

```
Chats/
├── README.md               <-- Este archivo: Guia maestra y catalogo de bitacoras
├── Links.md                <-- Bitacora tecnica principal y especificacion de modulos
└── artifacts/              <-- Planes de diseno, diagramas y recursos auxiliares
    └── .gitkeep
```

---

## 3. Catalogo de Bitacoras Activas

| Archivo | Modulo / Alcance | Estado | Ultima Version |
| :--- | :--- | :--- | :--- |
| [`Chats/Links.md`](Links.md) | Suite completa de enlaces multi-proyecto, seguridad criptografica y generador QR | Activo / En Produccion | 2.0.0 |

---

## 4. Estandar de Documentacion y Protocolo de Versionado

Cada bitacora individual dentro de este directorio debe respetar la siguiente estructura canonica:

1. **Encabezado y Metadatos:** Nombre del modulo, repositorio, ruta local, URLs de despliegue y descripcion general.
2. **Justificacion y Arquitectura:** Por que existe el modulo, como resuelve el problema y que tecnologias implementa.
3. **Desglose Modulo a Modulo:** Descripcion exhaustiva de cada archivo y carpeta que compone el repositorio.
4. **Bitacora de Versiones:** Registro cronologico de versiones con fecha, problemas resueltos, archivos modificados y estado de verificacion.
5. **Guia de Operacion y Despliegue:** Comandos CLI, flujos web y pasos para sincronizacion en GitHub Pages.
6. **Compromiso de Cero Emojis:** Todo archivo dentro del repositorio debe preservar el estandar de 0 emojis en codigo, comentarios y documentacion.
