# STRING:
#=========

# String :--> 1] It's collection of characters inside the single,Double quotes.
#---------    2] String are immutable,we can't change any character in string.

## 1] first_name = 'shubham'
##last_name = 'patil'
##full_name = first_name + ' ' + last_name
##print(full_name)
   
# WE CANNOT ADD STRING AND INTEGER BUT WE CAN CONVERT INTEGER IN STRING THEN WE CAN ADD
#-----------------------------------------------------------------------------------------

# 1]

##first_name = 'shubham'
##last_name = 'patil'

##print(first_name + 123)
##O/P ==> ERROR


#2]
##first_name = 'shubham'
##last_name = 'patil'

##print(first_name + '123')  ==> converting int in string to concatinate.
## O/P ==> shubham123

#3]

##first_name = 'shubham'
##last_name = 'patil'
##
##print(first_name + str(123))  ==> converting int in string to concatinate.
## O/P ==> shubham123

#4]

##first_name = 'shubham'
##print(first_name * 3)
##O/P ==> shubhamshubhamshubham

#================================================================================

## USER INPUT:
#=============

##  name = input('type your name')

# Now when we run the code code one window will popup and then will type
# the name using keyboard.

#=========================================================================

# 1]

##age = input('what is your age?')
##print(age)
##O/P ==> what we typr number as age is the O/P.

#----------------------------------------------------

# 2] ==> O/P should be==> your age is 25. see below the code below.

##age = input('what is your age?')
##print('your age is' + (age))

#NOTE:--> Input function will take input in string.

#========================================================================

## int() Function:
#==================

# Q] Ask user to input 2 number 10 and 20 and output should be
#    the total of this 2 number. i.e--> 30
# ANS:-->

#1st WAY:
#---------

##number_one =input('enter number one')
##number_two =input('enter number two')
##
##total = number_one + number_two
##print(total)
##O/P==> 1020 --> Bcoz input function gives string.

#2nd WAY:
#---------

##number_one =int(input('enter number one')) 
##number_two =int(input('enter number two'))
##
##total = number_one + number_two
##print(total)
##O/P==> 30

#NOTE--> Input function will take input in string so to convert that string
#-----   in integer we use int() function.

#  covert integer to string ==> str(4)
#  covert string to Integer ==> int('4')
#  covert string to float   ==> float('4')

#=========================================================================

# MORE VARIABLES:
#==============

#More than one variable in one line. see below,

##name,age = 'shubham ', 25
##print('hello ' + name + 'your age is ' + str(25))
##O/P==> hello shubham your age is 25

# NOW, More variables using user input 

##name,age = input('enter your name & age').split()

# O/P should be shubham and 25 but both on new line

##print(name)
##print(age)
##O/P==> enter your name & ageshubham 25
##       shubham
##       25

#NOTE: When we use split() and there is no argument in paranthesis then
#      after entering the name give space then type age.

#========================================================================

# STRING FORMATING:
#==================

##name = 'shubham '
##age = 25

#  1]

##print('hi '+name+'your age is '+str(age))
##O/P==>  hi shubham your age is 25

# 2]

##print('hi %s your age is %d'%(name,age))
##O/P==>  hi shubham your age is 25

# 3]

##print(f'hi {name} your age is{age}')
##O/P==>  hi shubham your age is 25

# 4]

##print('hi {} your age is {}'.format(name,age))
##O/P==>  hi shubham your age is 25


#===========================================================

#Exercise 1
#==========

#Q] Ask user to input 3 numbers and you have to print average of three
#   number using string formatting.Try to take all 3 number in comma
#   seperated input

# ANS:==>

# 1'st way of doing
#--------------------

##num1 = input('enter your first number')
##num2 = input('enter your second number')
##num3 = input('enter your third number')
##
##print(f'average of 3 number is:{int(num1)+ int(num2)+ int(num3)/3}')
##O/P==> Get's the average of 3 number is: --

# 2nd way of doing
#------------------

##num1,num2,num3 = input('enter your three number').split(',')
##
##print(f'average of three number is:{int(num1)+int(num2)+int(num3)/3} ')
##O/P==> enter your three number10,20,30
##      average of three number is:40.0

#========================================================================

## STRING INDEXING / SLICING : Use always square barcket for slicing/indexing.
#=============================

#syntax for slicing ==> [star:end:step]

##language = 'python'

#python is string here,bocz it's in quotes.
#+ve poition of :--> p=0,y=1,t=2,h=3,o=4,n=5.      
#-ve position of:--> p=-6,y=-5,t=4,h=-3,o=-2,n=-1.


##print(language[:])
##O/P==> python --> no start and no end given so it print the string as it is.

##print(language[0:])
##O/P==> python ---> starting for 0th position to end position of string.

##print(language[0:5])
##O/P==>  pytho --> here starts from 0th position and end at 4th position 

