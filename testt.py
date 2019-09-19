

#a = ['spam', 'eggs', 100, 1234] #list

#b = ("apple", "banana", "cherry") #tuple

#c= {"name" : "John", "age" : 36} #dict

#d = {"apple", "banana", "cherry"} #set

#e = frozenset({"apple", "banana", "cherry"}) # a frozen set

#x = str("Hello World")	                 #str	
#x = int(20)	                              #int	
#x = float(20.5)	                         #float	
#x = complex(1j)	                          #complex	
#x = list(("apple", "banana", "cherry"))	  #list	
#x = tuple(("apple", "banana", "cherry"))	#tuple	
#x = range(6)	                            #range	
#x = dict(name="John", age=36)	             #dict	
#x = set(("apple", "banana", "cherry"))       #	set	
# x = frozenset(("apple", "banana", "cherry"))

#print(a)
#print(a[1])
#print(len(a))
def comment():
    hisset = {"apple", "banana", "cherry"}

    for x in thisset:
        print(x)

    thisset.add("orange")
    print(thisset)
    thisset.update(["orange", "mango", "grapes"])

    thisset.clear()

    print(thisset)

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print()

    for x in thisdict:      #print the names in dict
        print(x)

    print()
    for x in thisdict:          #print the values
        print(thisdict[x])


    #copy a dict
    samedict= dict(thisdict)
    print(samedict)
    print()

    samedict["color"] = "red" # adding to a dict
    print(samedict)

    #nested dict
    child1 = {
    "name" : "Emil",
    "year" : 2004
    }
    child2 = {
    "name" : "Tobias",
    "year" : 2007
    }
    child3 = {
        "name" : "Linus",
        "year" : 2011
    }

    myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }

    #using while statements
    i = 1
    while i < 8:
        if (i % 2) == 1:
            print(i)
        i += 1

    #nested for loop   
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

    #using functions in python
    # 
    #  
def my_function1():
    print("Hello from a function")

my_function1()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

