def ft_pos_neg_separator_lst(lst):
    otr = []
    null = []
    pol = []
    for i in lst:
        if i == 0:
            null.append(i)
        elif i > 0:
            pol.append(i)
        else:
            otr.append(i)
    otvet = [otr, null, pol]
    return otvet

