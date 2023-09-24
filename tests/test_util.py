from utils.util import operations, filter_operations, form_date, mask_num


def test_operations():
    response = operations()
    assert isinstance(response, list)  # Проверяем, что результат является списком
    assert len(response) > 0  # Проверяем, что словарь содержит данные


def test_filter_operations():
    transactions = [
        {'date': '2022-01-01', 'amount': 100},
        {'date': '2022-01-02', 'amount': 200},
        {'date': '2022-01-03', 'amount': 300},
        {'date': '2022-01-04', 'amount': 400},
        {'date': '2022-01-05', 'amount': 500},
        {'date': '2022-01-06', 'amount': 600},
        {'date': '2022-01-07', 'amount': 700},
        {'date': '2022-01-08', 'amount': 800},
        {'date': '2022-01-09', 'amount': 900},
        {'date': '2022-01-10', 'amount': 1000}
    ]
    result = filter_operations(transactions)
    assert isinstance(result, list)  # Проверяем, что результат является списком
    assert len(result) == 5  # Проверяем, что в списке содержится ровно 5 элементов


def test_form_date():
    date = '2022-01-01'
    result = form_date(date)
    assert isinstance(result, str)  # Проверяем, что результат является строкой
    assert len(result) == 10  # Проверяем, что строка имеет ожидаемую длину в формате ДД.ММ.ГГГГ


def test_mask_num():
    card_number = '1234567890123456789'
    account_number = 'Счет 09876543210987654321'
    result_card = mask_num(card_number)
    result_account = mask_num(account_number)
    assert isinstance(result_card, str)  # Проверяем, что результат для номера карты является строкой
    assert isinstance(result_account, str)  # Проверяем, что результат для номера счета является строкой
    assert len(result_card) == 21  # Проверяем, что строка имеет ожидаемую длину для номера карты
    assert len(result_account) == 6  # Проверяем, что строка имеет ожидаемую длину для номера счета
    assert result_card == '1234 5678** **** 6789'  # Проверяем, что номер карты был правильно замаскирован
    assert result_account == '**4321'  # Проверяем, что номер счета был правильно замаскирован

