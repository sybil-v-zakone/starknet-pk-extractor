# Starknet private keys extractor

Скрипт из сид фраз получает адреса и приватники кошельков ArgentX.

### Установка зависимостей:

#### *Для Windows:*

Обязательно выполнить действия из данной инструкции:

https://sybil-v-zakone.notion.site/sybil-v-zakone/starknet-py-578a3b2fb96e49149a52b987cbbb8c73

После того, как выполнили действия из инструкции, выполняем данные команды в терминале:

1. `cd путь\к\проекту`
2. `python -m venv venv`
3. `.\venv\Scripts\activate`
4. `pip install -r requirements.txt`

#### *Для MacOS/Linux:*

Выполняем данные команды в терминале:

1. `cd путь/к/проекту`
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`

### Конфигурация:

Все настройки находятся в файле ```config.py```.

`CAIRO_VERSION` — версия Cairo, для которой нужно генерить кошельки. Принимаемые значения: ```cairo0``` и ```cairo1```. Последний символ ставить в соответствии с требуемой версией Cairo.

### Запуск

Заполните файл ```data/seed_phrases.txt``` сид фразами кошельков, для которых нужно получить адрес и запустите файл main.py: ```python main.py```.

### Результаты работы скрипта:
* ```data/addresses.txt``` —  сгенерированные адреса.
* ```data/private_keys.txt``` —  сгенерированные приватники.
