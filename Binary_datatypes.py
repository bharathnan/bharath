#bytes datatype
#the byte datatype reperesents a group of byte numbers just like an array
#a byte number is any positive integer from 0 to 255
#it cannot store negative numbers.
elements = [55,20,0,40,15]
x=bytes(elements)
print(x[0])
for i in x: print(i)
#range datatype
r = range(10)
for i in r:print(i)
r1=range(30,40,2)
for i in r1:print(i)