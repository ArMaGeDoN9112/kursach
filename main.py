from datetime import datetime
from zoneinfo import ZoneInfo
import json
from pprint import pprint
import os.path


def print_multiple_choice(list_of_choices: list, phrase: str):
    print(phrase)
    for i in range(len(list_of_choices)):
        print(f'"{i}" - {list_of_choices[i]}')


def check_int_in_range(min: int, max: int) -> str:
    check = input("Введите число: ")
    while not check.isdecimal() or int(check) > max or int(check) < min:
        print("Число введено неверно...")
        check = input("Введите число заного: ")

    return check


def add_card_in_db(db: dict):
    new_card = str(int(list(db.keys())[-1]) + 1)

    while len(new_card) < 4:
        new_card = "0" + new_card

    db[new_card] = {}
    return new_card


def delete_from_db(db: dict):
    card_number = input("Введите номер карты, которую нужно очистить: ")

    db[card_number] = {}


def check_name():
    name = input("Введите полное ФИО пользователя: ")
    while len(name.split()) != 3:
        print("Недостаточно введенных данных...")
        name = input("Введите полное ФИО пользователя: ")
    return name


def check_permission_level(permission_list: list):
    print_multiple_choice(permission_list, "Выберите нужный уровень: ")
    permission_level = input("Введите цифру: ")
    while not permission_level.isdecimal() or int(permission_level) >= len(permission_list):
        print("Неверное значение...")
        permission_level = input("Введите цифру: ")
    return permission_level


def get_time() -> str:
    return datetime.now(tz=ZoneInfo("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")


def input_data_about_employee(db: dict, permission_list: list):
    for i in list(db.keys()):
        if db[i] == {}:
            card_number = i
            break
    else:
        card_number = add_card_in_db(db)

    name = check_name()

    print_multiple_choice(permission_list, "Введите уровень доступа для этой карты...")

    permission_level = check_permission_level(permission_list)

    time = get_time()

    db[card_number] = {"name":name, "permission_level":permission_level, "add_time":time}

    print(f"Человеку с именем - {name} была присвоена карта с номером - {card_number}")
    # add data to database


def change_data_in_db(change_variables: list[str], db: dict, permission_list: list):
    card_number = input("Введите номер карты, для которой нужно изменить данные: ")

    if db[card_number] == {}:
        print("Данные карты пусты. Изменить нечего...\n")

        return

    time = get_time()

    print_multiple_choice(change_variables, "Выберите что хотите изменить:")
    to_change = int(check_int_in_range(0, len(change_variables)))

    match to_change:
        case 0:
            db[card_number][change_variables[to_change]] = check_name()
        case 1:
            db[card_number][change_variables[to_change]] = check_permission_level(permission_list)
    db[card_number]["change_time"] = time


def convert_dict_to_json(db: dict):
    with open("local_database.json", "w") as outfile:
        json.dump(db, outfile, ensure_ascii=False, indent=4)
    outfile.close()

def get_dict_from_json() -> dict:
    path = './local_database.json'
    check = os.path.isfile(path)
    if (check):
        with open("local_database.json", "r") as read_file:
            data = json.load(read_file)
            read_file.close()
            return data
    return {"0000": {}}

change_variables = ["name", "permission_level"]
permission_list = ["Обычный", "Склад"]

if __name__ == "__main__":
    data = get_dict_from_json()


    while True:
        modes = ["Добавить нового сотрудника", "Изменить данные карты",
                 "Очистить данные с карты", "Показать базу данных"]

        print_multiple_choice(modes, "Выберите режим: ")
        mode = int(check_int_in_range(0, len(modes)))

        match mode:
            case 0:
                input_data_about_employee(data, permission_list)
            case 1:
                change_data_in_db(change_variables, data, permission_list)
            case 2:
                delete_from_db(data)
            case 3:
                print()
                pprint(data)
                print()

        convert_dict_to_json(data)
