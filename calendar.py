from datetime import *


def dia_da_semana(x):
    return {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 0,
    }[x]


def mes(x):
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


lista = [[0 for i in range(7)] for j in range(6)]

data_atual = date.today()

while True:
    try:
        data_atual = data_atual.replace(day=1)
        dia = data_atual

        while dia_da_semana(data_atual.weekday()) != 0:
            data_atual -= timedelta(days=1)

        for i in range(6):
            for j in range(7):
                lista[i][j] = data_atual.strftime('%d')
                data_atual += timedelta(days=1)

        print(f"{mes(dia.month)} - {dia.year}")
        for line in lista:
            print(line)

        usr = input("p or n:\n")
        if usr == "p":
            data_atual = dia.replace(day=1) - timedelta(days=1)
            data_atual.replace(day=1)
        elif usr == "n":
            data_atual = dia.replace(day=1) + timedelta(days=32)
            data_atual.replace(day=1)

    except IOError:
        break
