#                    CHAPTER 5

##LIST: SYMBOL FOR LIST ---->  [ ]
#=======

# ---> List is the ordered collection of items.


#========================================================================

## SOME BASICS TO KNOW, SEE BELOW:
#===================================

# 1]

##number = [1,2,3,4,5,6,7,8]
##print(number)
##O/P==> [1, 2, 3, 4, 5, 6, 7, 8]

# 2] Let's see how access the element using INDEXING. See below

##number = [1, 2, 3, 4, 5, 6, 7, 8]
##print(number[1])
##o/p==> 2

# 3]

##word= [1,2,"word1","word2",True,False,None]
##print(word[:3])
##O/P==> [1, 2, 'word1']

# 4]

##word = [1,2,True]
##print(word[-1])
##O/P==> True

# ADD element in LIST

##mixed = [1,2,True,None,5.5]
##mixed[2] = 1000
##print(mixed)
##O/P==> [1, 2, 1000, None, 5.5]

#=============================================================================

## OTHER WAY TO ADD DATA IN LIST:  see below.
#=================================

## USING append FUNCTION keyword:
#=================================

# 1]

##fruits = ['grapes','apple']
##fruits.append('mango')
##print(fruits)
##O/P==> ['grapes', 'apple', 'mango']
# In above o/p mango is added in list.Here append element will always been
# added at last.

# 2] USING inser FUNCTION:

#-> Insert function takes two arguments that is--> insert(index, new value)
#-> Here, in mentioned index new value is stored & old value is shifted to 
#   right side.

##fruits = ['grapes','apple']
##fruits.insert(1, 'mango')
##print(fruits)
##o/p==> ['grapes', 'mango', 'apple']
# in main list apple is first index in that index we have stored mango and
# apple gets shifted to right side.

# CONCATINATION : TO ADD
# Now concatinate the two list

##fruit1 = ['mango','orange']
##fruit2 = ['grapes','apple']
##fruits_list = fruit1 + fruit2
##print(fruits_list)
##O/P==> ['mango', 'orange', 'grapes', 'apple']
# BOTH LIST ARE ADDED TOGETHER. THHIS IS CONCATIONATION.

## Use extend function

##fruit1 = ['mango','orange']
##fruit2 = ['grapes','apple']
##fruit1.extend(fruit2)
##print(fruit1)
##O/P==> ['mango', 'orange', 'grapes', 'apple']

#=======================================================================

## DELETE DATA FROM LIST:
#========================

# ==> TO Delete element from list USE pop() Method. 

## POP() --> This method automatically delete's the last element of the list.
#            We can give argument in pop method & that argument will be index

# 1] pop() method without argument.

##fruit = ['mango','orange']
##fruit.pop()
##print(fruit)
##O/P==> ['mango']

# 2] pop() method with argument.

##fruit = ['mango','orange','apple','kiwi']
##fruit.pop(2)
##print(fruit)
##O/P==> ['mango', 'orange', 'kiwi']

## 3] USE del method to delet the element from the list.
# HERE, del function with variable and argument should be in square bracket.

##fruit = ['orange','mango']
##del fruit[1]
##print(fruit)
##O/P==> ['orange']

#========================================================================

## Remove() Method:
#===================

# 1]

##fruit = ['mango','orange','apple','kiwi']
##fruit.remove('apple')
##print(fruit)
##O/P==> ['mango', 'orange', 'kiwi']

# 2]

##fruit = ['apple','mango','orange','apple','kiwi']
##fruit.remove('apple')
##print(fruit)
##O/P==> ['mango', 'orange', 'apple', 'kiwi']
# Here, two apple are there in the list,so we used remove method and it 
# removed one apple from the list.

#===========================================================================

### REVISION OF ABOVE:
#======================


# 1] --> append,extend,insert ==> used for adding the element in the list.

# 2] --> pop,del,remove ==> used for deleting/remove the element in the list.


#============================================================================

## Checking of particular element present in list or not:
#==========================================================

# 1]

##fruit = ['mango','orange','banana']
##
##if 'orange' in fruit:
##    print('orange is present')
##else:
##    print('orange is not present')
##O/P==> orange is present

#=============================================================================

## SOME MORE METHODS IN LIST:
#=============================

# 1] COUNT()

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##fruit = fruits.count('apple')
##print(fruit)
##O/P==> 2
#-> Here,count method gives the count of element we want.

#==========================================================================

# 2] SORT()

# i) sort() with no argument --> In this we have to sort the list first then
#                                we can print the o/p.

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##fruits.sort()
##print(fruits)
##O/P==> ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'peers']
# Here, sort method sort the list in ascending order a-z,i.e- a,b,c,d in
# this form. And sort has not given argument.

