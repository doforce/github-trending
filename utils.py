import re


def get_list_num(arr: list[str]):
    return int("".join(re.compile(r'\d+').findall(''.join(arr))))
