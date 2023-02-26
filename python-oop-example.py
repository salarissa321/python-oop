'''

def mysum(*vartuple):
    

    result= 0
    for x in vartuple:
        result += x

    return result


j= mysum()
print(j)
'''













'''
def mysum(x,y):
    return x+y

k=mysum(10,20)
print(k)



mysum2= lambda x,y : x+y


k =mysum2(10,20)
print(k)
'''


#scope

'''
f= 0
print(f)    #0







def do():
    f=5     #local
    print(f)  #5


    

do()

    
print(f)   #0

'''


#data types
'''
str
list
tuple
dict
'''
'''
name= 'Salar'
age= 27

print(f"my name is {name} and i am {age} years old")
'''

'''
list ------> array 50X
'''
'''
d={'salar': 100, 'issa': 90, 'ali': 80}


for c , v in d.items():
    print(f"{c}-----{v}")
'''


'''
class Calc:
    def sum(self,x,y):
        return x+y

    def mul(self,x,y):
        return x*y



c1=Calc()
print (c1.sum(10,20))

print (c1.mul(10,20))



c2=Calc()
print (c2.sum(59,20320))

print (c2.mul(1895,20280))
'''
class Student:
    def print_mark(self,mark):
        print(mark)



salar = Student()
salar.print_mark(50)






















































































































































































































