with open('backend/static/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="section-studio"')
if idx != -1:
    print(text[idx:idx+3500])
