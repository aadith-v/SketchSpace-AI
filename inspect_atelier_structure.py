import re

with open('build_luxury_atelier_studio.py', encoding='utf-8') as f:
    text = f.read()

print(f"File length: {len(text):,} characters")
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Sections found:", sections)

# Check colors
colors = re.findall(r'--[a-z0-9\-]+:\s*[^;]+;', text[:2500])
print("\nColor variables sample:")
for c in colors[:15]:
    print(" ", c)
