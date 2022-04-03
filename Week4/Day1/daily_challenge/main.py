a = input("Enter a string")

if len(a) < 10:
    print("string not long enough")
elif len(a) > 10:
    print("string too long")

print(a[0])
print(a[0:2])
print(a[0:3])
print(a[0:4])
print(a[0:5])
print(a[0:6])
print(a[0:7])
print(a[0:8])
print(a[0:9])
print(a[0:10])
print(a[0:11])

import random
print(''.join(random.sample(a,len(a))))


