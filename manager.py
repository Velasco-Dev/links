#!/usr/bin/env python3
"""
================================================================================
PROYECTO: NOX Links Suite
REPOSITORIO: https://github.com/Velasco-Dev/links
ARCHIVO: manager.py
DESCRIPCION: Asistente CLI para compilar redirecciones estaticas para GitHub Pages,
             gestionar enlaces multi-proyecto en redirects.json y generar codigos QR.
================================================================================
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Configuracion de codificacion UTF-8 para Windows
if sys.platform == "win32":
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
REDIRECTS_JSON = BASE_DIR / "redirects.json"
ASSETS_DIR = BASE_DIR / "assets"
QRS_DIR = ASSETS_DIR / "qrs"
LOGO_PATH = ASSETS_DIR / "logo.jpeg"

QRS_DIR.mkdir(parents=True, exist_ok=True)

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class DummyColor:
        def __getattr__(self, name): return ""
    Fore = DummyColor()
    Style = DummyColor()

try:
    import qrcode
    from PIL import Image, ImageDraw
    QR_ENABLED = True
except ImportError:
    QR_ENABLED = False


def load_redirects_data():
    if not REDIRECTS_JSON.exists():
        return {
            "schema_version": "2.0.0",
            "base_url": "https://velasco-dev.github.io/links",
            "default_project": "nox",
            "projects": {},
            "redirects": []
        }
    with open(REDIRECTS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def save_redirects_data(data):
    with open(REDIRECTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_folder_redirect(slug, target_url, title):
    # Evitar sobreescribir la carpeta administrativa si se llama 'admin'
    if slug == "admin":
        return BASE_DIR / "admin" / "index.html"

    folder = BASE_DIR / slug
    folder.mkdir(parents=True, exist_ok=True)
    index_file = folder / "index.html"

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target_url}">
  <link rel="canonical" href="{target_url}">
  <title>Redirigiendo a {title}...</title>
  <script>window.location.replace("{target_url}");</script>
  <style>
    body {{ background-color: #080114; color: #F8FAFC; font-family: system-ui, -apple-system, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
    .card {{ text-align: center; padding: 2.5rem; background: rgba(18, 7, 43, 0.9); border: 1px solid rgba(255, 0, 127, 0.35); border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.6); max-width: 480px; width: 90%; }}
    .spinner {{ width: 36px; height: 36px; border: 3px solid rgba(0, 240, 255, 0.2); border-top-color: #00F0FF; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 1.5rem auto; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    h2 {{ font-size: 1.4rem; color: #FF007F; margin-bottom: 0.5rem; }}
    p {{ color: #94A3B8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 1.5rem; }}
    a {{ display: inline-block; padding: 0.75rem 1.5rem; background: linear-gradient(135deg, #FF007F 0%, #C70062 100%); color: #FFF; text-decoration: none; font-weight: 700; border-radius: 12px; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="spinner"></div>
    <h2>Redirigiendo a {title}</h2>
    <p>Abriendo enlace oficial...</p>
    <a href="{target_url}">Haz clic aqui si no eres redirigido</a>
  </div>
</body>
</html>
"""
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    return index_file


