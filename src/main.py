import json
from src.functions import get_last_executed_transactions


def main():
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    print(get_last_executed_transactions(data))

main()
