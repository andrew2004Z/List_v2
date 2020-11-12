def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_sum_even_lst(lst):
    sum1 = 0
    for i in range(ft_len(lst)):
        if i % 2 == 0:
            sum1 += lst[i]
    return sum1
