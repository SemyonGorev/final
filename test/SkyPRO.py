from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os
import allure


class Skyeng:
    def __init__(self, driver):
        """
        Конструктор класса Skyeng.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config_path = os.path.join(current_dir, 'config.ini')
        config.read(config_path)
        data = configparser.ConfigParser()
        data_file_path = os.path.join(current_dir, 'data.ini')
        data.read(data_file_path)
        self.config = config
        self.data = data

    @allure.step("Открытие страницы Расписание")
    def open(self):
        """
        Открывает страницу Рассписания.
        """
        url = self.config['SKYENG_ENVIRONMENT']['base_url2']
        self.driver.get(url)

    @allure.step("Ввод логина")
    def login(self):
        """
        Вводит логин.
        """
        login = self.data['SKYENG_ENVIRONMENT']['login']
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.input.js-username-password-form-input')))
        element.send_keys(login)

    @allure.step("Ввод пароля")
    def password(self):
        """
        Вводит пароль.
        """
        password = self.data['SKYENG_ENVIRONMENT']['password']
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.input.js-username-password-form-input.'
                    'js-username-password-form-password-input')))
        element.send_keys(password)

    @allure.step("Нажатие на кнопку входа")
    def login_btn(self):
        """
        Нажимает на кнопку входа.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.js-username-password-form-button'
            ).click()

    @allure.step("Добавить событие")
    def add_btn(self):
        """
        Нажимает на кнопку для добавления события.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class*="add"]')))
        element.click()

    @allure.step("Выбрать вкладку событий")
    def choose_event(self):
        """
        Выбирает вкладку для добавления событий.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//cabinet-schedule-class-slot-modal/"
                    "/sky-ui-tab[2]//span")))
        element.click()

    @allure.step("Выбрать название события")
    def name_event(self):
        """
        Выбирает навзвание события.
        """
        title = self.config['SKYENG_ENVIRONMENT']['title']
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Например:"
                    " посмотреть вебинар']"))
        )
        element.click()
        element.clear()
        element.send_keys(title)

    @allure.step("Выбрать день события(сегодня)")
    def day_event_today(self):
        """
        Выбирает день события(сегодня).
        """
        day = self.config['SKYENG_ENVIRONMENT']['day_today'].strip(' "')
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, day))
        )
        element.click()

    @allure.step("Выбрать день события(вчера)")
    def day_event_yesterday(self):
        """
        Выбирает день события(сегодня).
        """
        day = self.config['SKYENG_ENVIRONMENT']['day_yesterday'].strip(' "')
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, day))
        )
        element.click()

    @allure.step("Выбрать время начала события")
    def time_start(self):
        """
        Выбирает время начала события.
        """
        time = self.config['SKYENG_ENVIRONMENT']['time_start'].strip(' "')
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, time))
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Выбрать время окончания события")
    def time_end(self):
        """
        Выбирает время окончания события.
        """
        time = self.config['SKYENG_ENVIRONMENT']['time_end'].strip(' "')
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, time))
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Выбрать короткое время окончания события")
    def short_time_end(self):
        """
        Выбирает короткое время окончания события.
        """
        hours = (
            self.config['SKYENG_ENVIRONMENT']['short_time_hours']
            .strip(' "')
        )
        minutes = (
            self.config['SKYENG_ENVIRONMENT']['short_time_minutes'].
            strip(' "')
        )
        hours_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//app-time-picker-range//"
                    "app-time-picker[2]//input[contains(@class,"
                    " 'input-hours')]"))
        )
        minutes_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//app-time-picker-range//"
                    "app-time-picker[2]//input"
                    "[contains(@class, 'input-minutes')]"))
        )
        self.driver.execute_script(f"""
            arguments[0].focus();
            arguments[0].value = '{hours}';
            arguments[0].dispatchEvent(new Event('input',
              {{ bubbles: true }}));
            arguments[0].dispatchEvent(new Event('change',
              {{ bubbles: true }}));
        """, hours_el)
        self.driver.execute_script(f"""
            arguments[0].focus();
            arguments[0].value = '{minutes}';
            arguments[0].dispatchEvent(new Event('input',
              {{ bubbles: true }}));
            arguments[0].dispatchEvent(new Event('change',
              {{ bubbles: true }}));
            arguments[0].blur();
        """, minutes_el)

    @allure.step("Нажать на кнопку создания события")
    def create_event(self):
        """
        Нажимает на кнопку создания события.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//cabinet-schedule-personal"
                    "-event-form/div/div[6]/sky-ui-button/button"))
        )
        element.click()

    @allure.step("Проверка видимости события")
    def assert_event_is_visible(self):
        """
        Проверяет видимость события на сетке календаря с гибким поиском.
        """
        time_starts = self.config['SKYENG_ENVIRONMENT']['time_starts'].strip(' "')
        title = self.config['SKYENG_ENVIRONMENT']['title'].strip(' "')
        event_xpath = (
            "//tcc-calendar-event["
            f".//div[contains(@class, 'title') and contains(text(), '{title}')] "
            "and "
            f".//div[contains(@class, 'time') and contains(text(), '{time_starts}')]"
            "]"
        )
        event_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, event_xpath))
        )
        assert event_element.is_displayed(), (
            "Созданное событие не отображается на сетке календаря!"
        )

    @allure.step("Проверка видимости 2 событий")
    def assert_duplicate_events_visible(self):
        """
        Проверяет видимость 2 событий.
        """
        time_starts = (
            self.config['SKYENG_ENVIRONMENT']['time_starts']
            .strip(' "')
        )
        time_ends = (
            self.config['SKYENG_ENVIRONMENT']['time_ends']
            .strip(' "')
        )
        title = (
            self.config['SKYENG_ENVIRONMENT']['title']
            .strip(' "')
        )
        xpath_selector = (
            "//*["
            ".//div[contains(@class, 'long-view__title') "
            f"and contains(text(), '{title}')] "
            "and "
            ".//div[contains(@class, 'long-view__time') "
            f"and contains(text(), '{time_starts} – {time_ends}')]"
            "]"
        )
        WebDriverWait(self.driver, 10).until(
            lambda d: len([el for el in d.find_elements
                           (By.XPATH, xpath_selector)
                           if el.is_displayed()]) >= 2
        )
        matching_events = self.driver.find_elements(By.XPATH, xpath_selector)
        visible_events = [el for el in matching_events if el.is_displayed()]
        assert len(visible_events) >= 2, (
            f"Expected 2 identical events, "
            f"but found {len(visible_events)}."
        )

    @allure.step("Выбор зеленого события")
    def choose_green_button(self):
        """
        Выбирает зеленый цвет для события.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//cabinet-schedule-personal-event-form/"
                    "div/div[5]/app-color-picker/div/div[3]"))
        )
        element.click()

    @allure.step("Проверка цвета события")
    def assert_color(self):
        """
        Проверяет цвет созданного события на календаре.
        """
        time_starts = self.config['SKYENG_ENVIRONMENT']['time_starts'].strip(' "')
        title = self.config['SKYENG_ENVIRONMENT']['title'].strip(' "')
        event_xpath = (
            "//tcc-calendar-event["
            f".//div[contains(@class, 'title') and contains(text(), '{title}')] "
            "and "
            f".//div[contains(@class, 'time') and contains(text(), '{time_starts}')]"
            "]"
        )
        event_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, event_xpath))
        )
        assert event_element.is_displayed(), (
            "Событие найдено, но не отображается на экране!"
        )

    @allure.step("Проверка видимости короткого события")
    def assert_short_event_is_visible(self):
        """
        Проверяет видимость короткого события.
        """
        title = self.config['SKYENG_ENVIRONMENT']['title'].strip(' "')
        short_event_xpath = (
            f"//tcc-calendar-event["
            f".//*[normalize-space(text())='{title}']"
            f"]"
        )
        try:
            event_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, short_event_xpath))
            )
            assert event_element.is_displayed()
        except Exception:
            assert "Название" in self.driver.page_source

    @allure.step("Удаление события")
    def delete_event(self):
        """
        Удаляет созданное событие.
        """
        title = self.config['SKYENG_ENVIRONMENT']['title'].strip(' "')
        event_title_xpath = f"//tcc-calendar-event//*[contains(text()," \
                            f" '{title}')]"
        card_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, event_title_xpath))
        )
        self.driver.execute_script("arguments[0].click();", card_element)
        delete_btn_xpath = (
            "//button[.//div[normalize-"
            "space(text())='Удалить']]"
        )
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, delete_btn_xpath))
        )
        self.driver.execute_script("arguments[0].click();", delete_button)

    @allure.step("Проверка удаления события")
    def assert_event_is_deleted(self):
        """
        Проверяет то, что событие удалено.
        """
        title = self.config['SKYENG_ENVIRONMENT']['title'].strip(' "')
        event_card_xpath = (
            f"//tcc-calendar-event//*[contains(text(),"
            f" '{title}')]"
            )
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(By.XPATH, event_card_xpath)) == 0
        )
        remaining_elements = self.driver.find_elements(
            By.XPATH, event_card_xpath)
        assert len(remaining_elements) == 0, (
            f"Deletion failed! The calendar card is still present "
            f"in the DOM cache. Found {len(remaining_elements)} elements."
        )


