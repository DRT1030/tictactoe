def gnomesort(arr,n, cmp=None):
    cmp = cmp if cmp else lambda p1, p2 : p1 >= p2; index = 0
    while (index < n):
        if index == 0 or cmp(arr[index], arr[index-1]): index += 1
        else: arr[index], arr[index-1] = arr[index-1], arr[index]; index -= 1
    return arr
    
def cmpmulti(p1, p2):
    return sum(map(ord, str(p1))) >= sum(map(ord, str(p2)))
    
arr = (input("Type your stuffs (it sorts by the sum of the ascii values of the string): ")).split()
n = len(arr)
arr = list(map(str, arr))
arr = gnomesort(arr,n, cmpmulti)
print("Aftersort: " + str(arr))
