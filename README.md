# NOX Links Suite | Enlaces Oficiales, Redirecciones & Consola Multi-Proyecto

> **Repositorio Oficial:** [https://github.com/Velasco-Dev/links](https://github.com/Velasco-Dev/links)  
> **Directorio Maestro de Proyectos:** [https://velasco-dev.github.io/links/](https://velasco-dev.github.io/links/)  
> **Portal Oficial NOX Slush & Beats:** [https://velasco-dev.github.io/links/nox/](https://velasco-dev.github.io/links/nox/)  
> **Consola Gerencial Privada:** Acceso restringido bajo autenticacion en `/admin/`

Suite de alto rendimiento para la gestion centralizada de enlaces cortos, portales de marca moviles (Bio Link), generacion de codigos QR y administracion multi-empresa protegida criptograficamente para **NOX Slush & Beats** y futuras marcas satelite.

---

## 1. Arquitectura de Rutas del Repositorio

La suite opera bajo un esquema jerarquico y modular:

1. **Directorio Maestro de Marcas (`/links/`):**
   * Es la base central de la plataforma (`https://velasco-dev.github.io/links/`). Muestra las tarjetas de todas las marcas y proyectos registrados con su respectivo logo, descripcion y acceso a su portal.

2. **Portal Bio Link por Empresa (`/links/<proyecto>/`):**
   * Cada marca tiene su propio portal independiente con su propia identidad visual, logotipo, paleta cromatica y listado exclusivo de enlaces publicos:
     * Portal NOX: `https://velasco-dev.github.io/links/nox/`
     * Portal Empresa X: `https://velasco-dev.github.io/links/xproyecto/`

3. **Enlaces Cortos por Empresa (`/links/<proyecto>/<slug>`):**
   * Cada enlace corto se encuentra estrictamente organizado dentro de la ruta de su proyecto:
     * `https://velasco-dev.github.io/links/nox/menu` -> Redirige al Menu Digital
     * `https://velasco-dev.github.io/links/nox/ig` -> Redirige al Instagram Oficial
     * `https://velasco-dev.github.io/links/nox/wa` -> Redirige a WhatsApp Oficial
     * `https://velasco-dev.github.io/links/xproyecto/catalogo` -> Redirige al catalogo de X proyecto

4. **Consola Gerencial Privada (`/links/admin/`):**
   * Acceso exclusivo del propietario protegido por barrera criptografica (SHA-256 + salt).
   * Creador de nuevos proyectos y subida directa de logos de nuevas empresas desde archivo (PNG, JPG, WebP o SVG con optimizacion automatica).
   * Sincronizacion en tiempo real con GitHub REST API para commits automaticos en la nube.

---

## 2. Catalogo de Enlaces de NOX Slush & Beats

| Alias | Enlace Corto Oficial | Destino Real | Visibilidad |
| :--- | :--- | :--- | :--- |
| `/nox/menu` | [velasco-dev.github.io/links/nox/menu](https://velasco-dev.github.io/links/nox/menu) | Menu Digital & Web App Oficial (GAS) | Publico |
| `/nox/ig` | [velasco-dev.github.io/links/nox/ig](https://velasco-dev.github.io/links/nox/ig) | Instagram Oficial @noxslushnbeats | Publico |
| `/nox/wa` | [velasco-dev.github.io/links/nox/wa](https://velasco-dev.github.io/links/nox/wa) | WhatsApp Oficial & Cotizaciones | Publico |
| `/nox/db` | [velasco-dev.github.io/links/nox/db](https://velasco-dev.github.io/links/nox/db) | Base de Datos Sheets (7 Pestanas) | Privado / Gerencial |
| `/nox/editor` | [velasco-dev.github.io/links/nox/editor](https://velasco-dev.github.io/links/nox/editor) | Editor Cloud de Apps Script | Privado / Gerencial |

---

## 3. Guia Operativa de Sincronizacion

Cada vez que agregues o edites proyectos en local:

```powershell
# 1. Compilar portales y carpetas de redireccion
python manager.py --build

# 2. Generar codigos QR (opcional)
python manager.py --qr-all

# 3. Publicar en GitHub Pages
git add .
git commit -m "Actualizar portales y enlaces de proyectos"
git push origin main
```
