#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() here. Check before submitting

import math
import random
from evaluator import *

universal_state = get_data()[6][:]


def new_move():
    # write here your definition. You can also define helper functions
    global universal_state
    mu = float(get_data()[5])
    # agirlik
    green = 1 / 2 * mu
    yellow = 1 / 8 * mu
    blue = 1 / 2 * (1 - mu - mu ** 2)
    purple = 2 / 5 * mu ** 2
    gray = 1 / 5 * mu ** 2
    # yonler = [0, 1, 2, 3, 4, 5, 6, 7]  #koordinat sistemine göre bakış açıları
    lst = []
    eski_koordinatlar = []  # başlangıç
    yeni_koordinat = []  # sonraki adım
    M = get_data()[0]  # row sayısı
    N = get_data()[1]  # column sayısı
    for i in universal_state:
        x = i[0][0]
        y = i[0][1]
        eski_koordinatlar.append((x, y))
        geldigi_yon = i[1]
        if geldigi_yon == 0:
            yonler = [0, 1, 2, 3, 4, 5, 6, 7]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 1:
            yonler = [1, 2, 3, 4, 5, 6, 7, 0]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 2:
            yonler = [2, 3, 4, 5, 6, 7, 0, 1]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 3:
            yonler = [3, 4, 5, 6, 7, 0, 1, 2]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 4:
            yonler = [4, 5, 6, 7, 0, 1, 2, 3]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 5:
            yonler = [5, 6, 7, 0, 1, 2, 3, 4]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 6:
            yonler = [6, 7, 0, 1, 2, 3, 4, 5]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)

        if geldigi_yon == 7:
            yonler = [7, 0, 1, 2, 3, 4, 5, 6]
            gidecegi_yon = random.choices(yonler, [green, yellow, blue, purple, gray, purple, blue, yellow])
            lst.append(gidecegi_yon)
    for i in range(0, len(lst)):
        if lst[i] == [0]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x, y + 1)) > 0 :
                yeni_koordinat.append((x, y))
                lst[i][0]=universal_state[i][1]
                continue
            elif (x,y+1) in eski_koordinatlar:
                yeni_koordinat.append((x,y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x < 0 or x >= N or y+1 < 0 or y+1 >= M:
                yeni_koordinat.append((x,y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x, y + 1))

        if lst[i] == [1]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x-1, y + 1)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x-1, y + 1) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x-1 < 0 or x-1 >= N or y + 1 < 0 or y + 1 >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x-1, y + 1))

        if lst[i] == [2]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x-1, y )) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x-1, y) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x-1 < 0 or x-1 >= N or y < 0 or y >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x-1, y))

        if lst[i] == [3]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x-1, y - 1)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x-1, y - 1) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x-1 < 0 or x-1 >= N or y - 1 < 0 or y - 1 >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x-1, y - 1))

        if lst[i] == [4]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x, y - 1)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x, y - 1) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x < 0 or x >= N or y - 1 < 0 or y - 1 >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x, y - 1))

        if lst[i] == [5]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x + 1, y - 1)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x + 1, y - 1) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x + 1 < 0 or x + 1 >= N or y - 1 < 0 or y - 1 >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x + 1, y - 1))

        if lst[i] == [6]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x + 1, y)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x + 1, y) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x + 1 < 0 or x + 1 >= N or y < 0 or y  >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x + 1, y))

        if lst[i] == [7]:
            x = eski_koordinatlar[i][0]
            y = eski_koordinatlar[i][1]
            if yeni_koordinat.count((x + 1, y + 1)) > 0:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif (x + 1, y + 1) in eski_koordinatlar:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            elif x + 1 < 0 or x + 1 >= N or y + 1 < 0 or y + 1 >= M:
                yeni_koordinat.append((x, y))
                lst[i][0] = universal_state[i][1]
                continue
            else:
                yeni_koordinat.append((x + 1, y + 1))


    for i in range(0, len(lst)):
        universal_state[i][1] = lst[i][0]
        (universal_state[i][0]) = yeni_koordinat[i]

    D = get_data()[2]  # bulaştırma eşik uzaklığı
    k = get_data()[3]  # sabit
    lamda = get_data()[4]  # sabit
    P = len(universal_state)  # insan sayisi
    mask_status = []
    infection_status = []

    for m in range(0, P):
        mask_status.append(universal_state[m][2])
        infection_status.append(universal_state[m][3])

    second_infection = infection_status[:]

    for i in range(0, P):
        for j in range(i + 1, P):
            if (infection_status[i] == 'infected') and (infection_status[j] == 'notinfected'):
                uzaklik = math.dist(yeni_koordinat[i], yeni_koordinat[j])
                if uzaklik <= D:
                    probability = min(1, k / uzaklik ** 2)
                    if mask_status[i]=='masked' and mask_status[j]=='masked':
                        probability/=lamda**2
                    if mask_status[i] == 'notmasked' and mask_status[j] == 'notmasked':
                        probability=probability
                    if mask_status[i] != mask_status[j]:
                        probability/=lamda
                    infection = random.choices(['infected', 'notinfected'], [probability, 1 - probability])
                    if infection[0]=='infected':
                        second_infection[j] = infection[0]
            if infection_status[j] == 'infected' and infection_status[i] == 'notinfected':
                uzaklik = math.dist(yeni_koordinat[i], yeni_koordinat[j])
                if uzaklik <= D:
                    probability = min(1, k / uzaklik ** 2)
                    if mask_status[i] == 'masked' and mask_status[j] == 'masked':
                        probability /= lamda ** 2
                    if mask_status[i] == 'notmasked' and mask_status[j] == 'notmasked':
                        probability = probability
                    if mask_status[i] != mask_status[j]:
                        probability /= lamda
                    infection = random.choices(['infected', 'notinfected'], [probability, 1 - probability])
                    if infection[0]=='infected':
                        second_infection[i] = infection[0]
    infection_status = second_infection [:]
    for i in range(0, P):
        universal_state[i][3] = infection_status[i]
    #print(universal_state)
    return universal_state

