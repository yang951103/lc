def problem4():
    up_down_list = [0, 2, 1]
    res = [None, ]
    i = 0
    j = len(up_down_list) - 1

    def append_(i):
        if up_down_list[i] != res[-1]:
            res.append(up_down_list[i])

    while up_down_list[i] <= up_down_list[i + 1]:
        if up_down_list[i] <= up_down_list[j]:
            append_(i)
            i += 1
        else:
            append_(j)
            j -= 1
    append_(j)
    append_(i)
