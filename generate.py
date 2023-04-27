import datetime
import random


def full_dict_compare(left, right):
    if left != right:
        return False
    for key, value in left.items():
        if value != right[key]:
            print(value, right[key])
            return False
    return True


def generate_date(args_dict):
    """
    Функция генерирует дату на основе переданных аргументов
    Возвращает строку в формате 'ДД.ММ.ГГГГ'
    """

    anchor_date = args_dict.get('anchor_date', None)
    other_date = args_dict.get('other_date', None)
    days = args_dict.get('days', 0)
    months = args_dict.get('months', 0)
    years = args_dict.get('years', 0)
    form = args_dict.get('form', '%d.%m.%Y')

    if not anchor_date:
        anchor_date = datetime.date.today()
    if isinstance(anchor_date, str):
        anchor_date = datetime.datetime.strptime(anchor_date, '%d.%m.%Y').date()

    if not isinstance(anchor_date, datetime.date):
        raise ValueError('Некорректный формат опорной даты')

    year = anchor_date.year + years
    month = anchor_date.month + months
    day = anchor_date.day + days

    if month <= 0:
        year -= 1
        month += 12

    days_in_month = {
        1: 31,
        2: 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    while day <= 0:
        month -= 1
        if month <= 0:
            year -= 1
            month += 12
        day += days_in_month[month]

    while day > days_in_month[month]:
        day -= days_in_month[month]
        month += 1
        if month > 12:
            year += 1
            month -= 12

    generated_date = datetime.date(year, month, day) if other_date is None else other_date

    max_date = anchor_date if anchor_date > generated_date else generated_date
    min_date = anchor_date if max_date == generated_date else generated_date

    if min_date == max_date:
        return datetime.date.today().strftime(form)

    delta_days = random.randint(1, (max_date - min_date).days)

    return (max_date - datetime.timedelta(delta_days)).strftime(form)