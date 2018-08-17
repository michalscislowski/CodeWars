def sum_two_smallest_numbers(numbers):
    arr = list((numbers))
    list.sort(arr)
    b = arr[0]+arr[1]
    return b
