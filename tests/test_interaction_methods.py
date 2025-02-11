from src.interaction_methods import WorkMethods


def test_methods_1():
    """Тест получения данных по критерию."""
    wm = WorkMethods()
    vacancies_data = [{"snippet": {"requirement": "Python"}, "id": 1}]
    wm.save_vacancies(vacancies_data)
    result = wm.get_data("Python")
    assert result == vacancies_data


def test_methods_2():
    """Тест получения данных без критерия."""
    wm = WorkMethods()
    vacancies_data = [{"snippet": {"requirement": "Python"}, "id": 1}]
    wm.save_vacancies(vacancies_data)
    result = wm.get_data("Java")
    assert result == []


def test_methods_3():
    """Тест получения данных, когда файл не найден."""
    wm = WorkMethods()
    result = wm.get_data("Any criterion")
    assert result == []


def test_methods_4():
    """Тест удаления вакансий."""
    wm = WorkMethods()
    vacancies_data = [{"id": 1, "title": "Test vacancy"}]
    wm.save_vacancies(vacancies_data)
    wm.delete_vacancy()
    assert wm.get_data("Python") == []
