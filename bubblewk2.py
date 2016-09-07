import random
mylist = [random.randint(0,9) for i in range(9)]
mylist = [9,8,7,6,5,4,3,2,1]
print mylist
unsorted_index = len(mylist)
swap = True
while swap:
    swap = False
    for i in range(1,unsorted_index):
        if mylist[i-1] > mylist[i]:
            swap = True
            (mylist[i-1],mylist[i])=(mylist[i],mylist[i-1])
    unsorted_index -= 1
    print mylist

mylist = [9,8,7,6,5,4,3,2,1]
print 'bubble_sort'
print mylist
count = 0
swapped = True
while swapped == True:
    swapped = False
    num_elements = len(mylist) - count - 1
    for i in range(num_elements):
        if mylist[i] > mylist[i+1]:
            temp = mylist[i]
            mylist[i] = mylist[i + 1]
            mylist[i + 1] = temp
            swapped = True
    print mylist
