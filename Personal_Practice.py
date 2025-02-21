#Keyword Arguments
#Create a Function
def foo(x=1,y=2,z=3):return(2*x,4*y,8*z)

#Call Function
Call=foo(2,3,4)
print('Calling Function','foo' '=',Call)

#Calling Function's Arguments out of order
New_Call=foo(z=4,x=2,y=3)
print('Calling Arguments out of order = ',New_Call)

#Combining Functions with Defaults
Combo_Call=foo()
print('Combining Functions with Defaults = ',Combo_Call)

#Arguments to Function
def square(x): return (x*x)
def applier(q,x): return q(x)

#Output
print('Arguments to Function = ',applier(square,2))

#Lambda Notation
A_Lamb=(lambda x,y: 2*x + y)

#Call Lambda 
print('Lambda Notation = ',A_Lamb(3,4))

#Lambda Composition
def twice (f): return lambda x: f(f(x))

#Lambda Composition Output
Quad=twice(square)
print('Quad of',2,'=',Quad(2))

#Pass by Reference 
def Same_List(List):
    return List

#Call
MyList=['X']
Same_List(MyList)
print(MyList)

#Create Another Function (Set_List)
def Set_List(List):
    List=['A']
    return(List)

MyList=['X']
Same_List(MyList)
print(MyList)

def Add(List):
    list.append['B']
    return (List)

Add(MyList)
print(MyList)

