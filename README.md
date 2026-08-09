# final

### Описание:
Проект предоставляет возможность преподавателям (пользователям), в зависимости от их графики и пожеланий добавлять, редактировать и удалить личные события в расписании.

### UI тесты:
1.Создание события с сегодняшней датой
2.Создание события с вчерашней датой
3.Создание 2 событий в одном временном слоте
4.Создание события зеленого цвета
5.Создание короткого события

### API тесты:
1.Получить список событий
2.Создать событие длинной в 10 часов
3.Изменить название и описание события
4.Удаление события
5.Создание события без названия

### Стек:
- pytest
- selenium
- requests

### Полезные ссылки
- [Ссылка на тест-план](https://semyongorev.yonote.ru/share/1c10b517-ac9a-461b-aafd-8f0f48737242)

### Шаги
1. Склонировать проект 'git clone https://github.com/SemyonGorev/final.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'
### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install python-dotenv
- pip3 install requests

