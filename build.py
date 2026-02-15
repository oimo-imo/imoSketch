import os

# imagesフォルダ内の画像を取得（拡張子がjpg, png, webpのもの）
valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
images = [f for f in os.listdir('images') if f.lower().endswith(valid_extensions)]
images.sort(reverse=True) # 新しい順に並べる（名前順）

# HTMLのパーツを作成
img_tags = "\n".join([f'        <img src="images/{img}" alt="sketch">' for img in images])

# index.htmlを読み込んで書き換え
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

    new_html = html.replace('', img_tags)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        