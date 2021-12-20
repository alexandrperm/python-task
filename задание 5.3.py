
# Сделать нечёткое сравнение элементов

peoples_list = [['Степан', 8, 12, 63, 10], ['Степаа', 7, 5, 56, 13], ['Наталья Петрова', 9, 6, 25, 16]]
print(peoples_list)

def compare(S1,S2):
    print(S1)
    print(S2)
    ngrams = [
        S1[i:i+3] for i in range(len(S1))

    ]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count/max(len(S1),len(S2))

#сравним похожесть имен
x = compare(peoples_list[0][0], peoples_list[1][0])
print("Похожеcть,%:",x*100)