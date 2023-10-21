import datetime as dt

FORMAT = '%H:%M:%S' # Формат полученного времени.
WEIGHT = 75  # Вес. 
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    if len(data) != 2 or data[0] == '' or data[0] == None or data[1] == '' or data[1] == None:
        return True
    else:
        return False
    #Проверка корректности полученного пакета.
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time(time):
    mass_time = time.split(':')
    for i in range(len(mass_time)):
        if mass_time[i][0] == '0' and mass_time[i] != '00' and mass_time [i] != '0':
            mass_time[i] = mass_time[i].replace('0','', 1) 
    if len(time) == 7 and (int(mass_time[0]) >= 0 and int(mass_time[0]) < 24) and \
        (int(mass_time[1]) >= 0 and int(mass_time[1]) < 61) and (int(mass_time[2]) >= 0 and int(mass_time[2]) < 61): 
        return True
    else:
        return False
    #Проверка корректности параметра времени.
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True 


def get_step_day(steps):
    #Получить количество пройденных шагов за этот день.
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните эту сумму.
    summ_of_steps = 0
    for i in steps.values():
        summ_of_steps += i
    return summ_of_steps
    
    

def get_distance(day_steps):
    return (day_steps * STEP_M) / 1000
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.

    

def get_spent_calories(dist, current_time):
    time = dt.time.fromisoformat(current_time)
    minutes = time.hour * 60 + time.minute
    men_speed = dist / (minutes / 60)
    spent_calories = (K_1 * WEIGHT + (men_speed**2 / HEIGHT)\
                       * K_2 * WEIGHT) * minutes
    return spent_calories
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.

def get_achievement(dist):
    if dist >= 6.5 : return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9 : return 'Неплохо! День был продуктивный'
    elif dist >= 2 : return 'Завтра наверстаем!'
    else: return 'Лежать тоже полезно. Главное — участие, а не победа!'
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.


def show_message(time, day_steps, dist, spent_calories, achievement):
    out = (f'''
Время: {time}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{achievement}
''')
    print(out)
    return out

def accept_package(data):
    # Если функция проверки пакета вернет False
    if check_correct_data(data):
        return 
    # Распакуйте полученные данные.
    # Преобразуйте строку с временем в объект типа time.
    time = data[0]
    if check_correct_time(time):
        if len(time) != 8:
            time = '0' + time
        pack_time =  dt.time.fromisoformat(time)
    else:
        return 'Некорректное значение времени'
    list_storage_data = list(storage_data.keys())
    if len(list_storage_data) != 0 and list_storage_data[-1] >= pack_time:
        return
    storage_data[pack_time] = data[1]
    day_steps = get_step_day(storage_data)# Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)# Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, time) # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    # Добавьте новый элемент в словарь storage_data.
    # Верните словарь storage_data.
    return storage_data
    
# Данные для самопроверки.Не удаляйте их. 

package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)