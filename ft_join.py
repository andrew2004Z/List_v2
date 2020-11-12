def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_join(lst, sep=' '):
    a = ''
    for i in range(ft_len(lst) - 2):
        a += str(lst[i]) + sep 
    a += str(lst[-1])
    return a
