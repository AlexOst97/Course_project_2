from src.interaction_vacancies import WorkVacancies


def test_vacancies():
    vacancy1 = WorkVacancies(
        "Python разработчик",
        "https://example.com/job1",
        {"from": 150000, "to": 200000},
        "Опыт работы от 3 лет",
    )
    vacancy2 = WorkVacancies(
        "Python разработчик",
        "https://example.com/job2",
        {"from": 100000, "to": 120000},
        "Опыт работы от 2 лет",
    )

    assert (
        vacancy1
        == "Вакансия: Python разработчик. Ссылка: https://example.com/job1. Зарплата: {'from': 150000, 'to': 200000}. "
           "Описание: Опыт работы от 3 лет."
    )
    assert (
        vacancy2
        == "Вакансия: Python разработчик. Ссылка: https://example.com/job2. Зарплата: {'from': 100000, 'to': 120000}. "
           "Описание: Опыт работы от 2 лет."
    )

    # assert (vacancy1 == vacancy2) == False
    # assert (vacancy1 > vacancy2) == True
    # assert (vacancy1 < vacancy2) == False

    assert not (vacancy1 == vacancy2)
    assert vacancy1 > vacancy2
    assert not (vacancy1 < vacancy2)
