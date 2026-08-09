from SkyPRO import API
import requests
import allure


@allure.title("Получить список событий")
@allure.description("Тест получает список событий за 7 июля 2026")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_events():
    """
    Тест получает события за определенный период времени.

    """
    get_events = API()
    url = get_events.base_url + '/v2/schedule/events'
    payload = {
        "from": get_events.startAt,
        "till": get_events.endAt,
        "onlyTypes": []
    }
    headers = {
        "Content-Type": get_events.Content_Type,
        "Cookie": f"token_global={get_events.auth}"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    server_response_text = response.text
    assert response.status_code == 200, (
        f"API Failed! Status: {response.status_code}. "
        f"Server Message: {server_response_text}"
    )


@allure.title("Создать событие длинной в 10 часов")
@allure.description("Тест создает событие длинной в 10 часов на 7 июля 2026")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_ten_hours_event():
    """
    Тест создает событие длинной в 10 часов.

    """
    ten_hours_event = API()
    url = ten_hours_event.base_url + '/v2/schedule/createPersonal'

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
    response = requests.request(
        "POST", url, headers=headers, json=payload)
    server_response_text = response.text
    assert response.status_code == 200, (
        f"API Failed! Status: {response.status_code}. "
        f"Server Message: {server_response_text}"
    )


@allure.title("Изменить название и описание события")
@allure.description("Тест изменяет название и описание события")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_descr_and_name():
    """
    Тест изменяет название и описание события.

    """
    change_descr_and_name = API()
    url = change_descr_and_name.base_url + '/v2/schedule/updatePersonal'
    bg_color = f"#{change_descr_and_name.backgroundColor.strip('#')}"
    color = f"#{change_descr_and_name.color.strip('#')}"
    payload = {
        "id": int(change_descr_and_name.id),
        "oldStartAt": change_descr_and_name.startAt,
        "backgroundColor": bg_color,
        "color": color,
        "description": change_descr_and_name.newdescription,
        "title": change_descr_and_name.newtitle,
        "startAt": change_descr_and_name.startAt,
        "endAt": change_descr_and_name.endAt
        }
    headers = {
        "Content-Type": change_descr_and_name.Content_Type,
        "Cookie": f"token_global={change_descr_and_name.auth}"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    server_response_text = response.text
    assert response.status_code == 200, (
        f"API Failed! Status: {response.status_code}. "
        f"Server Message: {server_response_text}"
    )


@allure.title("Удаление события")
@allure.description("Тест удаляет событие")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_event():
    """
    Тест удаляет событие.

    """
    delete_event = API()
    url = delete_event.base_url + '/v2/schedule/removePersonal'

    payload = {
        "id": int(delete_event.id),
        "startAt": delete_event.startAt,
        "endAt": delete_event.endAt
        }
    headers = {
        "Content-Type": delete_event.Content_Type,
        "Cookie": f"token_global={delete_event.auth}"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    server_response_text = response.text
    assert response.status_code == 200, (
        f"API Failed! Status: {response.status_code}. "
        f"Server Message: {server_response_text}"
    )


@allure.title("Создание события без названия")
@allure.description("Тест проверяет возможность"
                    " создание события без названия")
@allure.feature("Расписание API")
@allure.severity(allure.severity_level.CRITICAL)
def test_event_without_title():
    """
    Тест проверяет возможность создание события без названия.

    """
    event_without_title = API()
    url = event_without_title.base_url + '/v2/schedule/createPersonal'
    bg_color = f"#{event_without_title.backgroundColor.strip('#')}"
    color = f"#{event_without_title.color.strip('#')}"
    payload = {
        "backgroundColor": bg_color,
        "color": color,
        "description": event_without_title.description,
        "title": "",
        "startAt": event_without_title.startAt,
        "endAt": event_without_title.endAt
        }
    headers = {
        "Content-Type": event_without_title.Content_Type,
        "Cookie": f"token_global={event_without_title.auth}"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    server_response_text = response.text
    msg = f"Status: {response.status_code}. Msg: {server_response_text}"
    assert response.status_code == 200, f"API Failed! {msg}"
    expected_error = "Value must be at least 1 character(s) long"
    assert expected_error in server_response_text, (
        f"Expected error message not found! "
        f"Got: {server_response_text}"
    )
