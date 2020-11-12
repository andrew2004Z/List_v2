def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_join(lst, sep1=' '):
    a = ''
    lst1 = []
    for i in range(ft_len(lst) - 1):
        a += str(lst[i]) + sep1
    a += str(lst[-1])
    return a
