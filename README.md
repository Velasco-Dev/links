# NOX Links Suite | Enlaces Oficiales, Redirecciones & Consola Multi-Proyecto

> **Repositorio Oficial:** [https://github.com/Velasco-Dev/links](https://github.com/Velasco-Dev/links)  
> **Portal Publico de Marca:** [https://velasco-dev.github.io/links/](https://velasco-dev.github.io/links/)  
> **Consola Gerencial Privada:** Acceso restringido bajo autenticacion en `/admin/`

Suite de alta velocidad para la gestion centralizada de enlaces cortos, portales de marca moviles (Bio Link) para redes sociales, generacion de codigos QR de alta definicion y administracion multi-proyecto protegida criptograficamente para **NOX Slush & Beats** y futuras marcas satelite.

---

## 1. Caracteristicas Principales

1. **Arquitectura Multi-Proyecto en un Mismo Contenedor:**
   - Soporte para multiples marcas y proyectos simultaneos dentro del mismo repositorio de GitHub Pages.
   - Cada proyecto cuenta con su propia identidad visual (paleta de colores, logotipo, tipografias), su propio catalogo de enlaces y su propia configuracion.
   - Proyecto predeterminado en la raiz (`https://velasco-dev.github.io/links/`) y proyectos secundarios accesibles dinamicamente via `?p=slug`.

2. **Segregacion Estricta de Enlaces (Publico vs Privado/Gerencial):**
   - **Enlaces Publicos:** Unicamente los canales de cara al cliente (Menu Digital, Instagram oficial, WhatsApp) se visualizan en el portal de marca.
   - **Enlaces Privados / Gerenciales:** Accesos operativos a bases de datos (Google Sheets) y entornos de desarrollo (Google Apps Script) se mantienen completamente ocultos al publico y solo son visibles/gestionables en la consola gerencial.

3. **Consola Gerencial Privada con Barrera Criptografica (`admin/`):**
   - Ubicada de forma privada en `/admin/` (sin ningun boton o enlace publico expuesto en el portal principal).
   - Bloqueo criptografico basado en SHA-256 con salt. La sesion activa reside en `sessionStorage` y expira automaticamente al cerrar la pestana.
   - Gestion completa de proyectos, modificacion de estilos en vivo, conmutador de temas (Dark/Light) y generador de codigos QR calibrado a los colores de cada marca.
   - Atajo secreto de acceso de propietario disponible haciendo 5 toques rapidos consecutivos sobre el logotipo circular del portal publico.

4. **Motor CLI en Python (`manager.py`):**
   - Compila automaticamente las carpetas fisicas de redireccion (`<slug>/index.html`) para garantizar respuesta HTTP 200 directa.
   - Genera codigos QR en lote con incrustacion de logotipo y mascara circular de proteccion.
   - Identifica y lista enlaces distinguiendo su visibilidad publica o privada.

---

## 2. Catalogo de Enlaces de NOX Slush & Beats

| Alias | Enlace Corto en GitHub | Destino Real | Visibilidad |
| :--- | :--- | :--- | :--- |
| `/menu` | [velasco-dev.github.io/links/menu](https://velasco-dev.github.io/links/menu) | Menu Digital & Web App Oficial (GAS) | Publico |
| `/ig` | [velasco-dev.github.io/links/ig](https://velasco-dev.github.io/links/ig) | Instagram Oficial @noxslushnbeats | Publico |
| `/wa` | [velasco-dev.github.io/links/wa](https://velasco-dev.github.io/links/wa) | WhatsApp Oficial & Cotizaciones | Publico |
| `/db` | [velasco-dev.github.io/links/db](https://velasco-dev.github.io/links/db) | Base de Datos Sheets (7 Pestanas) | Privado / Gerencial |
| `/editor` | [velasco-dev.github.io/links/editor](https://velasco-dev.github.io/links/editor) | Editor Cloud de Apps Script | Privado / Gerencial |

---

## 3. Guia Operativa de Sincronizacion

Cada vez que realices cambios en los enlaces o en la consola administrativa:

```powershell
# 1. Compilar carpetas fisicas de redireccion
python manager.py --build

# 2. Generar codigos QR (opcional)
python manager.py --qr-all

# 3. Publicar en GitHub Pages
git add .
git commit -m "Actualizar suite multi-proyecto y configuracion de seguridad"
git push origin main
```
