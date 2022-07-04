import csv


FIRST_PATH = '17.csv'
SECOND_PATH = '27.csv'


def get_seconds(time_str):
    """Функция для перевода кривого времени в конкректно этом csv из строки в секунды"""
    time_list = time_str.split('.')
    t = 0
    if time_list[1][-3:] == 'мин':
        t += int(time_list[1][:3]) * 60
        t += int(time_list[0][:2]) * 3600
    elif time_list[1][-3:] == 'сек':
        t += int(time_list[1][:3])
        t += int(time_list[0][:2]) * 60
    elif time_list[0].find('ч'):
        t += int(time_list[0][:2]) * 3600
    return t


def main():
    data = []
    # вытаскиваем данные из файла в список словарей

    with open(FIRST_PATH, newline='', encoding='utf-8') as file:
        data_first = list(csv.DictReader(file))
        data_first.pop()
        data_first.pop()
    with open(SECOND_PATH, newline='', encoding='utf-8') as file:
        data_second = list(csv.DictReader(file))
        data_second.pop()
        data_second.pop()

    sb = 0
    st = 0
    k = 0

    for row in data_first:
        if row['Завершено'] != '-':
            sb += float(row["Оценка/100,00"].replace(',', '.'))
            st += get_seconds(row["Затраченное время"])
            k += 1
    sb /= 10

    for row in data_second:
        if row['Завершено'] != '-':
            sb += float(row["Оценка/10,00"].replace(',', '.'))
            st += get_seconds(row["Затраченное время"])
            k += 1

    sb /= k
    st /= k

    answers = []
    for row in data_first:
        if row['Завершено'] != '-':
            if float(row["Оценка/100,00"].replace(',', '.')) / 10 and get_seconds(row["Затраченное время"]) < st:
                answers.append(row)

    for row in data_second:
        if row['Завершено'] != '-':
            if float(row["Оценка/10,00"].replace(',', '.')) and get_seconds(row["Затраченное время"]) < st:
                answers.append(row)

    print(len(answers))
    print(*answers, sep='\n')


if __name__ == '__main__':
    main()
