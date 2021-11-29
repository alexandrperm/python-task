
# имя, фамилия
# возраст
# количество  музыкальных посещений
# количество часов прибываня в центре
# количество танцевальных посещений

peoples_list=[['Степан Марков',8,12,63,10],['Света Беляева',7,5,56,13],['Наталья Петрова',9,6,25,16]]
print(peoples_list)

# поиск максимального количества часов посещений
max_visit=0
for people in peoples_list:
   print(people[3])
   if(people[3]>max_visit):
        max_visit=people [3]
print('максимальное количество часов посещений',max_visit)

# максимальное посещения тантев
max_dance=0
for people in peoples_list:
   print(people[4])
   if(people[4]>max_dance):
        max_dance=people [4]
print('максимальное количество часов посещений',max_dance)

#  поиск минимального посещения танцев
min_dance =max_dance
for people in peoples_list:
    if (people[4]<min_dance):
       min_dance=people[4]
print('минимальное посещения танцев', min_dance)

#минимальный возраст
min_age=100
for people in peoples_list:
    if (people[1]< min_age):
      min_age=people [1]
print('минимальный возраст',min_age)


peoples_dict={'первый':{'имя,фамилия':'Степан Марков', 'возраст' :8,'количество  музыкальных посещений':12,'количество часов прибываня в центре':63,'количество танцевальных посещений':10},'второй':
            {'имя,фамилия':'Света Беляева','возраст' :7,'количество  музыкальных посещений':5,'количество часов прибываня в центре':56,'количество танцевальных посещений':13},'третий':
            {'имя,фамилия':'Наталья Петрова','возраст' :9,'количество  музыкальных посещений':6,'количество часов прибываня в центре':25,'количество танцевальных посещений':16}}
print(people_dict)

max_age = 0
for peoples_index in peoples_dict:
    print(peoples_index)
    print(people_dict.get(peoples_index))
    print(people_dict.get(peoples_index).get("Возраст"))
    if(peoples_dict.get(people_index).get("Возраст") > max_age):
        max_age = peoples_dict.get(peoples_index).get("Возраст")
print("Максимальный возраст",max_age)