class WorkVacancies:
    """Класс для работы с вакансиями"""

    # name: str  # название вакансии
    # area: str  # ссылка на вакансию
    # salary: float  # зарплата
    # snippet: str  # краткое описание или требования

    __slots__ = ("name", "area", "salary", "snippet")

    def __init__(self, name: str, area: str, salary: dict, snippet: str):
        self.name = name
        self.area = area
        self.salary = self.__validate_salary(salary)
        self.snippet = snippet

    def __repr__(self):
        return f"Вакансия: {self.name}. Ссылка: {self.area}. Зарплата: {self.salary}. Описание: {self.snippet}.\n"

    def __validate_salary(self, salary: dict):
        """Валидирует данные о зарплате."""
        if not salary:
            return "Зарплата не указана"
        try:
            return salary
        except ValueError:
            return "Зарплата указана некорректно"

    def __eq__(self, other):
        '''Магический метод "равно"'''
        try:
            return self.salary["to"] == other.salary["to"]
        except Exception as error:
            return f"Ошибка: {error}"

    def __gt__(self, other):
        '''Магический метод "больше"'''
        try:
            return self.salary["to"] > other.salary["to"]
        except Exception as error:
            return f"Ошибка: {error}"

    def __lt__(self, other):
        '''Магический метод "меньше"'''
        try:
            return self.salary["to"] < other.salary["to"]
        except Exception as error:
            return f"Ошибка: {error}"


# if __name__ == "__main__":
#     vacancy1 = WorkVacancies("Python разработчик", "https://example.com/job1", {"from": 150000, "to": 200000},
#     "Опыт работы от 3 лет")
#     vacancy2 = WorkVacancies("Python разработчик", "https://example.com/job2", {"from": 100000, "to": 120000},
#     "Опыт работы от 2 лет")
#
#     print(vacancy1)
#     print(vacancy2)
#
#     print(vacancy1 > vacancy2)