# ii) sort() with argument

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##fruits.sort(reverse= True)
##print(fruits)
##O/P==> ['peers', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']
# Here, sort method don't sort the list in aplhabetical order a-z,i.e- a,b,c,d 
#  but it sort in descendig order. And sort has not given argument.

#=============================================================================

## SORTED()

# 1]

##fruits = ['orange','peers','banana','kiwi','apple','banana']
##print(fruits.sorted())
##O/P==> ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'peers']
#Here, sort method sorted the list in ascending order a-z,i.e- a,b,c,d in
# this form. And sort has not given argument.

# 2]
##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##fruits.sort(reverse= True)
##print(fruits)
##O/P==> ['peers', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']
# Here, sort method don't sort the list in aplhabetical order a-z,i.e- a,b,c,d 
#  but it sort in descendig order. And sort has not given argument.

#=============================================================================

## 3] CLEAR METHOD

# CLEAR METHOD() ==> Gives O/P in empty list.

##number = [3,6,0,5,7]
##number.clear()
##print(number)
##O/P==> []

#======================================================================

## 4] COPY METHOD

# creat copy of 1st list.

##number = [3,5,1,9,10]
##number_list = number.copy()
##print(number)
##print(number_list)
##O/P==> [3, 5, 1, 9, 10]
##       [3, 5, 1, 9, 10]

#-----------------------------

## SHALLO COPY:
#===============

##a = [1,2,3]
##b = a[:]
##a.append(1000)
##print(a)
##print(b)
##O/P==> [1, 2, 3, 1000]
##       [1, 2, 3]

# Remember that change done on a will not reflect on b this is shallow copy.

#=============================================================================

## LIST COMPARISON:
#==================

# In python we use " == " & ' is '

##fruit1 = ['orange','apple','pear']
##fruit2 = ['banana','kiwi','apple','banana']
##fruit3 = ['orange','apple','pear']

##print(fruit1 == fruit3)
##O/P==> True

##print(fruit1 is fruit2)
##O/P==> False

# ' == ' CHECKS IF BOTH HAVING SAME VALUE,THEN WE GET TRUE
# ' is ' CHECKS WHETHER THIS TWO LIST IS AT SAME MEMORY PLACE OR NOT.

#============================================================================

## SPLIT METHOD:
#===============

#1]

##user_info = 'shubham 25'.split()
##print(user_info)
##O/P==> ['shubham', '25']
# Here, in above example we have space in string ,so split function replace
# that space to comma(,) and O/P is in List.

# 2]

##user_info = 'shubham,25'.split(',')
##print(user_info)
##O/P==> ['shubham', '25']
# Here, shubham and 25 are separate string now.Bcoz in split method we have
# argument as coma(,) so it splits the value in separate string which are
# present before and after the coma.

#3]

##name,age = 'shubham,25'.split(',')
##print(name)
##print(age)
##O/P==> shubham
##       25

# 4]

##name,age = input('enter your name & age :').split(',')
##print(name)
##print(age)
##O/P==> enter your name & age :shubham,25
##       shubham
##       25

#============================================================================

## JOIN(METHOD):
#================

##user_info = ['shubham','24']
##print(','.join(user_info))
##O/P==> shubham,24

#===========================================================================

## LIST vs STRING:
#==================

# string are immutable.
# list are mutable.

# 1] string

##s = 'shubham'
##s.title()
##print(s)
# O/P==> shubham --> no change on string bcz its immutable.so make it work
#        p.title() should be declared in new variable then it works.

# 2] list

##l = ['a','b','c','d']
##l.pop()
##print(l)
##O/P==> ['a','b','c'

#============================================================================

## Looping in list:
#=================

## i) for loop
#================

#1]

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##for fruit in fruits:
##    print(fruit)
##O/P==> orange
##       apple
##       peers
##       banana
##       kiwi
##       apple
##       banana

# 2]

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##for fruit in fruits:
##    print(fruit, end = ',')
##O/P==> orange,apple,peers,banana,kiwi,apple,banana,

## ii) While loop:
#====================

##fruits = ['orange','apple','peers','banana','kiwi','apple','banana']
##i = 0
##while i < len(fruits):
##    print(fruits[i])
##    i += 1
##O/P==> orange
##       apple
##       peers
##       banana
##       kiwi
##       apple
##       banana

#==============================================================================

## List inside List:
#====================

##matrix = [[1,2,3],[4,5,6],[7,8,9]]
##print(matrix[2])
##O/P==> [7, 8, 9]

# now o/p should be --> 1,2,3,4,5,6,7,8,9

##matrix = [[1,2,3],[4,5,6],[7,8,9]]
##for sublist in matrix:
##    for i in sublist:
##        print(i)
##O/P==> 1
##       2
##       3
##       4
##       5
##       6
##       7
##       8
##       9

#===========================================================================

## Acess the values:
#====================

##matrix = [[1,2,3],[4,5,6],[7,8,9]]
##print(matrix[1][1])
##O/P==> 5

