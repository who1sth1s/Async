for i in range(5):
    print(i, end='///')
print('\n')  # return : 0///1///2///3///4///

def custom_range(end):
    i = 0
    while i < end:
        yield i
        i += 1

gen = custom_range(5)

for i in gen:
    print(i, end='//')
print('\n')  # return : 0//1//2//3//4//

rangeList = list(custom_range(5))  # return : [0, 1, 2, 3, 4]
rangeTuple = tuple(custom_range(5))  # return : (0, 1, 2, 3, 4)

rangeListGen = list(gen)  # return : []
rangeTupleGen = tuple(gen)  # return : ()

print(rangeList)
print(rangeTuple)

print(rangeListGen)
print(rangeTupleGen)