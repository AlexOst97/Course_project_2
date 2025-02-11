from unittest.mock import patch

from src.interaction_hh_ru import HeadHunterAPI


def test_hh1(capsys):
    HeadHunterAPI("https://api.hh.ru/vacancies")
    message = capsys.readouterr()
    assert message.out.strip() == ""


@patch("requests.get")
def test_hh2(test_hh_api):
    obj_api = HeadHunterAPI()
    assert type(obj_api) is HeadHunterAPI


def test_hh3():
    hh1 = HeadHunterAPI("https://api.hh.ru/vacancies")
    hh2 = hh1.url_status()
    assert hh2 == "Успешный запрос"


def test_hh4():
    hh1 = HeadHunterAPI("https://api.hh.ru/123")
    hh2 = hh1.url_status()
    assert hh2 == "Неуспешный запрос"
