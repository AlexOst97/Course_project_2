import requests
from src.abstract_class import AbstractApi
import json

class HeadHunterAPI(AbstractApi):
    '''Класс подключаться к API hh.ru и получает вакансии'''

    def __init__(self, file_worker: str):
        '''Конструктор для инициализации объектов'''
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        '''Метод, для записи вакансий'''

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


# if __name__ == "__main__":
#     hh1 = HeadHunterAPI(file_worker="..\\data\\vacancies.json")
#     hh2 = hh1.load_vacancies("Инженер")
#     print(hh2)