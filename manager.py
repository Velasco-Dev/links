#!/usr/bin/env python3
"""
================================================================================
PROYECTO: NOX Links Suite
REPOSITORIO: https://github.com/Velasco-Dev/links
ARCHIVO: manager.py
DESCRIPCION: Asistente CLI para compilar redirecciones estaticas para GitHub Pages,
             gestionar enlaces en redirects.json y generar codigos QR en alta definicion.
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
        return {"base_url": "https://velasco-dev.github.io/links", "redirects": []}
    with open(REDIRECTS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def save_redirects_data(data):
    with open(REDIRECTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_folder_redirect(slug, target_url, title):
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


def build_all_redirects():
    data = load_redirects_data()
    redirects = data.get("redirects", [])
    count = 0
    print(f"\n{Fore.CYAN}Compilando carpetas de redireccion estatica para GitHub Pages...{Style.RESET_ALL}")
    for item in redirects:
        slug = item.get("slug")
        url = item.get("url")
        title = item.get("title", slug)
        if slug and url:
            generate_folder_redirect(slug, url, title)
            print(f"  [+] Generado: /{slug}/index.html -> {url}")
            count += 1
    print(f"{Fore.GREEN}[OK] Se compilaron exitosamente {count} carpetas de redireccion.{Style.RESET_ALL}\n")


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
    data = load_redirects_data()
    base_url = data.get("base_url", "https://velasco-dev.github.io/links")
    redirects = data.get("redirects", [])
    count = 0
    print(f"\n{Fore.CYAN}Generando codigos QR oficiales en alta definicion...{Style.RESET_ALL}")
    for item in redirects:
        slug = item.get("slug")
        if slug:
            short_url = f"{base_url}/{slug}"
            out = generate_qr(short_url, f"qr_{slug}_neon.png", "nox_neon")
            print(f"  [+] QR Neón generado: assets/qrs/qr_{slug}_neon.png ({short_url})")
            count += 1
    print(f"{Fore.GREEN}[OK] Se generaron {count} codigos QR.{Style.RESET_ALL}\n")


def add_link(slug, url, title=None, category="general"):
    slug = slug.strip().lower()
    url = url.strip()
    title = title or slug

    data = load_redirects_data()
    existing = False
    for item in data.get("redirects", []):
        if item.get("slug") == slug:
            item["url"] = url
            item["title"] = title
            item["category"] = category
            existing = True
            break
    if not existing:
        data.setdefault("redirects", []).append({
            "slug": slug,
            "url": url,
            "title": title,
            "category": category,
            "is_active": True
        })
    save_redirects_data(data)
    generate_folder_redirect(slug, url, title)
    print(f"{Fore.GREEN}[OK] Enlace '{slug}' registrado y carpeta /{slug}/index.html compilada.{Style.RESET_ALL}")


def list_links():
    data = load_redirects_data()
    base_url = data.get("base_url", "https://velasco-dev.github.io/links")
    redirects = data.get("redirects", [])
    print(f"\n{Fore.CYAN}{'ALIAS':<12} | {'URL CORTA EN GITHUB':<42} | {'DESTINO'}{Style.RESET_ALL}")
    print("-" * 90)
    for r in redirects:
        s = r.get("slug", "")
        sh = f"{base_url}/{s}"
        dest = (r.get("url", ""))[:32]
        print(f"{Fore.YELLOW}{s:<12}{Style.RESET_ALL} | {sh:<42} | {dest}")
    print()


def interactive():
    while True:
        print(f"\n{Fore.MAGENTA}================================================================================")
        print(f"{Fore.CYAN}{Style.BRIGHT}  NOX LINKS SUITE | Gestor de Redirecciones para GitHub Pages")
        print(f"{Fore.MAGENTA}================================================================================")
        print("  [1] Compilar todas las carpetas de redireccion estatica")
        print("  [2] Anadir nuevo enlace corto")
        print("  [3] Listar enlaces registrados")
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
            if sl and u:
                add_link(sl, u, t)
        elif opt == "3":
            list_links()
        elif opt == "4":
            generate_all_qrs()
        elif opt == "0":
            break


def main():
    parser = argparse.ArgumentParser(description="NOX Links Suite Manager")
    parser.add_argument("--build", action="store_true", help="Compila todas las carpetas de redireccion")
    parser.add_argument("--list", action="store_true", help="Lista todos los enlaces")
    parser.add_argument("--qr-all", action="store_true", help="Genera todos los codigos QR")
    parser.add_argument("--add", nargs=3, metavar=("SLUG", "URL", "TITLE"), help="Anade un nuevo enlace")

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
        add_link(args.add[0], args.add[1], args.add[2])


if __name__ == "__main__":
    main()
