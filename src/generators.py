def filter_by_currency(lst, string = 'RUB'):
    return [
        transaction
        for transaction in lst
        if transaction.get("operationAmount", {}).get("currency", {}).get("code")
        == string
    ]

def transaction_descriptions(lst):
    for transaction in lst:
        yield (transaction.get("description"))


def card_number_generator(start, end):
    for num in range(start, end+1):
        card_number = f"{num:016d}"
        yield " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
