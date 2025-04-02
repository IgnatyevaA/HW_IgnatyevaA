import re
from collections import Counter

def filter_operations_by_string(list_tran: list[dict], str_search: str) -> list[dict]:
    pattern = re.compile(str_search, re.IGNORECASE)
    operations = [
        operations
        for operations in list_tran
        if pattern.search(operations.get("description", ""))
    ]
    return operations

def count_operations_by_description(operations, descriptions):
    lst = [operation["description"] for operation in operations if operation["description"] in descriptions]
    return Counter(lst)
