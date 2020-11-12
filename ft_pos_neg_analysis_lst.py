def ft_pos_neg_analysis_lst(lst):
    p = []
    otr = []
    null = 0
    for i in lst:
        if i > 0:
            p.append(i)
        elif i == 0:
            null += 1
        else:
            otr.append(i)
    colp = 0
    colo = 0
    maxp = 0
    minp = 10000000
    sump = 0
    sredp = 0
    maxo = -1000000
    mino = 10000000
    sumo = 0
    sredo = 0
    for i in p:
        colp += 1
        if maxp < i:
            maxp = i
        if minp > i:
            minp = i
        sump += i
    for i in otr:
        colo += 1
        if maxo < i:
            maxo = i
        if mino > i:
            mino = i
        sumo += i
    sredp = sump / colp
    sredo = sumo / colo
    print('Положительные:', "Отрицательные:", sep='\t')
    print(f"Количество чисел: {colp},", f"Количество чисел: {colo},", sep='\t')
    print(f"Максимальная цифра: {maxp},", f"Максимальная цифра: {maxo},", sep='\t')
    print(f"Минимальная цифра: {minp},", f"Минимальная цифра: {mino},", sep='\t')
    print(f"Сумма чисел: {sump},", f"Сумма чисел: {sumo},", sep='\t')
    print(f"Среднее значение: {sredp},", f"Среднее значение: {sredo},", sep='\t')
    print()
    print(f"Количество нулей: {null}")
    print()
