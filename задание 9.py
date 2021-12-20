from random import randint
qa_list=[]
# создание программы которая отвечает да или нет
# #сохнанение ответов, вопросов
while 1:
    question = input("введите вопрос")
    answer = randint(0, 1)
    found=0
    for a in qa_list:
        if question == a[0]:
            answer = a[1]
            found=1
    if answer:
        print("да")
    else:
        print("нет")
    if found == 0:
        qa_list.append([question,answer])

    print(qa_list)

