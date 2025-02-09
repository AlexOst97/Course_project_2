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
