##                 *Args
#                 =======
#============================================================================

#  *args are called as *operator

# 1]

##let's pass more argument while calling the function

##def all_total(*args):
##    total = 0
##    for i in args:
##        total += i
##    return total
##print(all_total(1,2,3,4))
##O/P==> 10

#=================================================================================

## *args with normal parameter:
#===============================

# 1]

##def multiply_nums(num1,*args):
##    multiply = 1
##    for i in args:
##        multiply *=i
##    return multiply
##print(multiply_nums(2,5,8))
##O/P==> 40    ==> 2 Belongs to num1 , and 5,8 belongs to *args

# 2]

##def multiply_nums(num1,num2,*args):
##    multiply = 1
##    for i in args:
##        multiply *=i
##    return multiply
##print(multiply_nums(48,50,5,10))
##O/P==> 50

#==========================================================================

## *ARGS AS ARGUMENT:
#====================

##def multpily_num(*args):
##    multiply = 1
##    for i in args:
##        multiply *= i
##    return multiply
##num=[1,2,3,4]
##print(multpily_num(num))
##O/P==> [1, 2, 3, 4]====> This is problem now so
#                        we should do unpacking of list so every element in
#                        list will br treated as seperate.see below

# 2]

##def multpily_num(*args):
##    multiply = 1
##    for i in args:
##        multiply *= i
##    return multiply
##num=[1,2,3,4]
##print(multpily_num(*num))
##O/P==> 24 ===> SO put * while calling the function 

#=============================================================================

## EXERCISE 1:
#=============

# ANS:
#=====


##def to_power(num,*args):
##    if args:
##        return[i**num for i in args]
##    else:
##        return "you did't pass anything"
##num=[1,2,3]
##print(to_power(3,*num))
##O/P==> [1,8,27]

#==============================================================================

##  **KWARGS (DOUBLE STAR OPERATOR):
#====================================


# Kwargs   ==> key word argument

# 1]

##def funct(**kwargs):
##    print(kwargs)
##    print(type(kwargs))
##
##print(funct(name='shubham',lat_name='patil'))
##O/P==> {'name': 'shubham', 'lat_name': 'patil'}
##<class 'dict'>

# 2]

##def funct(**kwargs):
##    for k,v in kwargs.item():
##        print(f"{k}:{v}")
##        
##funct(name="shubham")
##O/P==> {name:'shubham'}


#============================================================================

# 3]

##def funct(**kwargs):
##    for k,v in kwargs.item():
##        print(f"{k}:{v}")
##
##funct('age','name="shubham"')
##O/P==> age,{name='shubham'}

# 4]

##def funct(**kwargs):
##    for k,v in kwargs.item():
##        print(f"{k}:{v}")
##
##d = {1:4,2:10}
##print(funct(**d))
##O/P==> {1:4,2:10}

#=============================================================================

#Function with all type of parameter:(PADK)==>Parameter,*Args,Default,**Kwargs:
#=============================================================================


##def func(name,*args,last_name='patil',**kwargs):
##    print(name)
##    print(*args)
##    print(last_name)
##    print(**kwargs)
##func('shubham',1,2,3,'patil',a=1,b=2)
##O/P==>  shubham
##        1,2,3  
##        patil
##        a=1
##        b=2

##============================================================================

## Exercise :
#============

##def func(l, **kwrags):
##    if kwargs.get(reverse_str):
##        return[name[::-1].title() for name in l]
##    else:
##        return[name.title() for name in l]
##
##name=['shubham','pooja']
##print(func(name,reverse=True))
##O/P==> ['Mahbush','Ajoop']

#=========================================================================

##                      END OF ==>  *ARGS & **KWARGS
#                      ==============================

#=========================================================================






























































