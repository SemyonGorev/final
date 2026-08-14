from selenium import webdriver
from SkyPRO import Skyeng
import pytest
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.title("Создание события с сегодняшней датой")
@allure.description("Тест создает событие на сегодня")
@allure.story("Позитивный тест")
@allure.feature("Расписание UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_event_today(driver):
    """
    Тест создает событие на сегодня.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    Sky = Skyeng(driver)
    with allure.step("Открытие страницы Расписание"):
        Sky.open()
    with allure.step("Ввод логина"):
        Sky.login()
    with allure.step("Ввод пароля"):
        Sky.password()
    with allure.step("Нажатие на кнопку входа"):
        Sky.login_btn()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(сегодня)"):
        Sky.day_event_today()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать время окончания события"):
        Sky.time_end()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Проверка видимости события"):
        Sky.assert_event_is_visible()
    with allure.step("Удаление события"):
        Sky.delete_event()
    with allure.step("Проверка удаления события"):
        Sky.assert_event_is_deleted()


@pytest.mark.ui
@allure.title("Создание события с вчерашней датой")
@allure.description("Тест создает событие на вчера")
@allure.story("Позитивный тест")
@allure.feature("Расписание UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_event_yesterday(driver):
    """
    Тест создает событие на вчера.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    Sky = Skyeng(driver)
    with allure.step("Открытие страницы Расписание"):
        Sky.open()
    with allure.step("Ввод логина"):
        Sky.login()
    with allure.step("Ввод пароля"):
        Sky.password()
    with allure.step("Нажатие на кнопку входа"):
        Sky.login_btn()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(вчера)"):
        Sky.day_event_yesterday()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать время окончания события"):
        Sky.time_end()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Проверка видимости события"):
        Sky.assert_event_is_visible()
    with allure.step("Удаление события"):
        Sky.delete_event()
    with allure.step("Проверка удаления события"):
        Sky.assert_event_is_deleted()


@pytest.mark.ui
@allure.title("Создание 2 событий в одном временном слоте")
@allure.description("Тест создает 2 события в одном временном"
                    " слоте на сегодня")
@allure.story("Позитивный тест")
@allure.feature("Расписание UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_two_events_at_once(driver):
    """
    Тест создает 2 события в одном временном слоте на сегодня.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    Sky = Skyeng(driver)
    with allure.step("Открытие страницы Расписание"):
        Sky.open()
    with allure.step("Ввод логина"):
        Sky.login()
    with allure.step("Ввод пароля"):
        Sky.password()
    with allure.step("Нажатие на кнопку входа"):
        Sky.login_btn()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(сегодня)"):
        Sky.day_event_today()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать время окончания события"):
        Sky.time_end()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(сегодня)"):
        Sky.day_event_today()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать время окончания события"):
        Sky.time_end()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Проверка видимости 2 событий"):
        Sky.assert_duplicate_events_visible()
    with allure.step("Удаление события"):
        Sky.delete_event()
    with allure.step("Удаление события"):
        Sky.delete_event()


@pytest.mark.ui
@allure.title("Создание события зеленого цвета")
@allure.description("Тест создает зеленого цвета на сегодня")
@allure.story("Позитивный тест")
@allure.feature("Расписание UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_green_event(driver):
    """
    Тест создает 2 события в одном временном слоте на сегодня.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    Sky = Skyeng(driver)
    with allure.step("Открытие страницы Расписание"):
        Sky.open()
    with allure.step("Ввод логина"):
        Sky.login()
    with allure.step("Ввод пароля"):
        Sky.password()
    with allure.step("Нажатие на кнопку входа"):
        Sky.login_btn()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(сегодня)"):
        Sky.day_event_today()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать время окончания события"):
        Sky.time_end()
    with allure.step("Выбор зеленого события"):
        Sky.choose_green_button()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Проверка видимости события"):
        Sky.assert_event_is_visible()
    with allure.step("Проверка цвета события"):
        Sky.assert_color()
    with allure.step("Удаление события"):
        Sky.delete_event()
    with allure.step("Проверка удаления события"):
        Sky.assert_event_is_deleted()


@pytest.mark.ui
@allure.title("Создание короткого события")
@allure.description("Тест создает событие длинной"
                    " в 1 минуту на сегодня")
@allure.story("Позитивный тест")
@allure.feature("Расписание UI")
@allure.severity(allure.severity_level.CRITICAL)
def test_event_short(driver):
    Sky = Skyeng(driver)
    with allure.step("Открытие страницы Расписание"):
        Sky.open()
    with allure.step("Ввод логина"):
        Sky.login()
    with allure.step("Ввод пароля"):
        Sky.password()
    with allure.step("Нажатие на кнопку входа"):
        Sky.login_btn()
    with allure.step("Добавить событие"):
        Sky.add_btn()
    with allure.step("Выбрать вкладку событий"):
        Sky.choose_event()
    with allure.step("Выбрать название события"):
        Sky.name_event()
    with allure.step("Выбрать день события(сегодня)"):
        Sky.day_event_today()
    with allure.step("Выбрать время начала события"):
        Sky.time_start()
    with allure.step("Выбрать короткое время окончания события"):
        Sky.short_time_end()
    with allure.step("Нажать на кнопку создания события"):
        Sky.create_event()
    with allure.step("Проверка видимости короткого события"):
        Sky.assert_short_event_is_visible()
    with allure.step("Удаление события"):
        Sky.delete_event()
    with allure.step("Проверка удаления события"):
        Sky.assert_event_is_deleted()
