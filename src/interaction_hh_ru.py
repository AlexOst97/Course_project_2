import requests

from src.abstract_class import AbstractApi


class HeadHunterAPI(AbstractApi):
    """Класс подключаться к API hh.ru и получает вакансии"""

    def __init__(self, url: str = "https://api.hh.ru/vacancies"):
        """Конструктор для инициализации объектов"""
        self.__url = url
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__(url)

    def url_status(self):
        response = requests.get(self.__url)
        status = response.status_code
        if status == 200:
            return "Успешный запрос"
        else:
            return "Неуспешный запрос"

    def load_vacancies(self, keyword: str):
        """Метод, для записи вакансий"""

        self.__params["text"] = keyword
        while self.__params.get("page") != 1:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.__vacancies


# if __name__ == "__main__":
#     hh1 = HeadHunterAPI("https://api.hh.ru/vacancies")
#     hh2 = hh1.url_status()
#     print(hh2)
#     hh3 = hh1.load_vacancies("Python")
#     print(hh3)
