#Блюда с творогом выход 200 гр
#название блюд
#количество творога
#количества сахара
#количество яйца
#количество муки
#количество соли
list_of_dishes = [['зареканка с творогом',200,22,20,3,0 ], ['сырники',150,22,50,5,1], ['вареники ленивые',120,50,20,40,1]]
#print (list_of_dishes)

# поиск максимального садержания творога в блюде
def find_max_curd (z):
   max_curd=0
   for ingredients in z:
     print(ingredients[1])
     if(ingredients[1]>max_curd):
            max_curd=ingredients[1]
   print("максимальное содержание творога в блюде",max_curd)
   return max_curd

a=find_max_curd(list_of_dishes)
print ("максимального садержания творога в блюде",a)

from pprint import pprint
#функция для поиска числа в строке
def find_num_in_str(str):
    word_list = str.split()#разбили строку на слова
    for word in word_list:#для каждого слова
        if word.isnumeric():#проверяем является ли оно числовый
            return int(word)#возвращаем преобразование в число


# поиск возраста больше чем
# ingredients - словарь с персонами
# curd - переменная с возрастом который сравниваем
# delta - дельта или гистерезис

def find_curd (ingredients,curd):
    delta = 30  # можем тут менять гистерезис
    founded_ingredients = []#пустой список для хранения результатов
    for ingredients_index in ingredients:#для каждого индекса из словаря
        print(ingredients_index)#выводим индекс
        print(ingredients.get(ingredients_index))#выводим содержимое словаря по этому индексу
        print(ingredients.get(ingredients_index).curd)#выводим поле curd(творог) из содержимого по этому индексу
        if ((ingredients.get(ingredients_index).  curd <= (curd+delta)) and (ingredients.get(ingredients_index).curd >= (curd-delta))): #берем поле curd(творог) из содержимого по этому индексу и сравниваем с заданной переменной
            founded_ingredients.append(ingredients.get(ingredients_index))#если правда, то добавляем содержимое в список
    return founded_ingredients#возращаем список, наполненный в цикле for

#поиск возраста меньше чем
# ingredients - словарь с персонами
# curd - переменная с количеством который сравниваем
def find_curd_less_than (ingredients,curd):
    founded_ingredients = []  # пустой список для хранения результатов
    for ingredients_index in ingredients:  # для каждого индекса из словаря
        print(ingredients_index)#выводим индекс
        print(ingredients.get(ingredients_index))#выводим содержимое словаря по этому индексу
        print(ingredients.get(ingredients_index).curd)#выводим поле curd(творог) из содержимого по этому индексу
        if (ingredients.get( ingredients_index).curd < curd):  # берем поле curd(творог) из содержимого по этому индексу и сравниваем с заданной переменной
            founded_ingredients.append(ingredients.get(ingredients_index))  # если правда, то добавляем содержимое в список
    return founded_ingredients  # возращаем список, наполненный в цикле for


#поиск имени
# ingredients - словарь с ингридиентами
# блюдо - искомое имя
def find_food (ingredients,food):
    founded_ingredients = []#пустой список для хранения результатов
    for ingredients_index in ingredients:#для каждого индекса из словаря
       #print(ingredients_index)#выводим индекс
       #print(ingredients.get(ingredients_index))#выводим содержимое словаря по этому индексу
       # print(ingredients.get(ingredients_index).food)#выводим поле food(блюдо) из содержимого по этому индексу
        if (ingredients.get(ingredients_index).food == food):#берем поле food(блюдо) из содержимого по этому индексу и сравниваем с заданной переменной food
            founded_ingredients.append(ingredients.get(ingredients_index))#если правда, то добавляем содержимое в список
    return founded_ingredients#возращаем список, наполненный в цикле for

#описать классами ваши данные
class ingredients:
    def __init__(self,food, curd, sugar, egg, flour,salt ):
        self.food, self.curd, self.sugar, self.egg, self.flour, self.salt = food, curd, sugar, egg, flour,salt
        self.key = (food, curd)
    def __repr__(self):
        return "ingredients('%s',%d,%d,%d,%d,%d)" % (self.food, self.curd, self.sugar, self.egg, self.flour, self.salt)



#создаём объекты с ингридиентами

casserole=ingredients("запеканка с творогом",200,22,20,3,0)
cheesecakes=ingredients("сырники",150,22,50,5,1)
lazy_dumplings=ingredients("вареники ленивые",120,50,20,40,1)

#собираем объукты в словарь
list_of_dishes_dict= { casserole.key: casserole,
                      cheesecakes.key: cheesecakes,
                      lazy_dumplings.key: lazy_dumplings }
#выводим словарь
print(list_of_dishes_dict)

#разбор поискового запроса
search_str = input("введите поисковый запрос")

#могут быть следующие запросы:
#творог больше 150
#творог  меньше 100
#имя сырники
#муки больше 50
#муки меньше 30

#выводим поисковый запрос
#print("Поисковый запрос: ",search_str)

#если ищем творог
if 'творог' in search_str:#строка "творог" есть в поисковом запросе
    if 'больше' in search_str:#строка "больше" есть в поисковом запросе
        curd = find_num_in_str(search_str) #через функцию find_num_in_str ищем число в поисковом запросе
        print("Результат поиска: ",find_curd_more_than(list_of_dishes_dict,curd))#выполняем поиск по условию, выводим список результатов

    elif  'меньше' in search_str:
        curd = find_num_in_str(search_str)
        print("Результат поиска: ", find_curd_less_than(list_of_dishes_dict, curd))
    else:
        curd = find_num_in_str(search_str)
        print("Результат поиска: ", find_curd(list_of_dishes_dict, curd))
if 'блюдо' in search_str:
    #food = input()#альтернативный вариант указкния имени в поиске
    food = search_str[len('блюдо')+1:]#мы взали срез строки, начиная с позиции 3(длина слова 'блюдо') + 1 (пробел)
    print(food)
    print("Результат поиска: ", find_food(list_of_dishes_dict,food))