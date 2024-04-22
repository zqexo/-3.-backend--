from datetime import datetime
from src.functions import format_transaction
from src.functions import get_last_executed_transactions
import json
import pytest
def test_format_transaction_executed():
    transaction_executed = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    # формат даты может изменяться в зависимости от импортированной функции
    date_format = '%d.%m.%Y'
    date = datetime.strptime(transaction_executed['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(date_format)
    expected_output = f"{date} Перевод организации\nMaestro 1596 78** **** 5199 -> Счет **9589\n31957.58 руб."
    print(format_transaction(transaction_executed))
    assert format_transaction(transaction_executed) == expected_output

def test_get_last_executed_transactions():
    with open('../operations.json', 'r', encoding='utf-8') as file:
        test_data = json.load(file)
    assert get_last_executed_transactions(test_data) == """08.12.2019 Открытие вклада
N/A -> Счет **5907
41096.24 USD


07.12.2019 Перевод организации
Visa Classic 2842 88** **** 9012 -> Счет **3655
48150.39 USD


19.11.2019 Перевод организации
Maestro 7810 65** **** 5568 -> Счет **2869
30153.72 руб.


13.11.2019 Перевод со счета на счет
Счет 3861 39** **** 9794 -> Счет **8125
62814.53 руб.


05.11.2019 Открытие вклада
N/A -> Счет **8381
21344.35 руб.

"""