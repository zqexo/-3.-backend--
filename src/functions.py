from datetime import datetime


def format_transaction(transaction):
    """
    Код для форматирования одной транзакции
    """
    date_format = '%d.%m.%Y'
    date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime(date_format)
    description = transaction['description']

    currency = transaction['operationAmount']['currency']['name']
    amount = float(transaction['operationAmount']['amount'])
    formatted_amount = '{:.2f}'.format(amount)

    # Проверяем наличие и форматируем информацию об отправителе, если она есть
    if 'from' in transaction and transaction['from']:
        # Разделяем строку для получения типа карты и номера
        card_type, card_number = transaction['from'].rsplit(' ', 1)
        from_account = '{} {} {}** **** {}'.format(card_type, card_number[:4], card_number[6:8], card_number[-4:])
    else:
        from_account = 'N/A'

    # Извлекаем и замаскируем счет получателя
    to_account_num = transaction['to'].split(' ')[1]
    to_account = 'Счет **{}'.format(to_account_num[-4:])

    # Собираем и возвращаем строку с информацией о транзакции
    transaction_info = f"{date} {description}\n{from_account} -> {to_account}\n{formatted_amount} {currency}"
    return transaction_info


def get_last_executed_transactions(data, count=5):
    """
    Код для сортировки и возврата последних 5-ти операций
    """
    transactions = []
    executed_operations = [op for op in data if op.get('state') == 'EXECUTED']

    # Сортировка операций по дате
    executed_operations.sort(key=lambda x: x['date'], reverse=True)

    # Форматирование и вывод на экран
    for operation in executed_operations[:count]:
        transactions.append(format_transaction(operation))
        transactions.append('\n')  # Пустая строка между операциями

    # Вывод списка операций с разделением пустой строкой
    return '\n'.join(transactions)
