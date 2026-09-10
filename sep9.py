'''

Python project --> POP / OOP --> DSA (Logic based --> pattern based --> plaform based)
POP --> Dividing he entire code into blocks
blocks --> procedures --> functions (def)
Functions --> A resualble block of code (A block of statments which perform a specific task)

Syntax:

def < funcname>(parameters):
	"""Doc String"""
	statement(s).....
	...........  #body of func
	return values(s)...
fname(args) # func call
		


#simple scnario to understand

def add(a,b):
	"""Addition function"""
	c = a+ b
	return c
print(add(4,6)) #addition
c,d = 'codegnan','python'
print(add(c,d)) #concatenation
e,f = map(str,input("enter the values").split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7])) #merging
#print(add(1,2,3,4)) #positional arguments fail



#Variable length arguments --> *args We can pass any number of positional
#arguments-->data will be stored in tuple...

def sample(*a):
    """Demo of Variable length arguments"""
    print(a)
    print(type(a)) #default it stores in tuple format
sample()
sample(2,3,4,5)
sample('codegnan',[23,4],'poll',2+5j)

marks = [20,15,25,18]
sample(marks)
sample(*marks)
*a,b,c=12,'code','poll',23,4,9
print(a)
print(b)
print(c)



def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        #print(i)
        #if type(i) in [int,float]:
        if type(i) == int or type(i) == float:
            result = result + i
    return result
print(add(2,3,4))
print(add(2,'codegnan',3,4))


#keyword arguments -->we can pass the name for the arguments
def batch(name,age,place="Vizag"):
#def batch(name="Saketh",age,place='Hyd'): #error ->non default always follows default arguments
    """Keyword arguments usage"""
    print(f'{name} is in {place} and age is {age} years')
batch('Codegnan',1,'Vizag')
batch(place='Vizag',name='Codegnan',age=1)
#keyword arguments only needs name matching not order
batch(name="Saketh",age=32)
#default arguments can accept a value as default


print(4,5)
print(4,5,sep=':') #here keyword arguments is sep and we are changing
#the default value for sep


#keyword variable length arguments (**kwargs) -->Any number of
#keyword arguments,data is stored in dictionary

def batch(**a):
    """Keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name="akash",age=21,place="vizag",branch="CSE")

data = {'name':['Akash','Praneeth'],
        'place':['Vizag','Rajahmundry']}
#batch(**data)
data.update({'batch':'PFS-VSP-007'})
batch(**data)

#Task : Create a function with the usage of *args & **kwargs

def fn(*a,**b):
    ....
    .....
fn(*c,**d)

'''
def fn(*a, **b):
    print("a =", a)  
    print("b =", b) 
c = [10, 20]
d = {"x": 1, "y": 2}
fn(*c, **d)











