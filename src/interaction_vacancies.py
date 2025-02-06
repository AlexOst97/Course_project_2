
class WorkVacancies():
    '''Класс для работы с вакансиями'''

    name: str  #название вакансии
    area: str  #ссылка на вакансию
    salary: float  #зарплата
    snippet: str #краткое описание или требования

    def __init__(self, name, area, salary, snippet):
        self.name = name
        self.area = area
        self.salary = self.validate_salary(salary)
        self.snippet = snippet

    def __str__(self):
        return f"Вакансия: {self.name}. Ссылка: {self.area}. Зарплата: {self.salary}. Описание: {self.snippet}.\n"

    def validate_salary(self, salary):
        """Валидирует данные о зарплате."""
        if not salary:
            return "Зарплата не указана"
        try:
            return float(salary)
        except ValueError:
            return "Зарплата указана некорректно"

    def __eq__(self, other):
        '''Магический метод "равно"'''
        try:
            return self.salary == other.salary
        except Exception as error:
            return f"Ошибка: {error}"

    def __gt__(self, other):
        '''Магический метод "больше"'''
        try:
            return self.salary > other.salary
        except Exception as error:
            return f"Ошибка: {error}"

    def __lt__(self, other):
        '''Магический метод "меньше"'''
        try:
            return self.salary < other.salary
        except Exception as error:
            return f"Ошибка: {error}"


# if __name__ == "__main__":
#     vacancy1 = WorkVacancies("Python разработчик", "https://example.com/job1", "100000", "Опыт работы от 3 лет")
#     vacancy2 = WorkVacancies("Python разработчик", "https://example.com/job2", "150000", "Опыт работы от 2 лет")
#     vacancy3 = WorkVacancies("Инженер", "https://example.com/job3", None, "Проектирование первичного оборудования")
#     vacancy4 = WorkVacancies("Java разработчик", "https://example.com/job4", "abc", "Анализ данных")
#
#     print(vacancy1)
#     print(vacancy2)
#     print(vacancy3)
#     print(vacancy4)
#
#     print(vacancy1 == vacancy2)
#     print(vacancy1 > vacancy2)
#     print(vacancy1 < vacancy2)