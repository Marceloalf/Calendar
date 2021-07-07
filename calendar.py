from datetime import *


def format_calendar():
    return [[0 for i in range(7)] for j in range(6)]


def day_of_week(x):
    return {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 0,
    }[x]


def month(x):
    return {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }[x]


def first_day_of_the_month(day):
    return day.replace(day=1)


def first_day_first_week(day):
    first = day

    while day_of_week(first.weekday()) != 0:
        first -= timedelta(days=1)

    return first


def calendar_page(days, first):
    for weeks in range(6):
        for day in range(7):
            days[weeks][day] = first.strftime('%d')
            first += timedelta(days=1)

    return days


def header(day):
    return f"{month(day.month)} - {day.year}"


def main():
    calendar = format_calendar()

    today = date.today()
    today = first_day_of_the_month(today)

    first = first_day_first_week(today)

    calendar = calendar_page(calendar, first)

    print(header(today))
    for line in calendar:
        print(line)


if __name__ == '__main__':
    main()
