from SkyPRO import API
import requests
import allure
import pytest


@pytest.mark.api
@allure.title("Получить список событий")
@allure.description("Тест получает список событий за 7 июля 2026")
@allure.story("Позитивный тест")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_events():
    """
    Тест получает события за определенный период времени.

    """
    with allure.step("Инициализация конфигурации API"):
        get_events = API()
        url = get_events.base_url + '/v2/schedule/events'
    with allure.step("Формирование тела запроса и заголовков"):
        payload = {
            "from": get_events.startAt,
            "till": get_events.endAt,
            "onlyTypes": []
        }
        headers = {
            "Content-Type": get_events.Content_Type,
            "Cookie": f"token_global={get_events.auth}"
        }
    with allure.step(f"Отправка POST запроса на получение событий: {url}"):
        response = requests.request("POST", url, headers=headers, json=payload)
        server_response_text = response.text
    with allure.step("Проверка успешности ответа сервера (Статус 200 OK)"):
        assert response.status_code == 200, (
            f"API Failed! Status: {response.status_code}. "
            f"Server Message: {server_response_text}"
        )


@pytest.mark.api
@allure.title("Создать событие длинной в 10 часов")
@allure.description("Тест создает событие длинной в 10 часов на 7 июля 2026")
@allure.story("Позитивный тест")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_ten_hours_event():
    """
    Тест создает и автоматически удаляет событие длиной в 10 часов.
    """
    with allure.step("Инициализация конфигурации API"):
        ten_hours_event = API()
        create_url = ten_hours_event.base_url + '/v2/schedule/createPersonal'
        delete_url = ten_hours_event.base_url + '/v2/schedule/removePersonal'
    with allure.step("Формирование тела запроса и заголовков для создания"):
        payload = {
            "backgroundColor": '#' + ten_hours_event.backgroundColor,
            "color": '#' + ten_hours_event.color,
            "description": ten_hours_event.description,
            "title": ten_hours_event.title,
            "startAt": ten_hours_event.startAt,
            "endAt": ten_hours_event.endAt
        }
        headers = {
            "Content-Type": ten_hours_event.Content_Type,
            "Cookie": f"token_global={ten_hours_event.auth}"
        }
    step_msg = f"Отправка POST запроса на создание события: {create_url}"
    with allure.step(step_msg):
        response = requests.request(
            "POST", create_url, headers=headers, json=payload
        )
        server_response_text = response.text
    with allure.step("Проверка успешности создания события (Статус 200 OK)"):
        assert response.status_code == 200, (
            f"API Failed! Status: {response.status_code}. "
            f"Server Message: {server_response_text}"
        )
    with allure.step("Извлечение числового ID созданного события"):
        response_json = response.json()
        extracted_inner_id = (
            response_json.get("data", {})
            .get("payload", {})
            .get("id")
        )
        assert extracted_inner_id is not None, (
            f"Не удалось получить inner id из ответа! "
            f"Ответ сервера: {server_response_text}"
        )
    with allure.step("Формирование тела запроса для удаления"):
        delete_payload = {
            "id": int(extracted_inner_id),
            "startAt": ten_hours_event.startAt,
            "endAt": ten_hours_event.endAt
        }
    delete_msg = f"Отправка POST запроса на удаление события: {delete_url}"
    with allure.step(delete_msg):
        delete_response = requests.request(
            "POST", delete_url, headers=headers, json=delete_payload
        )
        delete_text = delete_response.text
    with allure.step("Проверка успешности удаления события (Статус 200 OK)"):
        assert delete_response.status_code == 200, (
            f"API Deletion Failed! Status: {delete_response.status_code}. "
            f"Server Message: {delete_text}"
        )


@pytest.mark.api
@allure.title("Изменить название и описание события")
@allure.description(
    "Тест создает событие, изменяет его название и описание, а затем удаляет."
)
@allure.story("Позитивный тест")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_descr_and_name():
    """Тест изменяет название и описание события, а потом автоматически удаляет
    событие.
    """
    with allure.step("Инициализация конфигурации API"):
        change_descr_and_name = API()
        create_url = (
            change_descr_and_name.base_url + "/v2/schedule/createPersonal"
        )
        update_url = (
            change_descr_and_name.base_url + "/v2/schedule/updatePersonal"
        )
        delete_url = (
            change_descr_and_name.base_url + "/v2/schedule/removePersonal"
        )
        headers = {
            "Content-Type": change_descr_and_name.Content_Type,
            "Cookie": f"token_global={change_descr_and_name.auth}",
        }
    with allure.step("Формирование тела запроса для создания события"):
        create_payload = {
            "backgroundColor": "#" + change_descr_and_name.backgroundColor,
            "color": "#" + change_descr_and_name.color,
            "description": change_descr_and_name.description,
            "title": change_descr_and_name.title,
            "startAt": change_descr_and_name.startAt,
            "endAt": change_descr_and_name.endAt,
        }
    with allure.step(
        f"Отправка POST запроса на создание события: {create_url}"
    ):
        response = requests.request(
            "POST", create_url, headers=headers, json=create_payload
        )
        server_response_text = response.text
    with allure.step("Проверка успешности создания события (Статус 200 OK)"):
        assert response.status_code == 200, (
            f"API Failed! Status: {response.status_code}. "
            f"Server Message: {server_response_text}"
        )
    with allure.step("Извлечение числового ID созданного события"):
        response_json = response.json()
        extracted_inner_id = (
            response_json.get("data", {}).get("payload", {}).get("id")
        )
        assert extracted_inner_id is not None, (
            f"Не удалось получить inner id из ответа! "
            f"Ответ сервера: {server_response_text}"
        )
    with allure.step("Формирование тела запроса для изменения события"):
        bg_color = f"#{change_descr_and_name.backgroundColor.strip('#')}"
        color = f"#{change_descr_and_name.color.strip('#')}"
        update_payload = {
            "id": int(extracted_inner_id),
            "oldStartAt": change_descr_and_name.startAt,
            "backgroundColor": bg_color,
            "color": color,
            "description": change_descr_and_name.newdescription,
            "title": change_descr_and_name.newtitle,
            "startAt": change_descr_and_name.startAt,
            "endAt": change_descr_and_name.endAt,
        }
    with allure.step(
        f"Отправка POST запроса на обновление события: {update_url}"
    ):
        response = requests.request(
            "POST", update_url, headers=headers, json=update_payload
        )
        server_response_text = response.text

    with allure.step("Проверка успешности обновления события (Статус 200 OK)"):
        assert response.status_code == 200, (
            f"API Failed! Status: {response.status_code}. "
            f"Server Message: {server_response_text}"
        )

    with allure.step("Формирование тела запроса для удаления"):
        delete_payload = {
            "id": int(extracted_inner_id),
            "startAt": change_descr_and_name.startAt,
            "endAt": change_descr_and_name.endAt,
        }
    with allure.step(
        f"Отправка POST запроса на удаление события: {delete_url}"
    ):
        delete_response = requests.request(
            "POST", delete_url, headers=headers, json=delete_payload
        )
        delete_text = delete_response.text

    with allure.step("Проверка успешности удаления события (Статус 200 OK)"):
        assert delete_response.status_code == 200, (
            f"API Deletion Failed! Status: {delete_response.status_code}. "
            f"Server Message: {delete_text}"
        )


