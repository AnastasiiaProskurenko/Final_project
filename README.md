# 🎬 Final_project

Це консольне Python-додаток для пошуку фільмів у базі даних **MySQL** з логуванням запитів у **MongoDB** та можливістю перегляду популярних і останніх пошуків.

---

## 📌 Можливості
```
- Пошук фільмів по:
  - назві
  - року випуску
  - діапазону років
  - жанру
  - жанру + роки
  - імені актора
- Пагінація результатів
- Логування кожного пошуку (тип, параметри, кількість знайдених записів, час)
- Перегляд:
  - топ-5 найпопулярніших запитів
  - останніх 5 унікальних запитів
```

## ⚙️ Установка

### 1. Клонирование проекта

```bash

git clone https://github.com/your-username/Final_project.git
cd Final_project
```
### 2. Установка зависимостей
```bash

pip install -r requirements.txt
```
### 3. Настройка окружения
```bash

Створіть файл .env в корені проєкту та додайте туди:

MONGO_URI=mongodb://localhost:27017
MONGO_DB_NAME=your_db
MONGO_COLLECTION_NAME=search_logs
Також переконайтесь, що в mysql_connector.py вказано правильні дані для підключення до MySQL.
```

### 📁 Структура проєкту
```bash

Final_project/
│
├── .env                  # Змінні середовища (не комітиться)
├── .gitignore            # Ігноровані файли для Git
├── formatter.py          # Форматований вивід таблиць та пагінація
├── log_stats.py          # Отримання статистики логів з MongoDB
├── log_writer.py         # Запис логів пошуків у MongoDB
├── main.py               # Головний файл запуску
├── mysql_connector.py    # Підключення та SQL-запити до MySQL
├── README.md             # Цей файл
├── requirements.txt      # Залежності проєкту
├── search_def.py         # Реалізація пошукових функцій
```
### ▶️ Запуск
```bash

python main.py
```

### 🧩 Опис основних файлів
```
main.py — точка входу, запускає меню та обробляє ввід користувача.

search_def.py — містить функції:

search_film_name()

search_film_year()

search_film_years_range()

search_film_gerne()

search_film_gerne_and_years()

search_film_actor()

show_popular_searches()

show_last_searches()

formatter.py — функції print_table() і paginate_results() для виводу результатів.

log_writer.py — логування запитів до MongoDB (тип, параметри, час, кількість).

log_stats.py — функції для отримання статистики:

топ-5 запитів

останні 5 унікальних запитів

mysql_connector.py — підключення до MySQL та виконання запитів.
```

### 🛠 Використані технології
```
Python 3.10+

MySQL — база даних фільмів

MongoDB — збереження логів

Pymongo, mysql-connector-python, python-dotenv
```