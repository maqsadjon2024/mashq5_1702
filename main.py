#33
def birlashtir(a, b):
    return a + b

print(birlashtir([1,2],[3,4]))

#34
def invert_dict(d):
    new = {}
    for k,v in d.items():
        new[v] = k
    return new

print(invert_dict({"a":1,"b":2}))

#35
def rimmi(text):
    return all(c in "IVX" for c in text)

print(rimmi("XIV"))

#36
import random
import string

def parol_yarat(uzunlik=8):
    belgilar = string.ascii_letters + string.digits
    return ''.join(random.choice(belgilar) for _ in range(uzunlik))

print(parol_yarat())

#37
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%15==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)

#38
def kvadratlar(lst):
    return [x*x for x in lst]

print(kvadratlar([1,2,3,4]))

#39
def boshmi(text):
    return text.strip() == ""

print(boshmi("   "))

#40
def tel_format(num):
    return "+998 ("+num[0:2]+") "+num[2:5]+"-"+num[5:7]+"-"+num[7:9]

print(tel_format("901234567"))
