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

#binarySearch()

def linearSearch():
    list=[1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    n = 0

    target = int(input("What number are you searching for? "))

    for x in range(len(list)):
        if list[n] == target:
            print("Found")
            break
        else:
            n +=1

#linearSearch()

def bubbleSort():
    list2 = [7, 6, 4, 2] #List to be sorted
    listSorted = [2, 4, 6, 7] #Sorted list for comparison

    pos = 0 #Index place in index
    isSorted = False

    while isSorted == False:
        if list2[pos] > list2[pos + 1]:
            list2[pos], list2[pos + 1] = list2[pos+1], list2[pos]
            print(list2)
            pos +=1
            if list2[pos] > 3:
                pos = 0
        else:
            pos+=1

        if list2 == listSorted:
            isSorted = True

bubbleSort()


