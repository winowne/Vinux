# Vinux

Лёгкий AI-чат-бот с терминальным интерфейсом (TUI) на Textual. Генерирует ответы на русском языке.

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/username/vinux.git
cd vinux

```

### 2. Создать виртуальное окружение

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate

```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

```

### 3. Установить зависимости

```bash
pip install -r requirements.txt

```

### 4. Скачать модель

Скачай файл модели с Hugging Face (ссылка указана в разделе **About** репозитория) и помести его в папку `models/`.

### 5. Запуск

```bash
python main.py

```

Управление в меню — стрелки, `Enter`.

Команды в чате: `/exit` — выход, `/clear` — очистить, `/back` — назад.

## Структура проекта

* `main.py` — точка входа, главное меню
* `config.py` — конфигурация
* `screens/` — экраны (чат, история, старт)
* `src/` — генерация, анимация, маскот (временно недоступен)
* `styles/` — CSS-стили
* `models/` — файлы модели
* `sessions/` — история диалогов

## Технологии

Python, PyTorch, PyTorch Lightning, Textual, HuggingFace Tokenizers, Rich