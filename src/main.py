# src/main.py
import os
import shutil
import sys                           # ← NEW (1)

from markdown_to_html import markdown_to_html_node
from utils import extract_title

# ─────────────────────────── helpers ────────────────────────────
def copy_static(src: str, dst: str) -> None:
    """Recursively copy the entire static/ directory to dst/."""
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleted existing {dst}/")

    def _copy(src_path, dst_path):
        os.mkdir(dst_path)
        for item in os.listdir(src_path):
            s_item = os.path.join(src_path, item)
            d_item = os.path.join(dst_path, item)
            if os.path.isdir(s_item):
                _copy(s_item, d_item)
            else:
                shutil.copy(s_item, d_item)
                print(f"Copied {s_item} -> {d_item}")

    _copy(src, dst)


def generate_page(from_path: str,
                  template_path: str,
                  dest_path: str,
                  basepath: str = "/") -> None:            # ← NEW PARAM (2)
    """Convert a single Markdown file to HTML, write to dest_path."""
    print(f"Generating {dest_path} from {from_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html_node = markdown_to_html_node(md_text)
    body_html = html_node.to_html()
    title = extract_title(md_text)

    html = (template
            .replace("{{ Title }}", title)
            .replace("{{ Content }}", body_html))

    # ensure basepath ends with exactly one “/”
    if not basepath.endswith("/"):
        basepath += "/"

    # patch absolute links & images
    html = (html
            .replace('href="/', f'href="{basepath}')
            .replace('src="/',  f'src="{basepath}'))

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)


def generate_pages_recursive(content_dir: str,
                             template_path: str,
                             out_dir: str,
                             basepath: str = "/") -> None:   # ← NEW PARAM (3)
    """Walk content_dir, convert every .md → matching .html in out_dir."""
    for root, _dirs, files in os.walk(content_dir):
        for name in files:
            if not name.lower().endswith(".md"):
                continue

            src_md   = os.path.join(root, name)
            rel_md   = os.path.relpath(src_md, content_dir)       # e.g. blog/post.md
            dest_html = os.path.join(out_dir,
                                     os.path.splitext(rel_md)[0] + ".html")

            generate_page(src_md, template_path, dest_html, basepath)   # ← pass basepath


# ───────────────────────────── main ─────────────────────────────
def main() -> None:
    # (4) pick up basepath from CLI or default “/”
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"[info] basepath = '{basepath}'")

    # (5) GitHub Pages output folder
    OUT_DIR = "docs"

    copy_static("static", OUT_DIR)
    generate_pages_recursive("content", "template.html", OUT_DIR, basepath)


# (6) correct guard
if __name__ == "__main__":
    main()
