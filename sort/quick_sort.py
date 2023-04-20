def quick_sort_bubu(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]  # 选用 start，所以下面先处理 end 一侧，且最后一步给 low 赋值。反之反过来
    # 双指针
    low, high = start, end
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]  # high 给 low，high空闲中
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]  # low 给 high，low 空闲中
        # 把中间和low交换
        arr[low] = pivot
    quick_sort_bubu(arr, start, low - 1)
    quick_sort_bubu(arr, high + 1, end)
    return arr


if __name__ == "__main__":
    lists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("排序前的序列为：", lists)
    print("排序后的序列为：")
    print(quick_sort_bubu(lists, 0, len(lists) - 1))
