def quick_sort(arr):
    return arr if len(arr) <= 1 else quick_sort([i for i in arr if i < arr[len(arr)//2]]) + [i for i in arr if i == arr[len(arr)//2]] + quick_sort([i for i in arr if i > arr[len(arr)//2]])

def quick_sort2(arr):
    return arr and quick_sort2([i for i in arr if i < arr[len(arr)//2]]) + [i for i in arr if i == arr[len(arr)//2]] + quick_sort2([i for i in arr if i > arr[len(arr)//2]])


def partition(arr, low, high):
    i = low  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)

print(quick_sort([2,1,4,3,5]))
