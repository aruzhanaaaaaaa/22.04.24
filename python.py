def multiple (x,y):
    print(x*y)
a=multiple(4,5)
print(a)


def multiple (x,y):
    print(x*y)
    return x*y
a=multiple(4,5)
print(a)


def multiple (x,y=10):
    print(x*y)
    return x*y
a=multiple(4)
print(a)



def check_numbers(x,y):
    if x + y > 100:
        return "больше 100"
    else:
        return "меньше"


print(check_numbers(60,61))


def find_max(list1):
    return max(list1)


print("ен улкен сан:", find_max([1, 2, 3, 4, 5]))



def find_max(list1):
    max_number = list1[0]
    for a in list1:
        if a > max_number:
            max_number = a
    return max_number

print("en ulken san",find_max([1, 2, 3, 4, 5]))