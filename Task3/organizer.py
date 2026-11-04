import os
import sys
from pathlib import Path
import shutil
inpu = sys.argv[1]

skipped = []
moved = []

if os.path.exists(Path(inpu)):
    print('exists')
else:
    print('no')
    exit(0)

CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt",
                  ".xls", ".xlsx", ".csv", ".ppt", ".pptx"],
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".heic"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code":      [".py", ".js", ".html", ".css", ".java", ".c", ".cpp",
                  ".json", ".sql", ".sh", ".ts"],
    "Executables": [".exe", ".msi", ".bat", ".app", ".apk",".jar"],

}

map = {ext: cat for cat,exts in CATEGORIES.items() for ext in exts}

        
with os.scandir(inpu) as entries:
        for entry in entries:
            finder = entry.name.find('.')
            if entry.name[finder:] in map:
                category_name = map[entry.name[finder:]]
                dest_dir = os.path.join(inpu, category_name)
                os.makedirs(dest_dir, exist_ok=True)
                moved.append(entry.name)
                shutil.move(entry.path, os.path.join(dest_dir, entry.name))

            else:
                skipped.append(entry.name)


print("summary")
print(f"Moved: {len(moved)}")
print(f"Skipped: {len(skipped)}")

