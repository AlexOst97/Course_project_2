from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def __init__(self, url):
        self.url = url


class AbstractMethods(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_data(self, *args):
        """Метод, для получения данных"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Метод, для удаления вакансий"""
        pass
