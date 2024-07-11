# cit_helperbot
Перевода гуглодока (Markdown) в телеграм-посты

## Для версионирования библиотек:

1. Убедиться, что в системе установлена подходящая версия Python (3.9 или выше).
2. Установить [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).
3. В директории проекта, в командной строке выполнить `poetry install`.
4. Если при запуске исполняемого файла система не "подхватывает" созданный virtual environment 
(проверить это можно, выполнив в консоли `which python` (Linux, MacOS) либо `where python` (Windows)), 
исполняемый файл запускать через `poetry run python bot.py`. 
В отдельных случаях может понадобиться указывать `python3` вместо `python`.