def generate_project_portal(proj_id, proj_data, base_url):
    if proj_id == "admin":
        return BASE_DIR / "admin" / "index.html"

    folder = BASE_DIR / proj_id
    folder.mkdir(parents=True, exist_ok=True)
    index_file = folder / "index.html"

    name = proj_data.get("name", proj_id.upper())
    tagline = proj_data.get("tagline", "")
    theme = proj_data.get("theme", {})
    bg = theme.get("bg", "#080114")
    card = theme.get("card", "rgba(18, 7, 43, 0.85)")
    primary = theme.get("primary", "#FF007F")
    cyan = theme.get("cyan", "#00F0FF")
    border = theme.get("border", "rgba(255, 0, 127, 0.25)")
    logo = theme.get("logo", "assets/logo.jpeg")
    if not logo.startswith("http") and not logo.startswith("../"):
        logo = f"../{logo}"

    links = proj_data.get("links", [])
    public_links = [l for l in links if l.get("is_public", True) and l.get("is_active", True) is not False]

    buttons_html = ""
    for l in public_links:
        slug = l.get("slug", "")
        url = l.get("url", "")
        title = l.get("title", slug)
        desc = l.get("description", "")
        icon = l.get("icon", "fa-solid fa-link")
        highlight = l.get("highlight", False)
        
        target_href = url if (url.startswith("http") or url.startswith("mailto:") or url.startswith("tel:")) else f"../{slug}/"
        target_attr = 'target="_blank" rel="noopener noreferrer"' if url.startswith("http") else ''
        hl_class = " highlight" if highlight else ""
        icon_style = '' if highlight else 'style="color: var(--cyan);"'

        buttons_html += f"""
      <a href="{target_href}" {target_attr} class="link-btn{hl_class}">
        <div class="link-icon" {icon_style}><i class="{icon}"></i></div>
        <div class="link-content">
          <div class="link-title">{title}</div>
          <div class="link-desc">{desc}</div>
        </div>
        <div class="link-arrow"><i class="fa-solid fa-chevron-right"></i></div>
      </a>
"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} | Enlaces Oficiales</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {{
      --bg: {bg};
      --card: {card};
      --primary: {primary};
      --cyan: {cyan};
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --border: {border};
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: var(--bg);
      background-image: 
        radial-gradient(circle at 10% 20%, rgba(255, 0, 127, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(0, 240, 255, 0.15) 0%, transparent 45%);
      color: var(--text);
      font-family: 'Outfit', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2.5rem 1.25rem;
    }}
    .portal-card {{ width: 100%; max-width: 480px; text-align: center; }}
    .brand-logo-frame {{
      width: 110px; height: 110px; margin: 0 auto 1.5rem auto; border-radius: 50%; padding: 4px;
      background: linear-gradient(135deg, var(--primary) 0%, var(--cyan) 100%);
      box-shadow: 0 0 25px rgba(255, 0, 127, 0.4); display: flex; align-items: center; justify-content: center;
    }}
    .brand-logo-frame img {{ width: 100%; height: 100%; border-radius: 50%; object-fit: cover; background: #080114; }}
    h1 {{
      font-family: 'Orbitron', sans-serif; font-size: 1.8rem; font-weight: 900; letter-spacing: 2px;
      background: linear-gradient(135deg, #FFF 20%, var(--cyan) 70%, var(--primary) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;
    }}
    .tagline {{ font-size: 0.95rem; color: var(--text-muted); margin-bottom: 2rem; line-height: 1.5; white-space: pre-line; }}
    .links-list {{ display: flex; flex-direction: column; gap: 1rem; margin-bottom: 2.5rem; }}
    .link-btn {{
      display: flex; align-items: center; padding: 1rem 1.25rem; background: var(--card);
      border: 1.5px solid var(--border); border-radius: 16px; color: var(--text); text-decoration: none;
      transition: all 0.25s ease; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4); backdrop-filter: blur(10px);
    }}
    .link-btn:hover {{ transform: translateY(-2px); border-color: var(--cyan); box-shadow: 0 10px 28px rgba(0, 240, 255, 0.25); }}
    .link-btn.highlight {{
      border-color: var(--primary);
      background: linear-gradient(135deg, rgba(255, 0, 127, 0.18) 0%, rgba(18, 7, 43, 0.85) 100%);
    }}
    .link-icon {{
      width: 44px; height: 44px; border-radius: 12px; background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1); display: flex; align-items: center; justify-content: center;
      font-size: 1.2rem; flex-shrink: 0; margin-right: 1rem;
    }}
    .link-content {{ text-align: left; flex: 1; }}
    .link-title {{ font-weight: 700; font-size: 1rem; color: var(--text); margin-bottom: 0.2rem; }}
    .link-desc {{ font-size: 0.8rem; color: var(--text-muted); }}
    .link-arrow {{ color: var(--cyan); font-size: 0.95rem; opacity: 0.7; }}
    footer {{ font-size: 0.82rem; color: var(--text-muted); border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1.5rem; }}
  </style>
</head>
<body>
  <div class="portal-card">
    <div class="brand-logo-frame">
      <img src="{logo}" alt="Logo de Marca" onerror="this.src='https://via.placeholder.com/150/12072b/00f0ff?text={proj_id}'">
    </div>
    <h1>{name}</h1>
    <p class="tagline">{tagline}</p>
    <div class="links-list">
      {buttons_html}
    </div>
    <footer>
      <span>{name} &copy; 2026 | Canales Oficiales</span>
    </footer>
  </div>
</body>
</html>
"""
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html)
    return index_file