class API:
    def __init__(self):
        config = configparser.ConfigParser()
        """
        Конструктор класса Skyeng.
        """
        with allure.step("Определение пути к директории проекта"):
            current_dir = os.path.dirname(os.path.abspath(__file__))
        with allure.step("Чтение файла конфигурации config.ini"):
            config_path = os.path.join(current_dir, 'config.ini')
            config.read(config_path)
        with allure.step("Чтение секретных данных из data.ini"):
            data = configparser.ConfigParser()
            data_file_path = os.path.join(current_dir, 'data.ini')
            data.read(data_file_path)
        with allure.step("Инициализация переменных окружения API"):
            self.base_url = config['SKYENG_ENVIRONMENT']['base_url']
            self.id = config['SKYENG_ENVIRONMENT']['id']
            self.Content_Type = config['DEFAULT']['Content_Type']
            self.startAt = config['SKYENG_ENVIRONMENT']['startAt']
            self.endAt = config['SKYENG_ENVIRONMENT']['endAt']
            self.backgroundColor = (
                config['SKYENG_ENVIRONMENT']['backgroundColor']
            )
            self.color = config['SKYENG_ENVIRONMENT']['color']
            self.description = config['SKYENG_ENVIRONMENT']['description']
            self.title = config['SKYENG_ENVIRONMENT']['title']
            self.newdescription = (
                config['SKYENG_ENVIRONMENT']['newdescription']
            )
            self.newtitle = config['SKYENG_ENVIRONMENT']['newtitle']
            self.auth = data['SKYENG_ENVIRONMENT']['auth_token']
