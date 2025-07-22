# Вибираємо стабільний Python
FROM python:3.10-slim

# Встановлюємо оновлення і pip
RUN apt-get update && apt-get install -y build-essential && \
    pip install --upgrade pip

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо все в контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо бот
CMD ["python", "main.py"]
