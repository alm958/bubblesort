import random
mylist = [random.randint(0,9) for i in range(9)]
mylist = [9,8,7,6,5,4,3,2,1,0]
print mylist
unsorted_index = len(mylist)
unsorted = True
while unsorted and not(unsorted_index <= 1):
    unsorted = False
    for i in range(1,unsorted_index):
        if mylist[i-1] > mylist[i]:
            unsorted = True
            (mylist[i-1],mylist[i])=(mylist[i],mylist[i-1])
    unsorted_index -= 1
    print mylist