##matrix = [[1,2,3],[4,5,6],[7,8,9]]
##print(matrix[2][2])
##O/P==> 9

##matrix = [[1,2,3],[4,5,6],[7,8,9]]
##print(type(matrix))
##O/P==> <class 'list'>

#===========================================================================


## Range function with list:
#============================

# there is another way to create list

##number = list(range(1,11))
##print(number)
##O/P==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## pop method:
#==============

##number = list(range(1,11))
##popped = number.pop()
##print(popped)
##O/P==> 10 --> We get the value which is pop i.e 10 is at last and value is
##              stored in popped variable.

#=============================================================================

## Index method:
#================

# --> gives umdex of particular value

##number = list(range(1,11))
##print(number.index(1))
##O/P==> 0
# Here in llist from 1 to 10, 1 is at 0th index.

##number = [1,2,3,4,5,6,7,8,9,10,1]
##print(number.index(1, 9))
##O/P==> 10
## Here, 1 is present two time in above list.It gives last one

##number = [1,2,3,4,5,6,7,8,9,10,1]
##print(number.index(5,2,6))
##O/P==> 4

#============================================================================

## Pass the list of function:
#============================

##number = [1,2,3,4,5,6,7,8,9,10]
##def negative_list(l):
##    negative = []
##    for i in l:
##        negative.append(-i)
##    return negative
##print(negative_list(number))
##O/P==> [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

#============================================================================

## EXERCISE 1:
#=============

# Q]--> Define function and in that pass a list and O/P should be square of
#       the list

## ANS:
#======

# 1]

##number = [1,2,3,4,5,6,7,8,9,10]
##def square_list(l):
##    square = []
##    for i in l:
##        square.append(i**2)
##    return square
##
##print(square_list(number))
##O/P==> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2]

##number = list(range(1,11))
##def square_list(l):
##    square = []
##    for i in l:
##        square.append(i**2)
##    return square
##
##print(square_list(number))
##O/P==> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#=============================================================================

## EXERCISE 2:
#=============

# Q]--> Define function which will take a list as argument and this function
#       will return reverse of this list.

## Ans:
#======

#

##number = [1,2,3,4]
##def reverse_list(l):
##    return l[::-1]
##
##print(reverse_list(number))
##O/P==> [4, 3, 2, 1]

#=========================================================================

## EXERCISE 3:
#=============

# Q]--> Define function that take list of word as argument and return list
#       with reverse of every element in that list
#  for e.g--> ['abc','tuv','xyz'] O/P--> ['cab','vut','zyx']

## ANS:
#======

##def reverse(l):
##    element = []
##    for i in l:
##        element.append(i[::-1])
##    return element
##
##word = ['abc','tuv','xyz']
##print(reverse(word))
##O/P==> ['cba', 'vut', 'zyx']

#============================================================================

## EXERCISE 4:
#=============

## Q]--> Define Odd & Even
#        Define function
#        input
#        list [1,2,3,4,5,6,7]
#  O/P==> [[1,3,5,7],[2,4,6]]

## ANS:
#======

##def filter_odd_even(l):
##    odd_num = []
##    even_num = []
##    for i in l:
##        if i%2 == 0:
##            even_num.append(i)
##        else:
##            odd_num.append(i)
##            output = [[odd_num],[even_num]]
##    return output
##
##number = [1,2,3,4,5,6,7]
##print(filter_odd_even(number))
##O/P==> [[[1, 3, 5, 7]], [[2, 4, 6]]]

#============================================================================


## EXERCISE 5:
#=============

## Q]--> Input --> [1,2,5,8],[1,2,7,6]
#        output --> [1,2]
# GET COMMON ELEMENT FROM INPUT

## ANS:
#======


##def common(l1,l2):
##    output = []
##    for i in l1:
##        if i in l2:
##            output.append(i)
##    return output
##
##print(common([1,2,5,8],[1,2,7,6]))
##O/=> [1, 2]

#===========================================================================

## MIN & MAX:
#============

# i]

##number = [6,60,2]
##print(min(number))
##print(max(number))
##O/P==> 2
###      60

# ii]

##number = [6,60,2]
##def greatest_diff(l):
##    return max(l) - min(l)
##
##print(greatest_diff(number))
##O/P==> 58 --> 60 - 2 = 58

#============================================================================

## EXERCISE 6:
#=============

## Q]--> Input is list , def function
#        o/p--> How many list present inside the list.

## ANS:
#======

##def sublist(l):
##    count = 0
##    for i in l:
##        if type(i) == list:
##            count += 1
##    return count
##
##mixed = [1,2,3,[1,2],[3,4]]
##print(sublist(mixed))
##O/P=> 2 ---> 2 list are present inside the list.


##==========================================================================##



#                            THANK YOU        

####======================================================================####






























































































































    


































































































































































