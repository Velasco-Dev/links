# Modulo Helpers/URL_Shorter - Recortador y Gestor Local de Enlaces

> **Documento de Control y Especificacion Tecnica:** Este archivo documenta el modulo centralizado [`/Helpers/URL_Shorter`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter), disenado como un subsistema autonomo para generar, gestionar y auditar enlaces cortos en local, servir redirecciones HTTP 302 hacia las distintas aplicaciones web y recursos en la nube del ecosistema (iniciando con **NOX Slush & Beats**), y producir codigos QR asociados.

---

## 1. Justificacion y Proposito Estrategico

En un ecosistema corporativo basado en **Google Apps Script**, **Google Sheets** y servicios web distribuidos, las URLs de produccion suelen ser extremadamente extensas, dificiles de memorizar y complejas de compartir en material fisico o terminales de punto de venta:

1. **Enlaces Amigables y de Facil Acceso:** Transformar enlaces de mas de 100 caracteres en aliases claros como `http://localhost:5050/menu`, `http://localhost:5050/db` o `http://localhost:5050/editor`.
2. **Impresion en Material POP y Tarjetas de Barra:** Reduccion de la densidad de datos al generar codigos QR; a menor longitud de la URL, el codigo QR tiene modulos mas grandes y legibles, lo que facilita el escaneo rapido en telefonos moviles incluso con baja iluminacion.
3. **Auditoria y Metricas de Acceso Local:** Registro de clics en base de datos SQLite con detalle de marca temporal, direccion IP, agente de usuario y referer.
4. **Resiliencia Dual (Offline / Online):** Capacidad de operar de forma 100% independiente en el navegador web mediante `localStorage` o acoplarse reactivamente al servidor local multi-hilo en Python.

---

## 2. Componentes del Modulo

El modulo se encapsula estrictamente dentro de la ruta [`Helpers/URL_Shorter/`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter):

* **[`Helpers/URL_Shorter/url_shortener.py`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter/url_shortener.py):** Motor en Python con menu interactivo en terminal (colores Colorama), gestor de base de datos SQLite (`data/urls.db`), generador de codigos QR y servidor HTTP multi-hilo de redireccion y API REST.
* **[`Helpers/URL_Shorter/recortador_url.html`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter/recortador_url.html):** Aplicacion web grafica con diseno Cyberpunk Liquid Glass (Orbitron, Outfit, FontAwesome), soporte dual para Modo Claro y Modo Oscuro, sincronizacion en caliente con el servidor y descarga de QR en PNG.
* **[`Helpers/URL_Shorter/requirements.txt`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter/requirements.txt):** Manifiesto de dependencias en Python (`colorama`, `qrcode`, `pillow`).
* **[`Helpers/URL_Shorter/data/`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter/data):** Directorio de almacenamiento para la base de datos SQLite (`urls.db`), codigos QR generados (`qrs/`) y exportaciones JSON/CSV.
* **[`Helpers/URL_Shorter/README.md`](file:///G:/Ingenieria%20Informatica/Git%20Externo/Proyectos_Google_Apps_Scripts/Helpers/URL_Shorter/README.md):** Manual rapido de operacion para desarrolladores y usuarios finales.

---

## 3. Presets Oficiales Integrados del Ecosistema NOX

El sistema incorpora de fabrica los accesos directos oficiales de la plataforma:

| Alias / Slug | Recurso Destino Oficial | Titulo Descriptivo |
| :--- | :--- | :--- |
| `/menu` | `https://script.google.com/macros/s/AKfycbzBLqsY6YqLex1KzvvlBT5viV8KNmw2VlKL8kZ-Wn5_/dev` | NOX \| Menu Digital & Web App Oficial |
| `/db` | `https://docs.google.com/spreadsheets/d/1vqtsoonbIRhnQ8bas060h27p7C-TKAIDX7cdHE8Ok5E/edit` | NOX \| Base de Datos Google Sheets (7 Pestanas) |
| `/editor` | `https://script.google.com/home/projects/19Jj1QYs18vnHqS9FqM41cnGebJPlyRewE035hxI8VMK1J4skK1ETXioR/edit` | NOX \| Editor de Google Apps Script |
| `/ig` | `https://www.instagram.com/noxslushnbeats/` | NOX \| Instagram Oficial (@noxslushnbeats) |

---

## 4. Arquitectura y Esquema de Datos

### 4.1. Base de Datos SQLite (`data/urls.db`)

El sistema utiliza dos tablas relacionales optimizadas con indices:

1. **Tabla `urls`:**
   - `id`: Identificador unico secuencial.
   - `slug`: Alias unico indexado (ej. `menu`, `db`, `promo2026`).
   - `long_url`: URL completa de destino.
   - `title`: Etiqueta descriptiva del recurso.
   - `clicks`: Contador acumulado de redirecciones exitosas.
   - `created_at`: Marca temporal de creacion.
   - `last_clicked`: Marca temporal del ultimo acceso registrado.
   - `is_active`: Bandera booleana de estado (1 = Activo, 0 = Inactivo).

2. **Tabla `clicks_log`:**
   - `id`: Identificador del evento de clic.
   - `slug`: Alias consultado.
   - `timestamp`: Momento exacto de la peticion HTTP.
   - `ip`: Direccion IP del cliente solicitante.
   - `user_agent`: Cabecera del navegador o dispositivo.
   - `referer`: Origen de la navegacion si esta disponible.

---

## 5. Guia Rapida de Operacion

### 5.1. Instalacion
```powershell
.\.venv\Scripts\pip.exe install -r Helpers/URL_Shorter/requirements.txt
```

### 5.2. Modo Servidor Local (Recomendado)
```powershell
.\.venv\Scripts\python.exe Helpers/URL_Shorter/url_shortener.py --serve --port 5050
```
- **Aplicacion Web:** [`http://localhost:5050/`](http://localhost:5050/)
- **Prueba de Redireccion:** [`http://localhost:5050/menu`](http://localhost:5050/menu)

### 5.3. Modo CLI y Generacion de Codigos QR
```powershell
# Cargar presets oficiales
.\.venv\Scripts\python.exe Helpers/URL_Shorter/url_shortener.py --init-presets

# Acortar URL personalizada
.\.venv\Scripts\python.exe Helpers/URL_Shorter/url_shortener.py -s "https://mi-enlace.com" -a "mi-alias"

# Generar codigo QR para un alias
.\.venv\Scripts\python.exe Helpers/URL_Shorter/url_shortener.py --qr menu --qr-style nox_neon
```
