from pathlib import Path
from collections import Counter
from PIL import Image

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}

def find_images(root):
    return [p for p in root.rglob("*") if p.suffix.lower() in IMAGE_EXTS]

def inspect(path, root):
    rel = path.relative_to(root)
    group = rel.parts[0] if len(rel.parts) > 1 else "(root)"
    try:
        with Image.open(path) as im:
            im.verify()
        with Image.open(path) as im:
            w, h = im.size
            mode = im.mode
    except Exception as e:
        return None, (str(rel), repr(e))
    return {
        "path": str(rel),
        "group": group,
        "width": w,
        "height": h,
        "aspect": round(w / h, 3),
        "mode": mode,
    }, None

if __name__ == "__main__":
    files = find_images(RAW)
    rows, corrupt = [], []
    for p in files:
        row, err = inspect(p, RAW)
        if row:
            rows.append(row)
        else:
            corrupt.append(err)
    print(f"Readable: {len(rows)}   Corrupt: {len(corrupt)}")
    print("\nPer age group:")
    if rows:
        group_counts = Counter(r["group"] for r in rows)
        for g, n in sorted(group_counts.items(),
                           key=lambda kv: int(kv[0]) if kv[0].isdigit() else 99):
            print(f"    age {g:>3}: {n}")
    else:
        print("    No readable images.")

    if rows:
        widths = sorted(r["width"] for r in rows)
        aspects = sorted(r["aspect"] for r in rows)
        mid = len(rows) // 2
        print(f"\nWidth min {widths[0]} median {widths[mid]} max {widths[-1]}")
        print(f"Aspect min {aspects[0]} median {aspects[mid]} max {aspects[-1]}")
    else:
        print("\nNo readable images to summarize.")