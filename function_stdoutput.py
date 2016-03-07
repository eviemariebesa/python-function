#!/urs/bin/env python

def Myfunc(name, age):
    print"Hi! My name is", name + " and my age is",age
    print"Hi! My name is %s and my age is %d"%(name, age)
    print"Hi! My name is {} and my age is {}".format(name, age)

Myfunc("Mary",19)
