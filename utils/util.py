import requests
from dateutil.parser import parse

# Список транзакций подготовленный для сортировки
transactions = []


def operations():
    """Выгрузка данных из json"""
    response = requests.get('https://api.npoint.io/f1760286ce84f3be5c5c')
    oper = response.json()
    return oper


def filter_operations(transactions):
    """Сортировка транзакций по дате в обратном порядке и взятие последних 5 операций"""
    sorted_operations = sorted(transactions, key=lambda x: x['date'], reverse=True)
    last_5_operations = sorted_operations[:5]
    return last_5_operations


def form_date(date):
    """Изменение формата даты в ДД.ММ.ГГГГ"""
    date_string = operation.get('date')
    meta = f"{parse(date_string):%d.%m.%Y}"
    return meta


def mask_num(number):
    """Формат вывода данных карты и счета:
    - Номер карты замаскирован и не отображается целиком в формате XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    - Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета)."""
    if "Счет" in number:
        account_number = f"**{number[-4:]}"
        return account_number
    return f"{number[:4]} {number[4:8]}** **** {number[-4:]}"


# Фильтрация транзакций по статусу EXECUTED
for operation in operations():
    if operation.get('state') == "EXECUTED":
        transactions.append(operation)

# Вызов функции для фильтрации операций
filtered_operations = filter_operations(transactions)

# Вывод отфильтрованных операций
for operation in filtered_operations:
    print(form_date(operation.get('date')), operation.get('description'))

    if operation.get('from') is not None:
        print(mask_num(operation.get('from')), "->", mask_num(operation.get('to')))
    else:
        print("->", mask_num(operation.get('to')))

    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
    print(' ')
