def ft_rmstrchar(str1, less):
    a = ''
    for i in str1:
        if i not in less:
            a += i
    return a