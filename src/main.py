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

def main():
    copy_static("static", "public")

if __name__ == "__main__":
    main()
