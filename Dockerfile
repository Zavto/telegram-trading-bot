# Використовуємо стабільний Python 3.10
FROM python:3.10-slim

# Оновлення системи та pip
RUN apt-get update && apt-get install -y build-essential && \
    pip install --upgrade pip

# Робоча директорія
WORKDIR /app

# Копіюємо проєкт
COPY . .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск бота
CMD ["python", "main.py"]
