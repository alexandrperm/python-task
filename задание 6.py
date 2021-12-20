from pprint import pprint
#функция для поиска числа в строке
def find_num_in_str(str):
    word_list = str.split()#разбили строку на слова
    for word in word_list:#для каждого слова
        if word.isnumeric():#проверяем является ли оно числовый
            return int(word)#возвращаем преобразование в число

#поиск возраста больше чем
# persons - словарь с персонами
# age - переменная с возрастом который сравниваем

def find_age_more_than (persons,age):
    founded_persons = []#пустой список для хранения результатов
    for person_index in persons:#для каждого индекса из словаря
        #print(person_index)#выводим индекс
        #print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        #print(persons.get(person_index).age)#выводим поле age(возраст) из содержимого по этому индексу
        # берем поле age(возраст) из содержимого по этому индексу и сравниваем с заданной переменной
        if (persons.get(person_index).age >= age):
            founded_persons.append(persons.get(person_index))#если правда, то добавляем содержимое в список
    return founded_persons#возращаем список, наполненный в цикле for

#поиск возраста меньше чем
# persons - словарь с персонами
# age - переменная с возрастом который сравниваем
def find_age_less_than (persons,age):
    founded_persons = []#пустой список для хранения результатов
    for person_index in persons:#для каждого индекса из словаря
        #print(person_index)#выводим индекс
        #print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        #print(persons.get(person_index).age)#выводим поле age(возраст) из содержимого по этому индексу
        if (persons.get(person_index).age < age):#берем поле age(возраст) из содержимого по этому индексу и сравниваем с заданной переменной
            founded_persons.append(persons.get(person_index))#если правда, то добавляем содержимое в список
    return founded_persons#возращаем список, наполненный в цикле for

#поиск возраста
# persons - словарь с персонами
# age - переменная с возрастом который сравниваем
# delta - дельта или гистерезис
def find_age (persons,age):
    delta = 2#можем тут менять гистерезис
    founded_persons = []#пустой список для хранения результатов
    for person_index in persons:#для каждого индекса из словаря
        #print(person_index)#выводим индекс
        #print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        #print(persons.get(person_index).age)#выводим поле age(возраст) из содержимого по этому индексу
        # берем поле age(возраст) из содержимого по этому индексу и сравниваем с заданной переменной
        if ((persons.get(person_index).age <= (age+delta)) and (persons.get(person_index).age >= (age-delta))):
            founded_persons.append(persons.get(person_index))#если правда, то добавляем содержимое в список
    return founded_persons#возращаем список, наполненный в цикле for


#поиск имени
# persons - словарь с персонами
# name - искомое имя
def find_name (persons,name):
    founded_persons = []#пустой список для хранения результатов
    for person_index in persons:#для каждого индекса из словаря
        #print(person_index)#выводим индекс
        #print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        #print(persons.get(person_index).name)#выводим поле name(имя) из содержимого по этому индексу
        if (persons.get(person_index).name == name):#берем поле name(имя) из содержимого по этому индексу и сравниваем с заданной переменной name
            founded_persons.append(persons.get(person_index))#если правда, то добавляем содержимое в список
    return founded_persons#возращаем список, наполненный в цикле for


def find_visits_more_than(persons, visits):
    founded_persons = []  # пустой список для хранения результатов
    for person_index in persons:  # для каждого индекса из словаря
        # print(person_index)#выводим индекс
        # print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        # print(persons.get(person_index).visits)#выводим поле visits(посещений) из содержимого по этому индексу
        if (persons.get(
                person_index).visits >= visits):  # берем поле visits(посещений) из содержимого по этому индексу и сравниваем с заданной переменной
            founded_persons.append(persons.get(person_index))  # если правда, то добавляем содержимое в список
        return founded_persons  # возращаем список, наполненный в цикле for


# if 'меньше' in search_str:

def find_visits_less_than(persons, visits):
    founded_persons = []  # пустой список для хранения результатов
    for person_index in persons:  # для каждого индекса из словаря
        # print(person_index)#выводим индекс
        # print(persons.get(person_index))#выводим содержимое словаря по этому индексу
        # print(persons.get(person_index).visits)#выводим поле visits(посещений) из содержимого по этому индексу
        if (persons.get(
                person_index).visits < visits):  # берем поле visits(посещений) из содержимого по этому индексу и сравниваем с заданной переменной
            founded_persons.append(persons.get(person_index))  # если правда, то добавляем содержимое в список
    return founded_persons  # возращаем список, наполненный в цикле for


# могут быть следующие запросы:
#print("Поисковый запрос: ", search_str)


#описать классами ваши данные
class Person:
    def __init__(self, name, age, music, visits, dance ):
        self.name, self.age, self.music, self.visits, self.dance = name, age, music, visits, dance
        self.key = (name,age)
    def __repr__(self):
        return "Person('%s',%d,%d,%d,%d)" % (self.name, self.age, self.music, self.visits, self.dance)






#создаём объекты с посетитилями
stepan = Person("Степан",8,12,63,10)
sveta = Person("Света",7,5,56,13)
natali = Person("Наталья",9,6,25,16)

#собираем объекты в словарь
people_dict = { stepan.key: stepan,
                sveta.key: sveta,
                natali.key: natali}

#выводим словарь
pprint(people_dict)

#разбор поискового запроса
search_str = input("введите поисковый запрос")

#могут быть следующие запросы:
#возраст больше 10
#возраст меньше 15
#имя Степан
#посещений больше 50
#посещений меньше 19

#выводим поисковый запрос
print("Поисковый запрос: ",search_str)

#если ищем возраст
if 'возраст' in search_str:#строка "возраст" есть в поисковом запросе
    if 'больше' in search_str:#строка "больше" есть в поисковом запросе
        age = find_num_in_str(search_str) #через функцию find_num_in_str ищем число в поисковом запросе
        print("Результат поиска: ",find_age_more_than(people_dict,age))#выполняем поиск по условию, выводим список результатов

    elif 'меньше' in search_str:
        age = find_num_in_str(search_str)
        print("Результат поиска: ", find_age_less_than(people_dict, age))
    else:
        age = find_num_in_str(search_str)
        print("Результат поиска: ", find_age(people_dict, age))


if 'имя' in search_str:
    #name = input()#альтернативный вариант указкния имени в поиске
    name = search_str[len('имя')+1:]#мы взали срез строки, начиная с позиции 3(длина слова 'имя') + 1 (пробел)
    print("Результат поиска: ", find_name(people_dict,name))

#if 'посещений' in search_str:
#if 'больше' in search_str:
#если ищем посещений
if 'посещений' in search_str:#строка "посещений" есть в поисковом запросе
    if 'больше' in search_str:#строка "больше" есть в поисковом запросе
        visits = find_num_in_str(search_str) #через функцию find_num_in_str ищем число в поисковом запросе
        print("Результат поиска: ",find_visits_more_than(people_dict,visits))#выполняем поиск по условию, выводим список результатов

    if 'меньше' in search_str:
        visits = find_num_in_str(search_str)
        print("Результат поиска: ", find_visits_less_than(people_dict, visits))



