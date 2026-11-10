# Bitacora Tecnica y Control de Modulos | NOX Links Suite

> **Documento de Control y Especificacion Tecnica:** Este archivo documenta de forma exhaustiva la arquitectura, especificacion modulo a modulo, registro evolutivo y directrices de mantenimiento del repositorio autonomo [`Velasco-Dev/links`](https://github.com/Velasco-Dev/links), desplegado en produccion mediante GitHub Pages en [`https://velasco-dev.github.io/links/`](https://velasco-dev.github.io/links/).

---

## 1. Justificacion Estrategica y Vision de Negocio

El proyecto insignia **NOX Slush & Beats** y sus aplicaciones satelite en Google Cloud y Google Apps Script requieren canales de acceso rapidos, cortos, confiables y con estetica de marca para interactuar con clientes, trabajadores y administradores:

1. **Eliminacion de Intermediarios con Publicidad:** Plataformas comerciales como Bitly o Linktree imponen pantallas intermedias, anuncios invasivos, limites mensuales y costos recurrentes. NOX Links Suite resuelve el 100% de los accesos de forma directa e instantanea.
2. **Optimizacion para Redes Sociales (Instagram Bio):** La URL oficial `https://velasco-dev.github.io/links/menu` tiene una longitud de solo 42 caracteres, siendo sumamente estetica y legible en biografias de redes sociales, mensajes directos de WhatsApp y material impreso.
3. **Optimizacion de Codigos QR:** Cuanto mas corta es la URL destino codificada, menor es la densidad de modulos del codigo QR. Esto incrementa de forma notable la velocidad y tolerancia de lectura de los codigos impresos en acrilicos de mesa, vasos y servilletas en condiciones de iluminacion nocturna.
4. **Independencia de Servidores Locales:** Al operar sobre la infraestructura global de **GitHub Pages**, los enlaces estan en linea las 24 horas del dia los 365 dias del ano, sin necesidad de mantener encendida una computadora personal ni pagar hosting dedicado.

---

## 2. Desglose Modulo a Modulo del Repositorio

A continuacion se describe en detalle cada archivo, directorio y subsistema que conforma el proyecto:

```
G:\Ingenieria Informatica\Git Externo\links/
├── index.html              <-- Modulo 1: Portal Publico de Marca (Bio Link)
├── admin.html              <-- Modulo 2: Consola de Administracion & QR Studio
├── 404.html                <-- Modulo 3: Enrutador SPA de Redireccion Dinamica
├── redirects.json          <-- Modulo 4: Base de Datos Centralizada de Redirecciones
├── manager.py              <-- Modulo 5: Asistente CLI en Python (Compilador & QR Engine)
├── menu/index.html         <-- Modulo 6A: Redireccion Estatica Directa hacia Menu Digital (GAS)
├── db/index.html           <-- Modulo 6B: Redireccion Estatica Directa hacia Base de Datos (Sheets)
├── editor/index.html       <-- Modulo 6C: Redireccion Estatica Directa hacia Editor Apps Script
├── ig/index.html           <-- Modulo 6D: Redireccion Estatica Directa hacia Instagram Oficial
├── assets/                 <-- Modulo 7: Activos de Identidad Visual y QR
│   ├── logo.jpeg           (Logotipo oficial circular de NOX)
│   └── qrs/                (Codigos QR exportados en alta definicion)
├── requirements.txt        <-- Modulo 8A: Dependencias de Python (colorama, qrcode, pillow)
├── .gitignore              <-- Modulo 8B: Filtros de control de versiones
└── README.md               <-- Modulo 8C: Manual de usuario y guia de despliegue
```

---

### Modulo 1: Portal Publico de Marca (`index.html`)

* **Ruta de Acceso:** [`index.html`](../index.html)
* **URL en Produccion:** `https://velasco-dev.github.io/links/`
* **Proposito y Funcion:** Es la cara publica visible cuando un usuario ingresa directamente a la raiz del dominio. Funciona como un portal movil de enlaces (estilo *Linktree* personalizado), optimizado para smartphones y navegadores de escritorio.
* **Componentes Visuales:**
  - **Insignia de Marca:** Logotipo oficial circular de NOX (`assets/logo.jpeg`) con borde luminoso degradado en magenta (`#FF007F`) y cian (`#00F0FF`).
  - **Tipografia Corporativa:** Titulares en *Orbitron* (900 bold) y textos informativos en *Outfit*.
  - **Estetica Liquid Glass:** Fondo oscuro espacial (`#080114`) con gradientes radiales sutiles y tarjetas con desenfoque de fondo (`backdrop-filter: blur(10px)`).
  - **Botonera Directa con Iconos FontAwesome:**
    - Boton destacado magenta: *Menu Digital & Pedidos en Linea* (apunta a `menu/`).
    - Boton Instagram oficial (apunta a `ig/`).
    - Boton directo de atencion y cotizacion de eventos en WhatsApp (`https://wa.me/...`).
    - Botones operacionales hacia la base de datos de Google Sheets (`db/`) y editor de scripts (`editor/`).
  - **Pie de Pagina:** Enlace de acceso rapido a la consola de administracion (`admin.html`).

---

### Modulo 2: Consola de Administracion Unificada (`admin.html`)

* **Ruta de Acceso:** [`admin.html`](../admin.html)
* **Proposito y Funcion:** Centro de control privado ejecutable tanto en local (mediante doble clic o servidor local) como directamente en la web. Permite gestionar todo el ciclo de vida de los enlaces y generar codigos QR sin salir de la misma pantalla.
* **Secciones Principales (Pestanas de la Suite):**
  1. **Pestana 1 - Recortador & Catalogo de Enlaces:**
     - Formulario de captura de URL larga, alias corto (slug) con previsualizador en vivo del enlace de GitHub Pages y generador de slugs aleatorios seguros.
     - Tabla interactiva con buscador en tiempo real, opciones de copiado al portapapeles en un clic y exportacion de [`redirects.json`](../redirects.json) actualizado.
  2. **Pestana 2 - Generador de Codigos QR Avanzado:**
     - Integracion directa con `qrcodejs` en el navegador.
     - Paletas cromaticas calibradas: Neón Magenta (`#FF007F` sobre blanco), Clasico B&W (`#000000` sobre blanco) y Cian Electrico (`#00F0FF` sobre purpura oscuro `#080114`).
     - Selector de resolucion de imagen (260px para web, 512px para stickers y mesas, 1024px para pendones y lonas).
     - Descarga directa en formato PNG.
  3. **Pestana 3 - Guia de Despliegue en GitHub Pages:**
     - Manual interactivo paso a paso para sincronizar cambios mediante terminal y configurar el dominio.
  4. **Pestana 4 - Modulos Extensibles:**
     - Panel arquitectonico disenado para anadir futuras herramientas operativas (creador de firmas de correo, generador de codigos de barra, calculadora de mermas).
  - **Modo Claro / Modo Oscuro:** Selector persistente en `localStorage` con transicion cromatica suave.

---

### Modulo 3: Enrutador SPA de Redireccion Dinamica (`404.html`)

* **Ruta de Acceso:** [`404.html`](../404.html)
* **Proposito y Funcion:** En GitHub Pages, cualquier solicitud HTTP hacia una ruta que no exista fisicamente en el repositorio es dirigida automaticamente hacia `404.html`.
* **Mecanismo de Intercepcion en 3 Fases:**
  1. **Lectura de Ruta:** El script inline extrae el slug desde `window.location.pathname` (ejemplo: si el usuario entra a `.../links/verano`, detecta `verano`).
  2. **Copia de Respaldo Instantanea (Zero Latency):** Posee un diccionario en memoria con los presets criticos (`menu`, `db`, `editor`, `ig`) para redirigir de forma inmediata sin esperar peticiones de red.
  3. **Consulta Dinamica:** Si no esta en el diccionario basico, realiza un `fetch` en segundo plano a `redirects.json?v=...`. Si existe el alias, ejecuta `window.location.replace(match.url)`.
  4. **Pantalla de Contingencia:** En caso de que el enlace realmente no exista o haya sido eliminado, muestra una tarjeta informativa con diseno Cyberpunk y un boton para regresar al portal oficial (`index.html`).

---

### Modulo 4: Registro Centralizado de Redirecciones (`redirects.json`)

* **Ruta de Acceso:** [`redirects.json`](../redirects.json)
* **Estructura de Datos (Esquema JSON):**
  - `base_url`: Dominio canonico del repositorio (`https://velasco-dev.github.io/links`).
  - `updated_at`: Marca temporal ISO de la ultima modificacion.
  - `redirects`: Matriz de objetos que describen cada enlace:
    - `slug` (string): Identificador corto y unico.
    - `url` (string): URL completa de destino.
    - `title` (string): Nombre comercial o descriptivo del recurso.
    - `description` (string): Informacion auxiliar.
    - `category` (string): Clasificacion (`comercial`, `operaciones`, `desarrollo`, `social`).
    - `is_active` (boolean): Bandera de disponibilidad.

---

### Modulo 5: Asistente CLI en Python (`manager.py`)

* **Ruta de Acceso:** [`manager.py`](../manager.py)
* **Proposito y Funcion:** Motor utilitario para terminal en entornos Windows, Linux o macOS. Permite automatizar tareas por lotes antes de hacer commit en Git.
* **Capacidades Operativas:**
  - `python manager.py --build`: Lee [`redirects.json`](../redirects.json) y compila/actualiza automaticamente las carpetas fisicas (`<slug>/index.html`) con su respectiva meta-redireccion.
  - `python manager.py --qr-all`: Genera codigos QR en alta definicion con incrustacion de logotipo circular y placa protectora para cada enlace del registro, guardandolos en [`assets/qrs/`](../assets/qrs).
  - `python manager.py --add <slug> <url> <title>`: Registra un nuevo enlace y genera su carpeta fisica en un solo comando.
  - `python manager.py --list`: Muestra una tabla formateada en consola con los enlaces y sus rutas publicas en GitHub Pages.
  - Modo Interactivo: Si se ejecuta sin parametros (`python manager.py`), despliega un menu numerado interactivo con soporte de colorama.

---

### Modulo 6: Carpetas de Redireccion Estatica Directa

* **Carpetas Creadas:**
  - [`menu/index.html`](../menu/index.html) -> Web App Oficial de Google Apps Script (`.../dev` o `.../exec`).
  - [`db/index.html`](../db/index.html) -> Hoja de Calculo de Google Sheets.
  - [`editor/index.html`](../editor/index.html) -> Editor en la nube de Google Apps Script.
  - [`ig/index.html`](../ig/index.html) -> Perfil oficial en Instagram.
* **Mecanismo Tecnico:**  
  Cada archivo implementa una triple garantia de redireccion:
  1. `<meta http-equiv="refresh" content="0; url=...">` para compatibilidad nativa en navegadores antiguos o sin JavaScript activo.
  2. `<link rel="canonical" href="...">` para preservacion de SEO y correcta indexacion.
  3. `<script>window.location.replace("...");</script>` para transicion inmediata sin guardar la pagina intermedia en el historial de navegacion del usuario (el boton "Atras" del telefono funciona de forma natural).

---

### Modulo 7: Activos de Identidad Visual y QR (`assets/`)

* **Ruta de Acceso:** [`assets/`](../assets/)
* **Contenido:**
  - [`assets/logo.jpeg`](../assets/logo.jpeg): Logotipo oficial de NOX Slush & Beats, utilizado para el portal y para la incrustacion con mascara circular en los codigos QR.
  - [`assets/qrs/`](../assets/qrs): Directorio de almacenamiento de imagenes PNG generadas en alta definicion (ej. `qr_menu_neon.png`, `qr_db_neon.png`, etc.).

---

## 3. Bitacora de Evolucion y Versiones

### Version 1.0.0 (10 de Noviembre de 2026) - Lanzamiento Inicial y Desacoplamiento

* **Objetivo:** Creacion y publicacion de un repositorio autonomo e independiente para enlaces cortos y utilidades operativas de NOX en [`https://github.com/Velasco-Dev/links`](https://github.com/Velasco-Dev/links).
* **Acciones Implementadas:**
  1. **Desacoplamiento Estructural:** Creacion del directorio [`G:\Ingenieria Informatica\Git Externo\links`](file:///G:/Ingenieria%20Informatica/Git%20Externo/links) completamente desligado del repositorio de scripts internos de Google Apps Script.
  2. **Arquitectura Dual de Redireccion:**
     - Generacion de carpetas fisicas estaticas para los 4 enlaces criticos (`menu`, `db`, `editor`, `ig`) para garantizar HTTP 200 inmediato.
     - Implementacion del enrutador dinámico en [`404.html`](../404.html) conectado a [`redirects.json`](../redirects.json).
  3. **Portal Publico de Marca:** Diseno y desarrollo de [`index.html`](../index.html) como Linktree oficial con identidad visual Cyberpunk Liquid Glass.
  4. **Suite de Administracion:** Desarrollo de [`admin.html`](../admin.html) unificando acortador, tabla de gestion y generador de codigos QR con soporte para Modo Oscuro y Modo Claro.
  5. **Motor CLI en Python:** Creacion de [`manager.py`](../manager.py) con soporte de compilacion estatica por lotes y generacion de codigos QR con corte circular de logotipo.
  6. **Infraestructura de Documentacion:** Creacion del directorio [`Chats/`](README.md), subcarpeta [`Chats/artifacts/`](artifacts/) y bitacora maestra [`Chats/Links.md`](Links.md).
* **Verificacion:**
  - 0 errores de sintaxis en HTML, JavaScript y Python.
  - Canon Cero Emojis estrictamente verificado (0 ocurrencias).
  - Despliegue en GitHub Pages configurado a partir de la rama `main` en la raiz.

---

## 4. Guia de Operacion y Despliegue Continuo

### Como anadir un nuevo enlace y publicarlo en 3 pasos:

1. **Paso 1 (Crear enlace):**
   - Desde la interfaz web: Abre [`admin.html`](../admin.html), ingresa el alias (ejemplo: `promo`) y la URL de destino.
   - O desde consola:
     ```powershell
     python manager.py --add "promo" "https://tu-sitio.com/promo" "Promocion Especial"
     ```

2. **Paso 2 (Compilar carpetas de redireccion):**
   ```powershell
   python manager.py --build
   ```

3. **Paso 3 (Subir a GitHub):**
   ```powershell
   git add .
   git commit -m "Anadir nuevo enlace corto /promo"
   git push origin main
   ```
   En menos de 1 minuto el nuevo enlace estara disponible en:  
   `https://velasco-dev.github.io/links/promo`

---

## 5. Compromiso de Mantenimiento Continuo

Cada vez que se anada una nueva herramienta a la suite, se modifique la estructura de redirecciones o se incorporen nuevos activos visuales al repositorio [`Velasco-Dev/links`](https://github.com/Velasco-Dev/links), esta bitacora debe ser actualizada registrando la nueva version correspondiente en la Seccion 3.
