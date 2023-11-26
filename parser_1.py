from bs4 import BeautifulSoup
import sqlite3

# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('tuning_data.db')
cursor = conn.cursor()

# Создаем таблицу в базе данных, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tuning_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        engine TEXT,
        power_before TEXT,
        power_after TEXT,
        torque_before TEXT,
        torque_after TEXT,
        cost TEXT
    )
''')
conn.commit()

# Открываем HTML-файл и передаем его содержимое в BeautifulSoup
with open('index.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Инициализируем парсер BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Ищем все блоки с классом "modal fade"
modal_blocks = soup.find_all('div', class_='modal fade')

# Итерируем по каждому блоку модального окна
for modal_block in modal_blocks:
    # Извлекаем значение атрибута 'id' блока модального окна
    modal_id = modal_block.get('id')

    # Находим родительский элемент блока с именем, который является блоком модального окна
    modal_content = modal_block.find('div', class_='modal-content')

    # Ищем все таблицы внутри блока модального окна
    tables = modal_content.find_all('table', class_='table-hover')

    # Проходим по каждой таблице
    for table in tables:
        # Ищем строки с данными
        rows = table.find_all('tr')

        # Пропускаем первую строку с заголовками
        rows = rows[1:]

        # Проходим по каждой строке и извлекаем данные
        for row in rows:
            # Извлекаем ячейки данных
            cells = row.find_all(['td', 'th'])

            # Проверяем, что у нас достаточно ячеек для извлечения данных
            if len(cells) == 6:
                # Извлекаем данные из ячеек
                engine = cells[0].text.strip()
                power_before = cells[1].text.strip()
                power_after = cells[2].text.strip()
                torque_before = cells[3].text.strip()
                torque_after = cells[4].text.strip()
                cost = cells[5].text.strip()

                # Вставляем данные в базу данных
                cursor.execute('''
                    INSERT INTO tuning_data (name, engine, power_before, power_after, torque_before, torque_after, cost)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (modal_id, engine, power_before, power_after, torque_before, torque_after, cost))

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
