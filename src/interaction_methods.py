import json

from src.abstract_class import AbstractMethods


class WorkMethods(AbstractMethods):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    @staticmethod
    def save_vacancies(vacancies):
        """Запись списка вакансий в файл"""
        with open("..\\data\\vacancies.json", "w", encoding="utf8") as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            f.write(vacancies_json)

    def get_data(self, criterion):
        """Метод получения данных из файла по указанным критериям"""
        with open("..\\data\\vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            criterion_vac = []
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def delete_vacancy(self):
        """Метод удаления данных из файла"""
        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("..\\data\\vacancies.json", "w", encoding="utf8") as f:
            f.write(list)
