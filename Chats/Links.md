# Bitacora Tecnica y Control de Modulos | NOX Links Suite

> **Documento de Control y Especificacion Tecnica:** Este archivo documenta de forma exhaustiva la arquitectura, especificacion modulo a modulo, registro evolutivo y directrices de mantenimiento del repositorio autonomo [`Velasco-Dev/links`](https://github.com/Velasco-Dev/links), desplegado en produccion mediante GitHub Pages en [`https://velasco-dev.github.io/links/`](https://velasco-dev.github.io/links/).

---

## 1. Justificacion Estrategica y Vision de Negocio

El proyecto **NOX Slush & Beats** y sus futuras aplicaciones satelite requieren una plataforma de direccionamiento rapida, estetica, segura y multi-marca:

1. **Eliminacion de Intermediarios con Publicidad:** Plataformas comerciales como Bitly o Linktree imponen pantallas intermedias, anuncios invasivos, limites mensuales y costos recurrentes. NOX Links Suite resuelve el 100% de los accesos de forma directa e instantanea.
2. **Optimizacion para Redes Sociales (Instagram Bio):** La URL oficial `https://velasco-dev.github.io/links/menu` tiene una longitud de solo 42 caracteres, siendo sumamente estetica y legible en biografias de redes sociales, mensajes directos de WhatsApp y material impreso.
3. **Optimizacion de Codigos QR:** Cuanto mas corta es la URL destino codificada, menor es la densidad de modulos del codigo QR. Esto incrementa de forma notable la velocidad y tolerancia de lectura de los codigos impresos en acrilicos de mesa, vasos y servilletas en condiciones de iluminacion nocturna.
4. **Segregacion Estricta de Privacidad (Publico vs Gerencial):** El publico general unicamente tiene visibilidad sobre los canales de venta e interaccion (Menu, Instagram, WhatsApp). Las herramientas operativas y de desarrollo (Google Sheets, Editor Apps Script) se encapsulan como recursos privados accesibles unicamente por el propietario a traves de la consola gerencial autenticada.
5. **Capacidad Multi-Proyecto en Contenedor Unico:** Capacidad nativa para albergar multiples marcas y clientes en el mismo repositorio, permitiendo que cada uno tenga su propia paleta de colores, logotipo, tipografia y listado de enlaces publicos.
6. **Independencia de Servidores Locales:** Al operar sobre la infraestructura global de **GitHub Pages**, los enlaces estan en linea las 24 horas del dia los 365 dias del ano, con cero costo y cero mantenimiento de servidores personales.

---

## 2. Desglose Modulo a Modulo del Repositorio

A continuacion se describe en detalle cada archivo, directorio y subsistema que conforma el proyecto:

```
G:\Ingenieria Informatica\Git Externo\links/
├── index.html              <-- Modulo 1: Portal Publico Dinamico Multi-Proyecto (Bio Link)
├── admin/                  <-- Modulo 2: Consola Gerencial Privada & QR Studio
│   └── index.html          (Interfaz protegida bajo barrera criptografica SHA-256)
├── admin.html              <-- Modulo 2B: Enrutador rapido de contingencia hacia admin/
├── 404.html                <-- Modulo 3: Enrutador SPA de Redireccion Dinamica
├── redirects.json          <-- Modulo 4: Base de Datos Multi-Proyecto y Esquema Criptografico
├── manager.py              <-- Modulo 5: Asistente CLI en Python (Compilador & QR Engine)
├── menu/index.html         <-- Modulo 6A: Redireccion Estatica Directa hacia Menu Digital (GAS)
├── ig/index.html           <-- Modulo 6B: Redireccion Estatica Directa hacia Instagram Oficial
├── wa/index.html           <-- Modulo 6C: Redireccion Estatica Directa hacia WhatsApp Oficial
├── db/index.html           <-- Modulo 6D: Redireccion Estatica Privada hacia Base de Datos (Sheets)
├── editor/index.html       <-- Modulo 6E: Redireccion Estatica Privada hacia Editor Apps Script
├── assets/                 <-- Modulo 7: Activos de Identidad Visual y QR
│   ├── logo.jpeg           (Logotipo oficial circular de NOX)
│   └── qrs/                (Codigos QR exportados en alta definicion)
├── requirements.txt        <-- Modulo 8A: Dependencias de Python (colorama, qrcode, pillow)
├── .gitignore              <-- Modulo 8B: Filtros de control de versiones
└── README.md               <-- Modulo 8C: Manual de usuario y guia de despliegue
```

---

### Modulo 1: Portal Publico Dinamico Multi-Proyecto (`index.html`)

* **Ruta de Acceso:** [`index.html`](../index.html)
* **URL en Produccion:** `https://velasco-dev.github.io/links/` o `.../links/?p=<slug>`
* **Proposito y Funcion:** Es la cara publica visible cuando un cliente ingresa directamente al enlace de la biografia.
* **Caracteristicas de Seguridad y Buenas Practicas:**
  - **Exclusion Total de Enlaces Internos:** No muestra los accesos a Google Sheets ni al editor de scripts. Solo renderiza enlaces con la propiedad `is_public: true`.
  - **Cero Enlaces Administrativos en el Pie:** Se elimino cualquier boton visible hacia la consola de administracion.
  - **Renderizado Hibrido Cero Latencia:** Renderiza instantaneamente la estructura publica de NOX por defecto, y si detecta el parametro `?p=otro_proyecto`, re-estiliza reactivamente la interfaz (colores, logotipo, titulos y enlaces propios de ese proyecto).
  - **Atajo Secreto de Propietario:** Permite navegar a `/admin/` haciendo 5 toques rapidos sobre el logotipo circular superior.

---

### Modulo 2: Consola Gerencial Privada (`admin/index.html`)

* **Ruta de Acceso:** [`admin/index.html`](../admin/index.html)
* **URL en Produccion:** `https://velasco-dev.github.io/links/admin/`
* **Barrera Criptografica de Acceso:**
  - **Pantalla de Bloqueo Mandatoria:** Al cargar la pagina, ningun dato ni control administrativo es visible en el DOM hasta ingresar la clave maestra correcta.
  - **Verificacion SHA-256 con Salt:** Implementa Web Crypto API en el navegador para comparar el resumen criptografico de la contrasena ingresada contra `security.admin_hash`.
  - **Aislamiento de Sesion en `sessionStorage`:** La sesion activa expira automaticamente al cerrar la pestana o al hacer clic en "Bloquear".
* **Funcionalidades Gerenciales:**
  1. **Selector & Creador Multi-Proyecto:** Permite conmutar entre diferentes marcas o dar de alta un nuevo proyecto con su propia paleta de colores y enlaces.
  2. **Catalogo y Clasificacion de Enlaces:** Creacion, edicion y eliminacion de enlaces marcando de forma explicita si es **Publico** (visible para clientes) o **Privado / Gerencial** (oculto en el Bio Link).
  3. **Estudio QR Multi-Proyecto:** Generador de codigos QR de alta definicion (260px, 512px, 1024px) calibrado a la identidad cromatica del proyecto seleccionado.
  4. **Gestion de Seguridad:** Formulario para actualizar la clave maestra, generando automaticamente un nuevo salt y hash SHA-256.
  5. **Sincronizador JSON:** Herramienta para descargar o copiar [`redirects.json`](../redirects.json) para su posterior sincronizacion en Git.

---

### Modulo 3: Enrutador SPA de Redireccion Dinamica (`404.html`)

* **Ruta de Acceso:** [`404.html`](../404.html)
* **Proposito:** Resuelve rutas directas no compiladas en GitHub Pages y provee fallback instantaneo.
* **Comportamiento:**
  - Si la ruta solicitada es `admin`, redirige de inmediato a `admin/`.
  - Consulta `redirects.json` dinamicamente para resolver cualquier slug nuevo sin requerir carpetas fisicas inmediatas.
  - En caso de inexistencia, despliega pantalla de contingencia con boton de retorno.

---

### Modulo 4: Registro Centralizado Multi-Proyecto (`redirects.json`)

* **Ruta de Acceso:** [`redirects.json`](../redirects.json)
* **Esquema de Datos (Version 2.0.0):**
  - `schema_version`: Version del esquema (`2.0.0`).
  - `base_url`: Dominio canonico en GitHub Pages.
  - `default_project`: Proyecto raiz predeterminado (`nox`).
  - `security`: Parametros de autenticacion (`admin_salt`, `admin_hash`, `session_timeout_minutes`).
  - `projects`: Diccionario estructurado donde cada clave es el ID de un proyecto (ej. `nox`), conteniendo:
    - `id`, `name`, `tagline`.
    - `theme`: Propiedades CSS (`bg`, `card`, `primary`, `cyan`, `border`, `logo`).
    - `links`: Coleccion de objetos de enlace con banderas `is_public`, `highlight` e `is_active`.
  - `redirects`: Matriz plana universal de todos los slugs del sistema para soporte transparente de enrutamiento estatico y dinámico.

---

### Modulo 5: Asistente CLI en Python (`manager.py`)

* **Ruta de Acceso:** [`manager.py`](../manager.py)
* **Capacidades Operativas:**
  - `python manager.py --build`: Compila automaticamente las carpetas fisicas (`<slug>/index.html`) para todos los enlaces registrados, preservando la carpeta `admin/`.
  - `python manager.py --list`: Despliega tabla formateada en consola indicando: Proyecto, Alias, Tipo (Publico/Privado), URL Corta y Destino Real.
  - `python manager.py --add <slug> <url> <title> [--project <id>] [--private]`: Registra un enlace en el proyecto deseado indicando si es publico o privado.
  - `python manager.py --qr-all`: Genera codigos QR en alta definicion incrustando el logotipo circular.

---

## 3. Bitacora de Evolucion y Versiones

### Version 2.0.0 (10 de Noviembre de 2026) - Generalizacion Multi-Proyecto y Blindaje de Seguridad

* **Objetivo:** Transformar la suite en un contenedor multi-proyecto generico, proteger la consola administrativa bajo barrera criptografica y segregar estrictamente los enlaces publicos de los accesos gerenciales privados.
* **Problemas Abordados:**
  1. `admin.html` era accesible de forma publica sin ninguna restriccion para cualquier visitante.
  2. Enlaces operativos privados (base de datos en Google Sheets y editor de Google Apps Script) estaban expuestos en la interfaz publica principal.
  3. El repositorio estaba atado a una unica estetica y un unico proyecto sin capacidad de manejar otras marcas.
* **Acciones Implementadas:**
  1. **Barrera Criptografica Gerencial (`admin/`):**
     - Creacion del modulo [`admin/index.html`](../admin/index.html) con pantalla de bloqueo mandatoria impulsada por SHA-256 + salt mediante Web Crypto API.
     - Redireccion de contingencia desde [`admin.html`](../admin.html) y [`404.html`](../404.html) hacia `admin/`.
     - Gestion de sesion segura en `sessionStorage` con expiracion automatica y boton de bloqueo forzado.
  2. **Arquitectura Multi-Proyecto:**
     - Actualizacion del esquema de datos [`redirects.json`](../redirects.json) a version 2.0.0, soportando diccionario de `projects` independientes con sus propios colores, logos, tipografias y enlaces.
     - Adaptacion del portal publico [`index.html`](../index.html) para auto-configurarse reactivamente mediante parametro `?p=<slug>`.
     - Herramienta visual en la consola para registrar nuevos proyectos y personalizar marcas.
  3. **Segregacion de Privacidad (Cero Fugas de Datos Operativos):**
     - Clasificacion binaria de enlaces: `is_public: true` (mostrados en Bio Link) vs `is_public: false` (ocultos al cliente, solo visibles en panel gerencial).
     - Remocion completa de `db` y `editor` del portal publico [`index.html`](../index.html).
     - Remocion total de cualquier enlace al panel administrativo en el pie de pagina publico.
     - Incorporacion de atajo secreto de 5 toques sobre el logotipo para acceso rapido del propietario.
  4. **Actualizacion del Motor CLI (`manager.py`):**
     - Soporte para flags `--project` y `--private`.
     - Actualizacion de la funcion `list_links()` para mostrar proyecto y clasificacion Publico/Privado.
     - Proteccion explicita para evitar sobreescribir la carpeta `admin/` durante `build`.
* **Verificacion:**
  - Verificacion exitosa de compilacion con `python manager.py --build` (5 carpetas compiladas).
  - Verificacion exitosa de listado con `python manager.py --list`.
  - Generacion exitosa de codigos QR con incrustacion de logotipo para los 5 enlaces.
  - 0 errores de sintaxis y cumplimiento estricto del canon Cero Emojis.

---

### Version 1.0.0 (10 de Noviembre de 2026) - Lanzamiento Inicial y Desacoplamiento

* **Objetivo:** Creacion y publicacion de un repositorio autonomo e independiente para enlaces cortos y utilidades operativas de NOX en [`https://github.com/Velasco-Dev/links`](https://github.com/Velasco-Dev/links).
* **Acciones Implementadas:** Desacoplamiento de scripts internos, enrutamiento dual en GitHub Pages, creacion de `index.html`, `admin.html` inicial y `manager.py`.

---

## 4. Guia de Operacion y Despliegue Continuo

### Flujo de Publicacion de Cambios:

1. **Desde la Consola Gerencial Web (`/admin/`):**
   - Accede a `https://velasco-dev.github.io/links/admin/`.
   - Ingresa tu clave maestra.
   - Agrega o edita enlaces seleccionando si son publicos o privados.
   - En la pestana "Sincronizar & Git", haz clic en "Descargar redirects.json" (o copia su contenido).

2. **Compilacion y Despliegue en GitHub Pages:**
   ```powershell
   # 1. Compilar carpetas de redireccion
   python manager.py --build

   # 2. Subir a GitHub
   git add .
   git commit -m "Actualizar enlaces y configuracion multi-proyecto"
   git push origin main
   ```
   En menos de un minuto los cambios estaran en vivo en produccion.
