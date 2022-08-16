def fibon():
    n1 = 0
    n2 = 1
    sum = 0

    if n1 <= 0:
        print ("number should be higher than 0 ")
    elif n1 == 1:
        print ("0")
    elif n1 == 2:
        print ("1")
    for x in range(2, 29):
        sum = n1 + n2
        n1 = n2
        n2 = sum
        print(sum)

#fibon()

def binarySearch():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Must be sorted
    n = 0

    checkInt = int(input("What number do you want to check for? "))

    median = len(list) / 2
    print (int(median))

    if median == checkInt:
        print ("Integer found")
    elif median > checkInt:
        for x in range(int(median-1)):
            if list[n] == checkInt:
                print("Found")
                break
            else:
                n += 1
    elif median < checkInt:
        for i in range(int(median-1)):
            if list[int(median+1)] == checkInt:
                print("Found")
                break
            else:
                median+=1

binarySearch()


    #for x in range(len(list)):
