from abc import ABC, abstractmethod

class WorkApi(ABC):
    '''Абстрактный класс для работы с API сервиса с вакансиями'''

    @abstractmethod
    def __init__(self, file_worker):
        self.file_worker = file_worker