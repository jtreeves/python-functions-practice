def odd_range(end):
    array = []
    for i in range(1, end, 2):
        array.append(i)
    return array

print(odd_range(32))