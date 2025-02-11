from src.extra_functions import sorting
from src.interaction_hh_ru import HeadHunterAPI
from src.interaction_methods import WorkMethods


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    name_vacancies = input("Введите вакансию для поиска на сайте hh.ru: ")
    cl1 = HeadHunterAPI()
    cl12 = cl1.load_vacancies(name_vacancies)

    cl21 = WorkMethods()
    cl21.save_vacancies(cl12)

    name_criterion = input("Введите критерий для отбора вакансий: ")
    cl21.get_data(name_criterion)

    N = int(input("Введите количество топ-N вакансий для просмотра: "))
    cl31 = sorting(N)
    print(cl31)

    name_exit = input("Завершить и очистить файл вакансий да/нет: ")
    if name_exit == "да":
        cl21.delete_vacancy()
    else:
        user_interaction()


user_interaction()
