def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_join(lst, sep=' '):
    a = ''
    lst1 = []
    for i in range(ft_len(lst) - 1):
        a += str(lst1[i]) + sep
    a += str(lst1[-1])
    return a
