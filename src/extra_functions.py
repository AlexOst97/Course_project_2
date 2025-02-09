import json

from src.interaction_vacancies import WorkVacancies


def information_output(my_file="..\\data\\vacancies.json"):
    """Функция, для вывода информации"""

    with open(my_file, "r", encoding="utf8") as f:
        vacancies = json.load(f)
    list_info = []
    for vac in vacancies:
        if not vac["salary"]:
            vac["salary"] = 0
        else:
            if vac["salary"] is None:
                vac["salary"] = 0
            else:
                if vac["salary"]["currency"]:
                    vac["currency"] = vac["salary"]["currency"]
                else:
                    vac["currency"] = "Валюта не определена"
                if vac["salary"]["from"] is None and vac["salary"]["to"] is None:
                    vac["salary"] = 0
                else:
                    if vac["salary"]["from"] is None and vac["salary"]["to"] is not None:
                        vac["salary"] = vac["salary"]["to"]
                    else:
                        if vac["salary"]["from"] is not None and vac["salary"]["to"] is None:
                            vac["salary"] = vac["salary"]["from"]
                        else:
                            if vac["salary"]["from"] is not None and vac["salary"]["to"] is not None:
                                vac["salary"] = vac["salary"]["to"]
        if vac["snippet"]["requirement"]:
            vac["snippet"]["requirement"] = vac["snippet"]["requirement"]
        else:
            vac["snippet"]["requirement"] = "Информация отсутствует"
        list_info.append(vac)
    return list_info


def sorting(N):
    """Функция, для получения топ N вакансий по зарплате"""

    list_info = information_output()
    sorted_list = sorted(list_info, key=lambda x: x["salary"], reverse=True)
    sorted_vac = sorted_list[:N]
    sort_vac = []
    for vac in sorted_vac:
        if not vac["salary"]:
            vac["salary"] = 0
        else:
            if vac["salary"] is None:
                vac["salary"] = 0
        sort_vac.append(WorkVacancies(vac["name"], vac["area"], vac["salary"], vac["snippet"]))
    print(sort_vac)
    return sort_vac


if __name__ == "__main__":
    xxx1 = information_output("..\\tests\\test_vacancies.json")
    xxx2 = sorting(1)
