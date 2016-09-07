import random
import time
test = [random.randint(0,9) for k in range(10)]
j = len(test)
print test
start_time = time.time()
while j > 1 :
    for i in range(1,j):
        if test[i] < test[i-1] :
            (test[i], test[i-1]) = (test[i-1], test[i])
        #print str(test)+'end of for loop'
    j -= 1
    #print str(test) +'end of while loop'
end_time = time.time()
print test
print 'sort execution time (miliseconds):'+str((end_time - start_time)*1000)
