# NOX Links Suite | Enlaces Oficiales, Redirecciones & Generador de QR

> **Repositorio Oficial de Enlaces:** [https://github.com/Velasco-Dev/links](https://github.com/Velasco-Dev/links)  
> **Portal Publico en Vivo:** [https://velasco-dev.github.io/links/](https://velasco-dev.github.io/links/)

Suite unificada para acortar enlaces hacia aplicaciones web (como Google Apps Script), gestionar el portal movil de marca para Instagram y generar codigos QR en alta definicion con la identidad visual Cyberpunk de **NOX Slush & Beats**.

---

## 1. Caracteristicas Principales

1. **Redirecciones Ultrarrapidas sin Servidor:**
   - Alojado 100% en GitHub Pages: cero costos, cero publicidad y disponibilidad 24/7 en todo el mundo.
   - Enlaces cortos limpios para Instagram, WhatsApp o material impreso: `https://velasco-dev.github.io/links/<alias>`.
   - Redireccion instantanea con soporte dual: carpetas fisicas (`<alias>/index.html`) y enrutador SPA (`404.html` + `redirects.json`).

2. **Portal Publico de Marca (`index.html`):**
   - Pagina de inicio tipo Bio Link / Linktree con botones oficiales para acceder al Menú Digital, Instagram, WhatsApp y Base de Datos.
   - Diseno responsivo con efecto desenfoque Liquid Glass y tipografias Orbitron y Outfit.

3. **Consola de Administracion Unificada (`admin.html`):**
   - Recortador de enlaces interactivo con generador de slugs aleatorios.
   - Generador y visor de codigos QR con selector de paletas (Neón Magenta, Clasico B&W, Cian Electrico) y descarga en PNG.
   - Modo Claro y Modo Oscuro integrados.
   - Modulo extensible para futuras utilidades operativas.

4. **Motor CLI en Python (`manager.py`):**
   - Compila automaticamente todas las carpetas de redireccion a partir de `redirects.json`.
   - Genera codigos QR en lote con incrustacion de logotipo circular.

---

## 2. Enlaces Oficiales Preconfigurados

| Alias | Enlace Publico en GitHub | Destino Oficial |
| :--- | :--- | :--- |
| `/menu` | [https://velasco-dev.github.io/links/menu](https://velasco-dev.github.io/links/menu) | Web App & Menu Digital de NOX (Google Apps Script) |
| `/db` | [https://velasco-dev.github.io/links/db](https://velasco-dev.github.io/links/db) | Base de Datos Central Google Sheets (7 Pestanas) |
| `/editor` | [https://velasco-dev.github.io/links/editor](https://velasco-dev.github.io/links/editor) | Editor de Codigo Google Apps Script |
| `/ig` | [https://velasco-dev.github.io/links/ig](https://velasco-dev.github.io/links/ig) | Perfil Oficial de Instagram @noxslushnbeats |

---

## 3. Pasos para Publicar en GitHub Pages

Para conectar esta carpeta con tu repositorio en GitHub y poner los enlaces en vivo para todo el planeta:

### Paso 1: Subir los archivos a GitHub

Abre PowerShell en la carpeta `G:\Ingenieria Informatica\Git Externo\links` y ejecuta:

```powershell
git init
git remote add origin https://github.com/Velasco-Dev/links.git
git add .
git commit -m "Inicializar suite de enlaces NOX y redirecciones GitHub Pages"
git branch -M main
git push -u origin main
```

*(Si ya tenias el repositorio clonado o inicializado, simplemente haz `git add .`, `git commit -m "..."` y `git push`)*.

### Paso 2: Activar GitHub Pages en el Repositorio

1. Entra a tu repositorio en GitHub: [https://github.com/Velasco-Dev/links](https://github.com/Velasco-Dev/links)
2. Haz clic en la pestaña **Settings** (en la barra superior).
3. En el menu de la izquierda, entra a **Pages**.
4. En **Build and deployment > Branch**:
   - Selecciona la rama **main**.
   - Selecciona la carpeta **/ (root)**.
5. Haz clic en el botón **Save**.

En menos de un minuto tu portal estara activo en `https://velasco-dev.github.io/links/` y cualquier persona que entre a `https://velasco-dev.github.io/links/menu` saltara de inmediato a tu aplicacion de Google Apps Script.

---

## 4. Uso del Asistente Python (`manager.py`)

```powershell
# Compilar todas las carpetas de redireccion
python manager.py --build

# Generar todos los codigos QR en alta resolucion
python manager.py --qr-all

# Listar enlaces registrados
python manager.py --list

# Agregar un nuevo enlace
python manager.py --add "promo" "https://tu-sitio.com/promo" "Promocion Especial"
```
