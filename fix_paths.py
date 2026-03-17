import os
import glob
import re

directory = r'c:\Users\dzula\OneDrive\Desktop\kopeladar'
files = glob.glob(os.path.join(directory, '*.html'))
files.append(os.path.join(directory, 'main.js'))

replacements = [
    (r'"(?:\.\./)?html/([^"]+)"', r'"\1"'),
    (r"'(?:\.\./)?html/([^']+)'", r"'\1'"),
    (r'"\.\./css/([^"]+)"', r'"css/\1"'),
    (r"'\.\./css/([^']+)'", r"'css/\1'"),
    (r'"\.\./img/([^"]+)"', r'"img/\1"'),
    (r"'\.\./img/([^']+)'", r"'img/\1'"),
    (r'"(?:\.\./)?(?:javascript|js)/([^"]+)"', r'"\1"'),
    (r"'(?:\.\./)?(?:javascript|js)/([^']+)'", r"'\1'"),
    (r'"\.\./json/([^"]+)"', r'"json/\1"'),
    (r"'\.\./json/([^']+)'", r"'json/\1'")
]

count = 0
for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")
        count += 1

print(f"Done. Updated {count} files.")
