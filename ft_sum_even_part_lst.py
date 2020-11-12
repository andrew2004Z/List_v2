def ft_sum_even_part_lst(lst):
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    return s
