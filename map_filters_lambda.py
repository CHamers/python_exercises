#The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list.

def square(num):
    return num**2

myNumbers = [1,2,3,4,5]

for item in map(square,myNumbers):
    print(item)
print(list(map(square,myNumbers)))

#########################

def splicer(myString):
    if len(myString)%2 == 0:
        return 'EVEN'
    else:
        return myString[0]
    
names = ['Andy','Sally','Eve','Tony']
print(list(map(splicer,names)))
    