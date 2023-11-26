from bs4 import BeautifulSoup

# Исходный HTML-код
with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы с тегом 'figcaption'
figcaptions = soup.find_all('figcaption')

# Обходим каждый элемент 'figcaption' и добавляем его содержимое в атрибут 'alt' изображения
for figcaption in figcaptions:
    img_tag = figcaption.find_previous('img')
    if img_tag:
        img_tag['alt'] = figcaption.p.text

# Получаем новый HTML-код
new_html_content = str(soup)

with open('test2.html', 'w', encoding='utf-8') as file:
    file.write(new_html_content)
