##                      CHAPTER 6 ==> TUPLES:

#============================================================================

# Tuples are data structure
# Tuples can store any data structure.
# Tuples are immutable,once tuple is created can't update.
# For eg.
# var = ('one','two','three')
# --> Here, no append,no insert,no pop,no remove can be done.

#============================================================================

## Method can be used in tuples:
#================================

# i] count, index
# ii] len function
# iii] slicing

#============================================================================

## More about tuple:
#===================

## 1] Looping in tuple:
#=========================

##mixed = (1,2,3,4.0)
##for i in mixed:
##    print(mixed)
## O/P==> (1,2,3,4.0)

## 2] While loop:
#=================

##mixed = (1,2,3,4.0)
##while i in len(mixed):
##    print(i)
##O/P==> (1,2,3,4.0)


## 3]: TUPLE WITH ONE ELEMENT: when one element is there the give comma it 
#============================= becomes tuple.

# i]

##num = (1)
##print(type(num))
##O/P==> <class 'int'>

# ii]

##num = (1,)
##print(type(num))
##O/P==> <class 'tuple'>

## 4]: Tuple without paranthesis:
#================================

##guitar = 'yamaha','baton rouge','taylor'
##print(type(guitar))
##O/P==>  <class 'tuple'>
## Above, one variable with multiple data is TUPLE.


## 5]: Tuple Unpackig:
#=====================

##guitar = ('dhoni','virat','rohit')
##guitar1,guitar2,guitar3 = guitar
##print(guitar1)
##print(guitar2)
##print(guitar3)
##O/P==> dhoni
##       virat
##       rohit

## 6]: List inside tuple:
#=========================

##favorties = ('souther mangolia',['tokyo theme','landscape'])

# --> * When list is inside the tuple we can do pop , append on the list

# i]

##favorties[1].pop()
##print(favorties)
##O/P==> ('souther mangolia', ['tokyo theme'])

# ii]

##favorties[1].append('yes')
##print(favorties)
##O/P==> ('souther mangolia', ['tokyo theme', 'landscape', 'yes'])

##============================================================================

## Let's see some function that can ne used with tuple.
#=======================================================

# -->  MIN , MAX , SUM

# i]

##var = (1,2,3,4.0)
##print(var(min(var)))
##O/P ==> 1

# ii]

##var = (1,2,3,4.0)
##print(var(max(var)))
##O/P==> 4.0

# iiI]

##var = (1,2,3,4.0)
##print(var(sum(var)))
##O/P==> 9.0

#=============================================================================

## Functon returning two values:
#===============================

# Whenever, we do function and if we are returning two values we will get
# o/p in tuple.

# 1]

##def func(int1,int2):
##    add = int1 + int2
##    multiply = int1 * int2
##    return add,multiply
##
##print(func(2,3))
##O/P==> (5, 6) --> O/P in tuple

### --> if we want above o/p seperate for this see below;

# 2]

##def func(int1,int2):
##    add = int1 + int2
##    multiply = int1 * int2
##    return add,multiply
##
##add,multiply = func(2,3)
##print(add)
##print(multiply)
##O/P==> 5
##     6

#=============================================================================

## Something more about tuple,list,str:
#======================================

# 1]

##num = tuple(range(1,11))
##print(num)
##O/P==> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 2] Convert tuple to list and str:

# i]

##num = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
##print(num)
##O/==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ii]

##num = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
##print(num)
##O/P==> "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"


#============================================================================

#                           THANK YOU !!!

#============================================================================#



























































































