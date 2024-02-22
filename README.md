# Пример приложения на FastApi (REST + GraphQL)

## Запуск примера

1. Клонировать репозиторий
    ```PowerShell
    git clone https://github.com/IldarGaleevSkyProHomeworks/hello_fastapi.git
    cd hello_fastapi
    ```
1. Установить зависимости
    ```PowerShell
    poetry install
    ```

1. Активировать окружение
    ```PowerShell
    poetry shell
    ```

1. Запустить приложение
    ```PowerShell
    python main.py
    ```

Документация по эндпоинтам REST доступна по адресу `http://127.0.0.1:8000/docs`

Документация по эндпоинтам GraphQL доступна по адресу `http://127.0.0.1:8000/graphql`