from combidata import *
from re_generate import re_generate

from steps import *

library = {
    "cases": {},
    "workflow": {"standard": (ST_COMBINE, ST_GENERATE, ST_FORM, EXPORT, ASK, COMPARE),
                 "error": (ST_COMBINE, ST_GENERATE, ST_FORM, EXPORT, ER_COMPARE)},
    "tools": {},
    "template": {}
}
library["cases"]["ID_CARD"] = {
    "Correct": {
        "value": r"[0-9]{9}",
        "gen_func": re_generate,
        "name": "Проверка поля ID_CARD на корректное значение"
    },
    "None": {
        "is_presented": False,
        "type": "error",
        "error": {"ERROR": "Неправильно заполнено поле ID_CARD"},
        "name": "Проверка поля ID_CARD на присутствие ошибки по обязательности поля"
    },
    "NCorrectValue": {
        "value": r"[0-9]{10,15}|[0-9]{1,8}",
        "gen_func": re_generate,
        "type": "error",
        "error": {"ERROR": "Неправильно заполнено поле ID_CARD"},
        "name": "Проверка поля ID_CARD присутствие ошибки по некорректному значению"
    },
    "NCorrectSy": {
        "value": r"[A-Za-z]{1,5}",
        "gen_func": re_generate,
        "type": "error",
        "error": {"ERROR": "Неправильно заполнено поле ID_CARD"},
        "name": "Проверка поля ID_CARD на присутствие ошибки по некорректным символам"
    },
}
library["cases"]["PASSPORT"] = {
    "Correct": {
        "value": r"[0-9]{2} [0-9]{2} [0-9]{6}",
        "gen_func": re_generate,
        "name": "Проверка поля PASSPORT на корректное значение"
    },
    "Noness": {
        "is_presented": False,
        "name": "Проверка поля PASSPORT на необязательность"
    },
    "None": {
        "is_presented": False,
        "type": "off",
        "error": {"ERROR": "Неправильно заполнено поле PASSPORT"},
        "name": "Проверка поля PASSPORT на присутствие ошибки по обязательности поля"
    },
    "NCorrectValue": {
        "value": r"[0-9]{10}|[0-9]{11,15}|[0-9]{1,9}",
        "gen_func": re_generate,
        "type": "error",
        "error": {"ERROR": "Неправильно заполнено поле PASSPORT"},
        "name": "Проверка поля PASSPORT присутствие ошибки по некорректному значению"
    },
    "NCorrectSy": {
        "value": r"[A-Za-z]{1,5}",
        "gen_func": re_generate,
        "type": "error",
        "error": {"ERROR": "Неправильно заполнено поле PASSPORT"},
        "name": "Проверка поля PASSPORT на присутствие ошибки по некорректным символам"
    },
}
library["template"] = {field: field for field in library["cases"].keys()}
