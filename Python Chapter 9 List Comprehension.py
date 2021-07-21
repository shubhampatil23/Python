##                   List Comprehension
#                   ====================

#===========================================================================

# Q] ==> Create a list of square from 1 to 10. We can do it by 2 ways see below,

# 1st way:

##square = []
##for i in range(1,11):
##    square.append(i**2)
##print(square)
##O/P==> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 2nd way: USING LIST COMPREHENSION

##square =[i**2 for i in range(1,11)]
##print(square)
##O/P==>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## FOR NEGATIVE NUMBER:
#=======================

# 1st way:

##square = []
##for i in range(1,11):
##    square.append(-i**2)
##print(square)
##o/p==> [-1, -4, -9, -16, -25, -36, -49, -64, -81, -100]


# 2nd way:  USING LIST COMPREHENSION

##square = [-i**2 for i in range(1,11)]
##print(square)
##o/p==> [-1, -4, -9, -16, -25, -36, -49, -64, -81, -100]

#============================================================================

## SOME EXMPLES:
#===============

#NAME = ['harshit','shubham','mohit']
# ----> O/P should br  ['h','s','m']
# Get 1st letter of each string.

## 1st way

##name = ['harshit','shubham','mohit']
##new_list = []
##for i in name:
##    new_list.append(i[0])
##print(new_list)
##O/P==> ['h', 's', 'm']

## # 2nd way:  USING LIST COMPREHENSION

##name = ['harshit','shubham','mohit']
##new_list = [i[0] for i in name]
##print(new_list)
##O/P==> ['h', 's', 'm']

#============================================================================

## EXERCISE 1:
#==============

# Q]==> Define a function that take list of string O/P should be reverse of
#       list. USE LIST COMPREHENSION

##list1 = ['abc','tuv','xyz']
##new_list = [i[::-1] for i in list1]
##print(new_list)
##O/P==> ['cba', 'vut', 'zyx']

#=============================================================================

## List comprehension with ==>  if statement
#=========================

## some examples:

# O/P==> even no. in new list or in list

# 1ST WAY:

##number_list = [range(1,11)]
##new_list = []
##for i in number_list:
##    if i%2 == 0:
##        new_list.append(i)
##print(new_list)
##O/P==> [2,4,6,8,10]

# 2ND WAY:
# Task one --> print even no.
# task two print odd number

# TASK ONE:

##new_list = [i for i in range(1,11) if i%2 == 0]
##print(new_list)
##O/P==> [2,4,6,8,10]

# TASK TWO:
##new_list = [-i for i in range(1,11) if i % 2 == 0]
##print(new_list)
##O/P==> [-2, -4, -6, -8, -10]

#==========================================================================

## EXERCISE 1:
#==============

# Q]==> Define a function with input ==> [True,False [1,2,3],1,2,1.0]
# o/p should ==> ['1,'2','1.0'] in string (convert in string)

## ANS:
#======

##def string(l):
##    return [str(i) for i in l if(type(i)==int or type(i)==float)]
##
##print(string([True,False [1,2,3],1,2,1.0]))
##O/P==> ['1,'2','1.0']

#============================================================================

## LIST COMPREHENSION WITH ==> if-else
#=========================


# O/P Should be , if odd no. the print -ve no. and if even no. 
# then print square of even no.

# 1ST WAY:

##nums=[1,2,3,4,5,6,7,8,9,10]

##new_list = []
##for i in nums:
##    if i%2==0:
##        new_list.append(i**2)
##    else:
##        new_list.append(-i)
##print(new_list)
##O/P==> [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]

# 2ND WAY USING LIST COMPREHENSION:

##nums=[1,2,3,4,5,6,7,8,9,10]
##new_list = [i**2 if i%2==0 else -i if i in nums]
##print(new_list)
##O/P==> [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]

#============================================================================

## NESTED LIST WITH==> LIST COMPREHENSION
#===================

# O/P should be ====> [[1,2,3],[1,2,3],[1,2,3]]

##nested_list = [[i for i in range(1,4)] for i in range(3)]
##print(nested_list)
##O/P==> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#=============================================================================


#                     END OF LIST COMPREHENSION
#                    ===========================

#=============================================================================



















