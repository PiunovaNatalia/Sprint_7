# Sprint_7: Тестирование  API сервиса «Яндекс.Самокат».

## Содержание проекта
1. Папка tests: тест-кейсы
2. Файл .gitignore: файлы, которые не должны попасть в git
3. Файл confest: содержит полезные функции
4. Файл data: данные для тест-кейсов
5. Файл README.md: описание проекта
6. Файл requirements.txt: необходимые зависимости

## Запуск проекта:
1. Создать и активировать виртуальное окружение Python
2. Установить зависомсти: python -m pip install requirements.txt
3. Запустить тесты: python -m pytest -v
4. После завершения тестов появится папка с отчетами allure_results

## Сборка отчетов:
1. Генерация: python -m pytest -v --alluredir=allure_results
2. Создание html-страниц с отчетами: allure serve allure_results