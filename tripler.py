def tripler(array):
    result = []
    for i in range(len(array)):
        num = array[i]
        result.append(num * 3)
    return result

print(tripler([1,2,3,4,5]))