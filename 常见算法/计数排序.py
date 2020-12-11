# 计数排序
# 基本思想：类似于有序字典计数，所以为线性时间
# 没有负数（也可以做处理，不值得）
# 复杂度 o(max(arr) + len(arr))


def counting_sort(arr):
    k = max(arr)
    counting_list = [0]*(k + 1)
    for i in arr:
        counting_list[i] += 1

    # 每个数的终点位置
    for i in range(1, k+1):
        counting_list[i] += counting_list[i-1]

    res = [0]*len(arr)
    for i in arr:
        res[counting_list[i] - 1] = i
        counting_list[i] -= 1

    return res


if __name__ == '__main__':
    print(counting_sort([1,3,2,7,6,6,2,0,0]))

