import random
def numbers():
    list_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    n = random.choice(list_)
    return n
n = numbers()
def password(n):
    dict_ = {}
    dict_.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    dict_.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968})
    dict_.update({15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089, 18: 12151811724272163631545414513612711810})
    dict_.update({19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
print(n)
pair1 = list(range(1, n))
pair2 = list(range(1,n))
pairs = []
for i in pair1:
    p1 = i
    for j in pair2:
        p2 = j
        if p1 >= p2:
            continue
        else:
            x = n % (p1 + p2)
            if x == 0:
                pairs.append([p1, p2])
                result = str(p1) + str(p2)

print(*pairs)
print(result)