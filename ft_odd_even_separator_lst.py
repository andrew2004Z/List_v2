def ft_odd_even_separator_lst(lst):
    a1 = []
    a2 = []
    otvet = []
    for i in lst:
        if i % 2 == 0:
            a1.append(i)
        else:
            a2.append(i)
    otvet.append(a1)
    otvet.append(a2)
    return otvet

