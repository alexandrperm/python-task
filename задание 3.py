# Имя - Светлана
# Фамилия - Беляева
# Возраст - 34
# Колличество котов - 2
# Колличество собак - 1

#1. Описать себя, используюя список
peoples_list=[['Светлана','Беляева',34,2,1],
              ['Иван','Петров',18,4,1],
              ['Еся','Беляева',2,2,3]]


#поиск максимального возраста
max_age = 0
for people in peoples_list:
    print(people[2])
    if(people[2] > max_age):
        max_age = people[2]
print("Максимальный возраст",max_age)

max_cat=0
for people in peoples_list:
    print(people[3])
    if(people[3] > max_cat):
        max_cat = people[3]
print("максимальное количество котов", max_cat)

min_cat=max_cat
for people in peoples_list:
    if(people[3] < min_cat):
        min_cat = people[3]
print("минимальное количество котов", min_cat)

#поиск минимального колличества котов


#ввод данных
new_name = input ("Введите имя нового человека: ")
new_forname = input ("Введите фамилию нового человека: ")
new_age = int(input ("Введите возраст нового человека: "))
#todo доделать остальные поля
new_people=[new_name,new_forname,new_age,0,0]
peoples_list.append(new_people)
print("Список с новыми данными",peoples_list)


#2. Описать себя, используюя словарь
print("2. Описать себя, используюя словарь")
peoples_dict={'первый':{'Имя':'Светлана','Фамилия':'Беляева','Возраст':34,'Колличество котов':2,'Колличество собак':1},
              'второй':{'Имя':'Светлана','Фамилия':'Беляева','Возраст':34,'Колличество котов':2,'Колличество собак':1},
              'третий':{'Имя':'Светлана','Фамилия':'Беляева','Возраст':34,'Колличество котов':2,'Колличество собак':1}}
print(peoples_dict)

#поиск максимального возраста
max_age = 0
for people_index in peoples_dict:
    #print(people_index)
    #print(peoples_dict.get(people_index))
    #print(peoples_dict.get(people_index).get("Возраст"))
    if(peoples_dict.get(people_index).get("Возраст") > max_age):
        max_age = peoples_dict.get(people_index).get("Возраст")
print("Максимальный возраст",max_age)

