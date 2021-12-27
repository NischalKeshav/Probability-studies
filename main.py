import random
import statistics
import time
list = []
value = 0
avalue = 0
hypt = 0
null = 0
a = 0
b = 0
print (' ')
time.sleep(3)
equal = 0
mode = 0
average = 0
z = 1000
for v in range(z):
    value = random.randint(0, 1)
    if value == 0:
        a = a + 1
    else:
        b = b + 1
    list.append(value)
    average = average + value
    for x in range(9):
        value = random.randint(0, 1)
        list.append(value)
        average = average + value
        if value == 0:
            a = a + 1
        else:
            b = b + 1
    if a == b:
        mode = 'v'
        equal = equal + 1
    elif a > b:
        mode = 0
    elif b > a:
        mode = 1

    if list[0] == mode:
        hypt = hypt + 1
    elif mode == 'v':
        mode = 0
    else:
        null = null + 1
    print(list)
    list = []
print(hypt)
print(equal)
print(null)
if (hypt + equal + null) != z:
    print('NO')
else:
    if hypt > null:
        print('True')
    else:
        print('False ')
print(average /( z *10))