def build_all_redirects():
    data = load_redirects_data()
    base_url = data.get("base_url", "https://velasco-dev.github.io/links")
    redirects = data.get("redirects", [])
    projects = data.get("projects", {})
    count_slugs = 0
    count_projects = 0

    print(f"\n{Fore.CYAN}Compilando portales de proyectos y carpetas de redireccion...{Style.RESET_ALL}")

    # 1. Compilar portales fisicos para cada proyecto registrado (ej. /nox/index.html)
    for p_id, p_data in projects.items():
        if p_id != "admin":
            generate_project_portal(p_id, p_data, base_url)
            print(f"  [+] Portal de Proyecto compilado: /{p_id}/index.html ({p_data.get('name', p_id)})")
            count_projects += 1
    
    # 2. Extraer y compilar slugs unicos de redireccion
    seen = set()
    for item in redirects:
        slug = item.get("slug")
        url = item.get("url")
        title = item.get("title", slug)
        if slug and url and slug not in seen and slug != "admin" and slug not in projects:
            generate_folder_redirect(slug, url, title)
            is_pub = "Publico" if item.get("is_public", True) else "Privado"
            print(f"  [+] Redireccion compilada: /{slug}/index.html [{is_pub}] -> {url}")
            seen.add(slug)
            count_slugs += 1

    print(f"{Fore.GREEN}[OK] Se compilaron {count_projects} portales de proyecto y {count_slugs} rutas de redireccion.{Style.RESET_ALL}\n")


