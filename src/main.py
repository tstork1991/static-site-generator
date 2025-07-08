import os
import shutil

def copy_static(src, dst):
    # Delete destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleted existing {dst}/")

    # Recursively copy everything
    def _copy(src_path, dst_path):
        os.mkdir(dst_path)
        for item in os.listdir(src_path):
            src_item = os.path.join(src_path, item)
            dst_item = os.path.join(dst_path, item)
            if os.path.isdir(src_item):
                _copy(src_item, dst_item)
            else:
                shutil.copy(src_item, dst_item)
                print(f"Copied {src_item} -> {dst_item}")

    _copy(src, dst)

from markdown_to_html import markdown_to_html_node
from utils import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html_node = markdown_to_html_node(md)
    html_content = html_node.to_html()
    title = extract_title(md)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(result)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    """
    Walk through every file under `dir_path_content`.  
    For each *.md file, call `generate_page()` and write a matching *.html*
    file inside `dest_dir_path`, preserving the sub-folder structure.
    """
    for root, _dirs, files in os.walk(dir_path_content):
        for filename in files:
            if not filename.lower().endswith(".md"):
                continue

            from_path = os.path.join(root, filename)                    # content/blog/post.md
            rel_path  = os.path.relpath(from_path, dir_path_content)    # blog/post.md
            dest_path = os.path.join(dest_dir_path,
                                     os.path.splitext(rel_path)[0] + ".html")

            generate_page(from_path, template_path, dest_path)

def main():
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()

