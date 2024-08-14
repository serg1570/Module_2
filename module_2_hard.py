import random


def get_num1():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    code = random.choice(numbers)
    return code


def get_password(n):
    codepass = {}
    codepass.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635,
                     9: 1218273645, 10: 141923283746, 11: 11029384756, 12: 12131511124210394857,
                     13: 112211310495867, 14: 1611325212343114105968, 15: 1214114232133124115106978,
                     16: 1317115262143531341251161079, 17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911})
    password = codepass.get(n)
    return password


n = get_num1()
print('Число первого поля: -',n)

pair1 = list(range(1, n))
pair2 = list(range(1, n))
pairs = []
result = ''

for i in pair1:
    for j in pair2:
        p1 = i
        p2 = j
        if p1 >= p2:
            continue
        else:
            multuple = n % (p1 + p2)
            if multuple == 0:
                pairs.append([p1, p2])
                result = result + str(p1) + str(p2)
print("Пара чисел для второго поля: -",*pairs)
print("Пароль: -",result)
if int(result) == get_password(n):
    print("ВЫХОД ОТКРЫТ")