def generate_qr(text, filename, style="nox_neon"):
    if not QR_ENABLED:
        print(f"{Fore.RED}[ERROR] qrcode y pillow no estan instalados.{Style.RESET_ALL}")
        return None

    palettes = {
        "nox_neon": ("#FF007F", "#FFFFFF"),
        "classic": ("#000000", "#FFFFFF"),
        "nox_cyan": ("#00F0FF", "#080114")
    }
    fg, bg = palettes.get(style, ("#FF007F", "#FFFFFF"))

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg, back_color=bg).convert("RGBA")

    # Incrustar logo si existe
    if LOGO_PATH.exists():
        try:
            logo = Image.open(str(LOGO_PATH)).convert("RGBA")
            qw, qh = img.size
            logo_max = int(qw * 0.22)
            logo.thumbnail((logo_max, logo_max), Image.Resampling.LANCZOS)
            lw, lh = logo.size

            mask = Image.new("L", (lw, lh), 0)
            draw_m = ImageDraw.Draw(mask)
            draw_m.ellipse((0, 0, lw, lh), fill=255)

            badge_pad = 6
            badge_size = (lw + badge_pad * 2, lh + badge_pad * 2)
            badge = Image.new("RGBA", badge_size, (0, 0, 0, 0))
            draw_b = ImageDraw.Draw(badge)
            badge_bg = (255, 255, 255, 255) if style != "nox_cyan" else (8, 1, 20, 255)
            badge_border = (200, 200, 200, 255) if style != "nox_cyan" else (0, 240, 255, 255)
            draw_b.ellipse((0, 0, badge_size[0] - 1, badge_size[1] - 1), fill=badge_bg, outline=badge_border, width=2)

            pos_badge = ((qw - badge_size[0]) // 2, (qh - badge_size[1]) // 2)
            pos_logo = ((qw - lw) // 2, (qh - lh) // 2)

            img.paste(badge, pos_badge, badge)
            img.paste(logo, pos_logo, mask)
        except Exception:
            pass

    out_path = QRS_DIR / filename
    img.save(str(out_path), "PNG")
    return out_path


def generate_all_qrs():
    if not QR_ENABLED:
        print(f"\n{Fore.RED}[AVISO] Las librerias 'qrcode' y 'pillow' no estan instaladas en este entorno de Python.{Style.RESET_ALL}")
        print("Para generar codigos QR en terminal, instala: pip install -r requirements.txt\n")
        return

    data = load_redirects_data()
    base_url = data.get("base_url", "https://velasco-dev.github.io/links")
    redirects = data.get("redirects", [])
    count = 0
    print(f"\n{Fore.CYAN}Generando codigos QR oficiales en alta definicion...{Style.RESET_ALL}")
    for item in redirects:
        slug = item.get("slug")
        if slug and slug != "admin":
            short_url = f"{base_url}/{slug}"
            out = generate_qr(short_url, f"qr_{slug}_neon.png", "nox_neon")
            print(f"  [+] QR Neón generado: assets/qrs/qr_{slug}_neon.png ({short_url})")
            count += 1
    print(f"{Fore.GREEN}[OK] Se generaron {count} codigos QR.{Style.RESET_ALL}\n")


def add_link(slug, url, title=None, category="general", project="nox", is_public=True):
    slug = slug.strip().lower().replace(" ", "-")
    url = url.strip()
    title = title or slug

    data = load_redirects_data()
    
    # 1. Asegurar proyecto
    projects = data.setdefault("projects", {})
    if project not in projects:
        projects[project] = {
            "id": project,
            "name": project.upper(),
            "tagline": f"Portal de enlaces de {project}.",
            "theme": { "primary": "#FF007F", "cyan": "#00F0FF", "bg": "#080114" },
            "links": []
        }
    
    # 2. Agregar o actualizar en project.links
    p_links = projects[project].setdefault("links", [])
    found_in_proj = False
    for l in p_links:
        if l.get("slug") == slug:
            l["url"] = url
            l["title"] = title
            l["category"] = category
            l["is_public"] = is_public
            found_in_proj = True
            break
    if not found_in_proj:
        p_links.append({
            "slug": slug,
            "url": url,
            "title": title,
            "category": category,
            "is_public": is_public,
            "is_active": True
        })

    # 3. Sincronizar flat redirects
    flat = data.setdefault("redirects", [])
    found_flat = False
    for r in flat:
        if r.get("slug") == slug:
            r["url"] = url
            r["title"] = title
            r["category"] = category
            r["project"] = project
            r["is_public"] = is_public
            found_flat = True
            break
    if not found_flat:
        flat.append({
            "slug": slug,
            "project": project,
            "url": url,
            "title": title,
            "category": category,
            "is_public": is_public,
            "is_active": True
        })

    save_redirects_data(data)
    generate_folder_redirect(slug, url, title)
    pub_tag = "PUBLICO" if is_public else "PRIVADO/GERENCIAL"
    print(f"{Fore.GREEN}[OK] Enlace '{slug}' registrado en proyecto '{project}' [{pub_tag}].{Style.RESET_ALL}")


def list_links():
    data = load_redirects_data()
    base_url = data.get("base_url", "https://velasco-dev.github.io/links")
    redirects = data.get("redirects", [])
    print(f"\n{Fore.CYAN}{'PROYECTO':<10} | {'ALIAS':<12} | {'TIPO':<10} | {'URL CORTA':<38} | {'DESTINO'}{Style.RESET_ALL}")
    print("-" * 105)
    for r in redirects:
        p = r.get("project", "nox")
        s = r.get("slug", "")
        t = "PUBLICO" if r.get("is_public", True) else "PRIVADO"
        color_t = Fore.GREEN if r.get("is_public", True) else Fore.MAGENTA
        sh = f"{base_url}/{s}"
        dest = (r.get("url", ""))[:32]
        print(f"{Fore.YELLOW}{p:<10}{Style.RESET_ALL} | {Fore.CYAN}{s:<12}{Style.RESET_ALL} | {color_t}{t:<10}{Style.RESET_ALL} | {sh:<38} | {dest}")
    print()


def interactive():
    while True:
        print(f"\n{Fore.MAGENTA}================================================================================")
        print(f"{Fore.CYAN}{Style.BRIGHT}  NOX LINKS SUITE | Gestor Multi-Proyecto para GitHub Pages")
        print(f"{Fore.MAGENTA}================================================================================")
        print("  [1] Compilar todas las carpetas de redireccion estatica")
        print("  [2] Anadir nuevo enlace (Publico o Privado)")
        print("  [3] Listar enlaces registrados por proyecto")
        print("  [4] Generar codigos QR para todos los enlaces")
        print("  [0] Salir")
        print(f"{Fore.MAGENTA}--------------------------------------------------------------------------------")
        opt = input(f"{Fore.GREEN}Selecciona una opcion [0-4]: {Style.RESET_ALL}").strip()

        if opt == "1":
            build_all_redirects()
        elif opt == "2":
            sl = input("Alias (slug, ej. promo): ").strip().lower()
            u = input("URL larga de destino: ").strip()
            t = input("Titulo descriptivo: ").strip()
            pr = input("Proyecto [por defecto 'nox']: ").strip().lower() or "nox"
            pub = input("Es visible en el portal publico? (s/n) [s]: ").strip().lower() != "n"
            if sl and u:
                add_link(sl, u, t, project=pr, is_public=pub)
        elif opt == "3":
            list_links()
        elif opt == "4":
            generate_all_qrs()
        elif opt == "0":
            break


def main():
    parser = argparse.ArgumentParser(description="NOX Links Suite Multi-Project Manager")
    parser.add_argument("--build", action="store_true", help="Compila todas las carpetas de redireccion")
    parser.add_argument("--list", action="store_true", help="Lista todos los enlaces")
    parser.add_argument("--qr-all", action="store_true", help="Genera todos los codigos QR")
    parser.add_argument("--add", nargs=3, metavar=("SLUG", "URL", "TITLE"), help="Anade un nuevo enlace")
    parser.add_argument("--project", default="nox", help="Identificador del proyecto destino (default: nox)")
    parser.add_argument("--private", action="store_true", help="Marca el enlace como privado/gerencial (oculto en portal)")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        interactive()
        return

    if args.build:
        build_all_redirects()
    elif args.list:
        list_links()
    elif args.qr_all:
        generate_all_qrs()
    elif args.add:
        is_pub = not args.private
        add_link(args.add[0], args.add[1], args.add[2], project=args.project, is_public=is_pub)


if __name__ == "__main__":
    main()
