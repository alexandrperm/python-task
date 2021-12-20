# 1. оформить функциями поиск в списке
# имя, фамилия
# возраст
# количество  музыкальных посещений
# количество часов прибываня в центре
# количество танцевальных посещений

peoples_list = [['Степан Марков', 8, 12, 63, 10], ['Света Беляева', 7, 5, 56, 13], ['Наталья Петрова', 9, 6, 25, 16]]
visitors_list = [['Степан Марков', 8, 12, 63, 10], ['Света Беляева', 7, 5, 56, 13], ['Наталья Петрова', 9, 6, 25, 16]]
print(peoples_list)


# поиск максимального количества часов посещений в списке
def find_max_visit(a):
    max_visit = 0
    for people in a:
        if people[3] > max_visit:
            max_visit = people[3]
    return max_visit

# максимальное посещения тантев
def find_max_dance(a):
    max_dance = 0
    for people in a:
       if (people[4] > max_dance):
         max_dance = people[4]
    return max_dance


#  поиск минимального посещения танцев
def find_min_dance(a):
     min_dance = peoples_list[0][4]
     for people in a:
         if (people[4] < min_dance):
               min_dance = people[4]
     return min_dance



# минимальный возраст
def find_min_age(z):
    min_age = 100
    for people in z:
        if (people[1] < min_age):
            min_age = people[1]
    return min_age

x = find_max_visit(peoples_list)
print("максимальное количества часов посещений",x)

x = find_max_dance(peoples_list)
print('максимальное количество часов посещений танцев', x)

x = find_min_dance(peoples_list)
print('минимальное посещения танцев', x)

x = find_min_age(peoples_list)
print('минимальный возраст',x )