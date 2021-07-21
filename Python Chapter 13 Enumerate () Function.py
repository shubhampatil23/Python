##                  ENUMERATE FUNCTION
#               ==========================

#==============================================================================

# We use enumerate function with for loop to track position of our item
# in iterable

# When we use for loop in list,tuple in that we just
# track item in it with not it's position.

# To track position we use enumerate function

#=============================================================================

## i] without enumerate function:
#=============================

##names = ['abc','abcdef','shubham']
##pos = 0
##for name in names:
##    print(f'{pos} ---> {name}')
##    pos+=1
##O/P==> 0 ---> abc
##       1 ---> abcdef
##       2 ---> shubham

## ii] with enumerate function:
#==============================

##names = ['abc','abcdef','shubham']
##
##for pos,name in enumerate(names):
##    print(f'{pos} --> {name}')
##O/P==> 0 ---> abc
##       1 ---> abcdef
##       2 ---> shubham


#===============================================================================

# Q] Define  function with 2 argument
#    1] list containing string
#    2] string that want to find in your list and this function
#       return index of string in your list and if string is not present then
#       return -1


##def find_position(l, target):
##    for pos,names in enumerate(l):
##        if names == target:
##            return position
##    return -1
##names = ['abc','abcdef']
##print(find_position(names,'shubham'))
##O/P=> 2

#==============================================================================

## MAP () FUNCTION:
#==================

##lst = [10,20,30,40,50,60]
##sq_list = list(map(lambda x = x**2,lst)
##print(sq_list)
##O/P==> [100,400,600,1600,2500,3600]

##================================================================================

## FILTER() FUNCTION: takes argument as -> defined function name & variable name.
#====================

##def is_even(a):
##    return a%2==0
##
##nums=[3,4,21,5,6,9,8,10]

# i] 1st way to do :

##even = tuple(filter(is_even,nums)) 
##print(even)
## O/P==> (4,6,8,10)

# ii] 2nd way to do :

##even = filter(lambda x = x%2 == 0,nums)
##print(even)
##O/P==> [4, 6, 8, 10]


# iii] using list comprehension:

##even = [ i for i in nums if i%2==0]
##print(even)
##O/P==> [4, 6, 8, 10]

#=============================================================================


## ZIP() FUNCTION:
#=================

##user_id = ['useer1','useer2','useer3']
##names = ['shubham','mohit','rohit']

# i]

##print(list(zip(user_id,names)))
##O/P==> [('useer1', 'shubham'), ('useer2', 'mohit'), ('useer3', 'rohit')]

# ii]

##print(dict(zip(user_id,names)))
##O/P==> {'useer1': 'shubham', 'useer2': 'mohit', 'useer3': 'rohit'}

# If we have 3 varibles we can convert it in list,tuple but not in dictionary.
# In above we have only 2 variable so we can do or convert in list,tuple
#& dictionary.


#=============================================================================

##  * Operator with zip:
#=======================

##l1 = [1,3,5,7]
##l2 = [2,4,6,8]
##
##print(list(zip(*l)))
##O/P==> [(1,2),(3,4),(5,6),(7,8)]

#===========================================================================


## when we have l then convert it in l1 and l2

##l = [(1,2),(3,4),(5,6),(7,8)]
##
##l1,l2 = list(zip(*l))
##print(l1)
####print(l2)
##O/P==> (1, 3, 5, 7)
##       (2, 4, 6, 8)

#============================================================================

## Add big number in new list


##l1 = [1,3,5,7]
##l2 = [2,4,6,8]
##new_list = []
##
##for i in zip(l1,l2):
##    new_list.append((max(i))
##                    
##print(new_list)
##O/P==> new_list = [2,4,6,8]

#==============================================================================

# EXERCISE:
#===========

# Q] ==> Define a function that takes any no. of list
#        containing no. [1,2,3],[4,5,6,],[7,8,9] return average
#        (1+4+7)/3,(2+5+8)/3,(3,6,9)/3

## ANS:
#======

##def average(*args):
##    average=[]
##    for i in zip(*args):
##        average.append(sum(i) / len(i))
##    return average
##
##print(average([1,2,3],[4,5,6,],[7,8,9]))
##O/P==> [4.0, 5.0, 6.0]

#============================================================================

## all() function:
#=================

# - all function check in our iterable all value are True or Flase
# - if all value are True it return True else return False
# - if even one value is false we get False

# 1st way

##number1=[2,4,6,8,10]
##number2=[1,2,3,4,5,6]
##even=[]
##for num in number1:
##    even.append(num%2==0)
##
##print(all([True,True,True,True,True]))
##O/P==> True

# 2nd way

#i]

##number1=[2,4,6,8,10]
##number2=[1,2,3,4,5,6]
##print(all([num%2==0 for num in number1]))
##O/P==> True

#ii]

##number1=[2,4,6,8,10]
##number2=[1,2,3,4,5,6]
##print(all([num%2==0 for num in number2]))
##O/P==> False

#==========================================================================

## any() function:
#=================

# it check thst, we have one value as true then we get true
#   i.e ==> one no. is even we get true.



##number1=[13,7,8,17]
##print(any([num%2==0 for num in number1]))
##O/P==> True  bcoz=> we have 8 as even so one value is even we get true


#===========================================================================


## HOW WE WE USE ANY & ALL FUNCTON:
#===================================






