##print(language[-1])
##O/P==>  n

##print(language[-1:])
##O/P==> n --> starts at -1 and ends at -1 only.Always remember to flow from
##          right to left side of string.After n nothing is there so o/p is n

##print(language[-3:6])
##O/P==>  hon --> go from right to left side.

#============================================================================

## STEP ARGUMENT:
#================

##Syntax ==> [start:end:step]
# here step means at what difference the number should be printed OR
# its the difference of number.


##language = 'python'

##print(language[0:5:2])
##O/P==> pto  --> every letter with difference of 2 get printed 

##print(language[5::-1])
##O/P==> nohtyp  --> gets reverse of string as output.

##print(language[-1::-1])
##O/P==> O/P==> nohtyp  

#======================================================================

##EXERCISE:

## Q] Ask user name and print user name in reverse order.

# ANS:
#=====

##name =input('enter your name')
##print(f'The reverse of user name is:{name[::-1]}')
##O/P==> enter your nameshubham
##       The reverse of user name is:mahbuhs

#====================================================================


# STRING OPERATORS:
#==================

#  +   ==> known as concatination operator,use to join string.

#  *   ==> know as repetition operator.

#  []  ==> slice operator.

#  [:] ==> Range slice operator.

#  %   ==> used to perform string formating.

#  r   ==> used to get Raw string.

# in   ==> membership operator
  
# not in   ==> membership operator

##==================================================================


# STRING FORMATING: part 2
#===================

# 1] Using Triple Quotes:
 
##print("""they said,what's there""")
##O/P==> they said,what's there

# 2] Escaping single Quotes:

##print('they said,"what\'s going on?"')
##O/P==> they said,"what's going on?" --> no single quotes now.

# 3] Using ({}) curly brackets:

##print("{} and {} both are good".format('sachin','Dhoni'))
##O/P==> sachin and Dhoni both are good --> get placed in curly bracket.

# 4] Positional Argument:
#                                             0        1
##print("{1} and {0} both are good".format('sachin','Dhoni'))
##O/P==> Dhoni and sachin both are good

# AT 0th position there is sachin and on 1st position dhoni is there.

# 5] Keyword argument:

##print("{a},{b},{c}".format(a='james',b='harry',c='ricky'))
##O/P==> james,harry,ricky

#============================================================================

## STRING FORMATTING USING % OPERATOR:
#======================================

##Integer = 10
##Float = 10.20
##String = 'python'
##
##print('I am integer,my value is %d\n I am float, my value is %f\n I am string,my value is %s'%(Integer,Float,String))
##O/P==> I am integer,my value is 10
##       I am float, my value is 10.200000
##       I am string,my value is python

#=========================================================================

##EXERCISE:
#===========

# Q]  Take two comma seperated input from user
#          1] user name
#          2] single character

#   O/P should be ==> 1] User's name length.
#                     2] count the character of that user will input.

# ANS:
#=====

##name,char = input('enter name and char').split(',')
##print(f'legth of user is:{len(name)}')
##print(f'character count is:{name.lower().count(char.lower())}')
##O/P==> enter name and charshubham,h
##       legth of user is:7
##       character count is:2


#=====================================================================

## strip method:
#================

##name = '    shubham    ' 
##dots = '................'

# 1] strip = It removes both sides spaces.

##print(name.strip()+dots)
##O/P==> shubham................

# 2] lstrip = Remove left side space

##print(name.lstrip()+dots)
##O/P==> shubham    ................

# 3] rstrip = Remove right side space

##print(name.rstrip()+dots)
##O/P==>     shubham................

#====================================================================


## REPLACE METHOD():
#====================

# SYNTAX==> replace(want to replace,put new value,position)

##string = 'she is beatuiful and she is good'
#now in O/P string mentioned above should not have space
##print(string.replace(' ','_'))
##O/P==> she_is_beatuiful_and_she_is_good
# Above we have replaced space with underscore(_).

##print(string.replace('is','was',1))
##O/P==> she was beatuiful and she is good
# Above 1st 'is' is replaced by was  

#=============================================================================

## FIND() METHOD: Use to find the position of word from where it starts.
#===============

##SYNTAX==> find(give word,star,end)


##string = 'she is beatuiful and she is good'
##print(string.find('is'))
##O/P==> 4    --> position of 'is' is at 4 

##string = 'she is beatuiful and she is good'
##print(string.find('is',23,31))
##O/P==> 25    --> position of 'is' is at 25 from range 23 to 31 

#===================================================================

## CENTER() METHOD:
#==================

##SYNTAX==> center(return required length of string,'put something in space')

##name = 'shubham'
##print(name.center(11,'*'))
##O/P==> **shubham**  --> space is replaced with star(*) bcoz we have rturned
##       11 lenth of string.

#=============================================================================









































