@pytest.mark.api
@allure.title("Удаление события")
@allure.description("Тест удаляет событие")
@allure.story("Позитивный тест")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_event():
    """Тест создает и автоматически удаляет событие."""
    with allure.step("Инициализация конфигурации API"):
        delete_event = API()
        create_url = delete_event.base_url + "/v2/schedule/createPersonal"
        delete_url = delete_event.base_url + "/v2/schedule/removePersonal"
        headers = {
            "Content-Type": delete_event.Content_Type,
            "Cookie": f"token_global={delete_event.auth}",
        }
    with allure.step("Формирование тела запроса для создания события"):
        create_payload = {
            "backgroundColor": "#" + delete_event.backgroundColor,
            "color": "#" + delete_event.color,
            "description": delete_event.description,
            "title": delete_event.title,
            "startAt": delete_event.startAt,
            "endAt": delete_event.endAt,
        }
    with allure.step(
        f"Отправка POST запроса на создание события: {create_url}"
    ):
        response = requests.request(
            "POST", create_url, headers=headers, json=create_payload
        )
        server_response_text = response.text
    with allure.step("Проверка успешности создания события (Статус 200 OK)"):
        assert response.status_code == 200, (
            f"API Failed! Status: {response.status_code}. "
            f"Server Message: {server_response_text}"
        )
    with allure.step("Извлечение числового ID созданного события"):
        response_json = response.json()
        extracted_inner_id = (
            response_json.get("data", {}).get("payload", {}).get("id")
        )
        assert extracted_inner_id is not None, (
            f"Не удалось получить inner id из ответа! "
            f"Ответ сервера: {server_response_text}"
        )
    with allure.step("Формирование тела запроса для удаления"):
        delete_payload = {
            "id": int(extracted_inner_id),
            "startAt": delete_event.startAt,
            "endAt": delete_event.endAt,
        }
    with allure.step(
        f"Отправка POST запроса на удаление события: {delete_url}"
    ):
        delete_response = requests.request(
            "POST", delete_url, headers=headers, json=delete_payload
        )
        delete_text = delete_response.text
    with allure.step("Проверка успешности удаления события (Статус 200 OK)"):
        assert delete_response.status_code == 200, (
            f"API Deletion Failed! Status: {delete_response.status_code}. "
            f"Server Message: {delete_text}"
        )


@pytest.mark.api
@allure.title("Создание события без названия")
@allure.description(
    "Тест проверяет возможность создание события без названия"
)
@allure.story("Негативный тест")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_event_without_title():
    """Тест проверяет возможность создание события без названия."""
    with allure.step("Инициализация конфигурации API"):
        event_without_title = API()
        url = event_without_title.base_url + "/v2/schedule/createPersonal"
    with allure.step("Формирование некорректного тела запроса (пустой title)"):
        bg_color = f"#{event_without_title.backgroundColor.strip('#')}"
        color = f"#{event_without_title.color.strip('#')}"
        payload = {
            "backgroundColor": bg_color,
            "color": color,
            "description": event_without_title.description,
            "title": "",  # Оставляем пустым для проверки валидации
            "startAt": event_without_title.startAt,
            "endAt": event_without_title.endAt,
        }
        headers = {
            "Content-Type": event_without_title.Content_Type,
            "Cookie": f"token_global={event_without_title.auth}",
        }
    with allure.step(f"Отправка POST запроса с пустым названием: {url}"):
        response = requests.request("POST", url, headers=headers, json=payload)
        server_response_text = response.text
        msg = f"Status: {response.status_code}. Msg: {server_response_text}"
    with allure.step("Проверка отклонения запроса сервером (Статус 400)"):
        assert response.status_code == 200, f"API Failed! {msg}"
    with allure.step("Проверка наличия точного сообщения об ошибке валидации"):
        expected_error = "Value must be at least 1 character(s) long"
        assert expected_error in server_response_text, (
            f"Expected error message not found! "
            f"Got: {server_response_text}"
        )
