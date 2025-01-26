import random

with open("C:\MyPythonProjects\sep25\singular.txt") as file:
    text_array = [row.strip() for row in file]

lim = 4
counter = 0  # счётчик для ограничения вывода
max_words = 10  # максимальное количество слов для вывода

# функция, которая склеивает слова
def glue(x, y):
    global counter  # используем глобальный счётчик
    # находим максимальное доступное количество букв пересечения для этих двух слов
    start = min(len(x), len(y)) - 1
    # пока это количество больше минимального
    while start >= lim:
        s1 = x[-start:]  # берём конец первого слова
        s2 = y[:start]   # берём начало второго слова
        if s1 == s2:  # если они равны
            s = x + y[start:]  # склеиваем эти слова
            if s not in text_array:  # если получившегося слова нет в изначальном словаре
                print(s + " = " + x + " + " + y)
                counter += 1  # увеличиваем счётчик
                if counter >= max_words:  # если достигли лимита
                    return True  # возвращаем True для остановки
            break  # как только нашли пересечение слов — выходим из цикла
        else:
            start -= 1  # уменьшаем количество букв для пересечения
    return False  # возвращаем False, если продолжать нужно

# случайное перемешивание слов
random.shuffle(text_array)

# перебираем все слова с первого до предпоследнего
for i in range(0, len(text_array) - 1):
    for j in range(i + 1, len(text_array)):
        if glue(text_array[i], text_array[j]):  # пробуем найти пересечение первого слова со вторым
            break  # если достигли лимита, выходим из вложенного цикла
        if glue(text_array[j], text_array[i]):  # пробуем второго — с первым
            break  # если достигли лимита, выходим из вложенного цикла
    if counter >= max_words:  # если достигли лимита, выходим из внешнего цикла
        break
