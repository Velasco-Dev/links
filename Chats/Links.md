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

### Version 2.2.1 (10 de Noviembre de 2026) - Parche de Estabilidad en Consola Gerencial (Cierre de Sintaxis JS)

* **Objetivo:** Subsanar error de sintaxis en `admin/index.html` que bloqueaba el parseo del script principal y la funcion de desbloqueo `handleUnlock()`.
* **Problemas Abordados:**
  1. Presencia de un bloque redundante de cierre `generatePreviewQr(); }` en la linea 1785 de `admin/index.html` que arrojaba `Uncaught SyntaxError: Unexpected token '}'`.
  2. Fallo en cascada que impedia la carga de `handleUnlock` arrojando `ReferenceError` al intentar ingresar la clave en la pantalla de bloqueo.
* **Acciones Implementadas:**
  - Remocion de las lineas duplicadas en `admin/index.html`.
  - Verificacion automatica con `node --check` para todos los bloques `<script>` de los modulos HTML del proyecto.
* **Verificacion:**
  - Validacion de sintaxis 100% exitosa con Node.js en `admin/index.html`, `index.html` y `404.html`.
  - Canon Cero Emojis comprobado.

---

### Version 2.2.0 (10 de Noviembre de 2026) - Directorio Maestro de Marcas, Enrutamiento Jerarquico por Proyecto y Cargador de Logos

* **Objetivo:** Transformar la raiz del repositorio en un Directorio Maestro de proyectos, organizar los enlaces bajo rutas jerarquicas estrictas (`/links/<proyecto>/<slug>`) e integrar un modulo de subida directa de logotipos para nuevas empresas.
* **Problemas Abordados:**
  1. La raiz mostraba unicamente a NOX y los demas proyectos dependian de parametros `?p=slug`, impidiendo que `/links/` funcionara como la base central del ecosistema.
  2. Los enlaces cortos no estaban anidados por proyecto (`/links/menu` en lugar de `/links/nox/menu`), impidiendo tener un enlace con el mismo alias para diferentes empresas (ej. `/nox/menu` y `/xproyecto/menu`).
  3. No existia una interfaz grafica para que el usuario pudiera subir el logotipo de una nueva empresa directamente desde su dispositivo (movil o PC).
* **Acciones Implementadas:**
  1. **Directorio Maestro de Marcas en la Raiz (`index.html`):**
     - Rediseño de [`index.html`](../index.html) como un Hub Maestro que consulta [`redirects.json`](../redirects.json) y despliega tarjetas visuales para cada marca registrada (logo circular, nombre, descripcion y boton de acceso directo `/links/<proyecto>/`).
     - Preservacion del atajo secreto de 5 clics hacia `/admin/` en el logo maestro.
  2. **Enrutamiento Jerarquico por Proyecto (`/links/<proyecto>/<slug>`):**
     - Actualizacion de [`manager.py`](../manager.py) para compilar sub-carpetas fisicas directas (`<proyecto>/<slug>/index.html`), permitiendo URLs limpias como `https://velasco-dev.github.io/links/nox/menu` y `https://velasco-dev.github.io/links/xproyecto/catalogo`.
     - Actualizacion del enrutador dinámico en [`404.html`](../404.html) para descomponer la ruta en 2 segmentos (`cleanSegments[0] = project`, `cleanSegments[1] = slug`) y resolver redirecciones en tiempo real para proyectos recien anadidos desde la web.
     - Preservacion de enlaces en la raiz para compatibilidad retroactiva.
  3. **Cargador y Optimizador de Logotipos en Consola Gerencial (`admin/index.html`):**
     - Incorporacion de selector de archivos `<input type="file">` tanto en el editor de marca activa como en el formulario de creacion de nuevos proyectos.
     - Funcion JavaScript `handleLogoUpload()` con compresion automatica en Canvas HTML5 (maximo 260x260 px en PNG) que transforma la imagen en Data URL Base64 de alta resolucion y bajo peso, guardandose directamente en [`redirects.json`](../redirects.json).
     - Previsualizador en vivo del logo circular tanto en la consola como al crear un nuevo proyecto.
* **Verificacion:**
  - Compilacion exitosa de 1 proyecto con 5 sub-enlaces fisicos (`/nox/menu/`, `/nox/ig/`, `/nox/wa/`, etc.) y 5 enlaces raiz de respaldo.
  - Verificacion de resolucion dinamica en `404.html` para rutas compuestas.
  - Cero emojis verificado en todo el codigo y documentacion.

---

### Version 2.1.0 (10 de Noviembre de 2026) - Base de Datos en Vivo (GitHub Cloud API) y Rutas Fisicas Multi-Proyecto

* **Objetivo:** Resolver la persistencia en tiempo real en GitHub Pages permitiendo guardar cambios directamente desde la aplicacion web y habilitar rutas de acceso fisicas directas (`/links/nox`, `/links/<xproyecto>`).
* **Problemas Abordados:**
  1. Al editar un enlace desde la app desplegada, el cambio solo se guardaba en el `localStorage` del dispositivo local y no se reflejaba en el repositorio ni en produccion (debido a la naturaleza estatica de GitHub Pages).
  2. Necesidad de rutas independientes por proyecto (`links/nox`, `links/xproyecto`) en lugar de depender exclusivamente de query parameters (`?p=slug`).
* **Acciones Implementadas:**
  1. **Sincronizacion en Vivo con GitHub REST API:**
     - Integracion del cliente GitHub Contents API (`PUT /repos/Velasco-Dev/links/contents/redirects.json`) dentro de [`admin/index.html`](../admin/index.html).
     - Almacenamiento seguro del Personal Access Token (PAT) en el navegador del administrador.
     - Boton de cabecera "Publicar en GitHub" que realiza commits reales en la rama `main` en tiempo real sin requerir terminal.
  2. **Rutas Fisicas de Proyectos (`/links/nox/` y `/links/<xproyecto>/`):**
     - Actualizacion de [`manager.py`](../manager.py) para compilar no solo los slugs de redireccion sino tambien los portales fisicos de cada proyecto registrado (`nox/index.html`, `<xproyecto>/index.html`).
     - Adaptacion del enrutador dinámico en [`404.html`](../404.html) para detectar proyectos no compilados y redirigir inmediatamente a su portal.
     - Deteccion automatica en [`index.html`](../index.html) tanto por path `/links/<proyecto>/` como por parametro `?p=<slug>`.
* **Verificacion:**
  - Compilacion exitosa de `/nox/index.html` mediante `python manager.py --build`.
  - Integracion probada de `b64` encoding UTF-8 y conexion con API de GitHub.
  - Cero emojis preservado estrictamente en todo el repositorio.

---

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
