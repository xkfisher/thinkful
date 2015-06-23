import sys


print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))

try:
    n=int(sys.argv[1])
except:
    n="not int"

while type(n)!=int:
    try:
        n=int(raw_input("enter the upper limit of the count"))
    except:
        print("you have entered non numeric value, try again")
        
print("Fizz buzz counting up to {0}".format(n))
for i in range (1,n+1):
    if ((i%3==0) and (i%5==0)):
        print("fizzbuzz")
    elif (i%3==0):
        print ("fizz")
    elif (i%5==0):
        print ("buzz")
    else:
        print (i)