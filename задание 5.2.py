


peoples_dict2={'первый':{'имя,фамилия':'Степан Марков', 'возраст' :8,'количество  музыкальных посещений':12,'количество часов прибываня в центре':63,'количество танцевальных посещений':10},
            'второй':{'имя,фамилия':'Света Беляева','возраст' :7,'количество  музыкальных посещений':5,'количество часов прибываня в центре':56,'количество танцевальных посещений':13},
            'третий':{'имя,фамилия':'Наталья Петрова','возраст' :9,'количество  музыкальных посещений':6,'количество часов прибываня в центре':25,'количество танцевальных посещений':16}}
print(peoples_dict2)


def find_max_age (z):
    max_age = 0
    for peoples_index in z:
        print(peoples_index)
        print(z.get(peoples_index))
        print(z.get(peoples_index).get("возраст"))
        if (z.get(peoples_index).get("возраст") > max_age):
            max_age = z.get(peoples_index).get("возраст")
    return max_age

x = find_max_age(peoples_dict2)
print("Максимальный возраст",x)
def find_max_vizit (q):
     max_vizit = 0
     for peoples_index in q:
         print(peoples_index)
         print(q.get(peoples_index))
         print(q.get(peoples_index).get("количество часов прибываня в центре"))
         if (q.get(peoples_index).get("количество часов прибываня в центре") > max_vizit):
             max_vizit = q.get(peoples_index).get("количество часов прибываня в центре")
     return max_vizit
x = find_max_vizit(peoples_dict2)
print("количество часов прибываня в центре",x)