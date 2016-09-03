import random
import time
test = []
for k in range(0,100):
    test.append(int(round(random.random()*10000)))

j = len(test)
start_time = time.time()
while j > 1 :
    for i in range(1,j):
        if test[i] < test[i-1] :
            (test[i], test[i-1]) = (test[i-1], test[i])
    j -= 1
end_time = time.time()
print test
print 'sort execution time (miliseconds):'+str((end_time - start_time)*1000)
