
# O(log n) , best: O(1)
def binary_search(array, item):
    array.sort()
    print(f"Sorted array: {array}")
    low = 0
    high = len(array)-1
    mid = 0
    while low <=high:
        mid = (high+low)//2
        if array[mid] > item:
            high = mid - 1
        elif array[mid] < item:
            low = mid + 1
        else:
            return mid


array = [2,18,1,17,5,43,98,21,342,0, -1, -5]

res = binary_search(array, 5)
print(f"Element is on index: {res}")