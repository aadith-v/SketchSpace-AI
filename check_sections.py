import re

with open('backend/static/index.html', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print("Section IDs:")
for s in sections:
    print(" -", s)

navs = re.findall(r'<nav.*?</nav>', html, re.DOTALL)
if navs:
    print("\nNav content:")
    print(navs[0][:600])

scripts = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html)
print("\nJS functions found (sample):", [s for s in scripts if 'nav' in s.lower() or 'tab' in s.lower() or 'view' in s.lower() or 'mode' in s.lower()][:10])
