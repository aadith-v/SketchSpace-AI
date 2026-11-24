with open('backend/static/index.html', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'compare', text, re.IGNORECASE)]
print(f"Total 'compare' occurrences: {len(matches)}")
for idx in matches[:6]:
    print("--- SNIPPET ---")
    print(text[max(0, idx-100):min(len(text), idx+300)])
