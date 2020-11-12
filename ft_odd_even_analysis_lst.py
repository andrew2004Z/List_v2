def ft_odd_even_analysis_lst(lst):
    colc = 0
    coln = 0
    maxn = 0
    minn = -100
    maxc = 0
    minc = -100
    sumc = 0
    sumn = 0
    for i in lst:
        if i % 2 == 0:
            colc += 1
            if i > maxc:
                maxc = i
            if i < minc:
                minc = i
            sumc += i
        elif i % 2 == 1:
            coln += 1
            if i > maxn:
                maxn = i
            if i < minn:
                minn = i
            sumn += i
    print('Анализ списка:')
    print(f'Количество четных чисел:{colc},' + '\t\t' + f'Количество нечетных чисел:{coln}')
    print(f'Максимальная четная цифра:{maxc},' + '\t\t' + f'Максимальная нечетная цифра:{maxn},')
    print(f'Минимальная четная цифра:{maxc},' + '\t\t' + f'Минимальная нечетная цифра:{maxn},')
    print(f'Сумма четных чисел:{sumc},' + '\t\t' + f'Сумма нечетных чисел:{sumn},')
    print()
