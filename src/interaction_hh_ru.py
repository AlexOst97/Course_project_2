import requests
from src.abstract_class import WorkApi
import json

class HeadHunterAPI(WorkApi):
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

    def save_vacancies(self):
        '''Сохраняет полученные вакансии в файл'''
        try:
            with open(self.file_worker, 'w', encoding='utf-8') as file:
                json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
            print(f"Вакансии сохранены в {self.file_worker}")
        except Exception as error:
            print(f"Ошибка сохранения: {error}")


if __name__ == "__main__":
    hh = HeadHunterAPI(file_worker="..\\data\\vacancies_hh_ru.json")
    hh.load_vacancies("Инженер")
    hh.save_vacancies()