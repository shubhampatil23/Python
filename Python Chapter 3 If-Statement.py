## IF - STATEMENT :
#===================

# > If condition is true the the code will run.

# for eg.

##age= int(input('enter your age'))
##if age >= 18:
##    print('your age is eligible to play')
## O/P==> enter your age20
##        your age is eligible to play

#======================================================

## Pass statement in if statement:
#==================================

# PASS statement is used inside 'if statement' bcz to keep blank statement

##a=18
##if a>18:
##    pass
##O/P==> NO ERROR

#===========================================================================

## IF-ELSE STATEMENT:
#=====================

##age = 14
##if age >=14:
##    print("you are above 14")
##else:
##    print("sorry,you can't play")
##O/P==> you are above 14

#====================================================

####   EXCERCISE :
#==================

# NESTED IF-ELSE STATEMENT:
#=============================

# Q]=> Make a variable like winning_number and assign to it
##      - Ask user to guess the no.
##      - If user gussed correctly then print "You win!!!"
##      - If user didn't gussed no. correctly then,
##           i) if user gussed lower no. then actual no. then print "too low"
##           ii)if user gussed higher no. then actual no. then print "too high"
           
## ANS:
#======

##winning_number = 30
##user = int(input("guess the winning number"))
##if user == winning_number:
##    print("You win!!!")
##else:
##    if user < winning_number:
##        print("too low")
##    else:
##        print("too high")

##O/P==> 1] guess the winning number50
#           too high
#        2] guess the winning number25
#           too low
#        3] guess the winning number30
#           You win!!!

##==========================================================

## AND,OR OPERATOR:
#===================

# Let's see how to check two condition at same time for this we use AND,OR
#operator

## AND OPERATOR:  TABLE

#### T  T  = T
#### F  T  = F
#### T  F  = F
#### F  F  = F

# OR OPERATOR:

#### T  T  = T 
#### F  T  = T
#### T  F  = T
#### F  F  = F

##====================================================================

##name ='abc'
##age = 18
##if name == 'abc' and age == 18:
##    print('condition true')
##else:
##    print('condition flase')
##O/P==> condition true

##Above mentioned two variable are true,so AND operator gives true when both the
##conditions are true

#================================================================

# 1]

##name ='abc'
##age = 18
##if name == 'abc' or age == 18:
##    print('condition true')
##else:
##    print('condition flase')
##O/P==> condition true

##Above mentioned two variable are true,so OR operator gives true when both the
##conditions are true

#2]

##name ='abc'
##age = 18
##if name == 'abcdefg' or age == 18:
##    print('condition True')
##else:
##    print('condition Flase')
#O/P==> condition true

##Above mentioned two variable, in that one varible is false and one is true,
##so OR operator gives FLASE when both the
##conditions are FLASE ,if not then we get TRUE.

#============================================================================
    
#### EXCERCISE:
#===============

## Q] Ask user's name and age
##    - if user start with ['a' or 'A'] and age is above 10 then
##    - print('you can watch coco movie')
##    - Else print('sorry can't watch coco movie')

## ANS:
#=======

##name = input('Enter your name')
##
##age = int(input('Enter your age'))
##if name[0] == 'a' or name[0] == 'A' and age >= 10:
##    print('you can watch coco movie')
##else:
##    print('sorry can\'t watch coco movie')
##O/P==> 1] Enter your nameaman
##          Enter your age15
##          you can watch coco movie
##O/P==> 2] Enter your nameshubham
##          Enter your age25
##          sorry can't watch coco movie


#====================================================================

## IF-ELIF-ELSE:
#================

#let's see example

## Q] Write code for this below statements.
## --> show ticket pricing.
##     - age 1 to 3 --> free tickets.
##     - age 4 to 10 --> 150 Rs.
##     - age 11 to 60 --> 250 Rs.
##     - age above 60--> 200 Rs.

## ANS:
#=======

# 1]

##age = int(input('enter your age'))
##if 0<age<=3:
##    print('you can watch movie free')
##elif 3<age<=10:
##    print('ticket price :150 Rs')
##elif 10<age<=60:
##    print('ticket price :250 Rs')
##else:
##    print('ticket price :200 Rs')
##O/P==>enter your age10
##      ticket price :150 Rs

# 2]

### What if age is -ve its not possible but we should konw the logic for this

##age = int(input('enter your age'))
##if age == 0 or age < 0:  --> This line for,if age is zero or -ve
##     print('you can watch movie free')
##elif 3<age<=10:
##    print('ticket price :150 Rs')
##elif 10<age<=60:
##    print('ticket price :250 Rs')
##else:
##    print('ticket price :200 Rs')
##O/P==>enter your age-5
##      you can watch movie free

#=============================================================================

## USING in KEYWORD WITH if:
#============================

##name = 'shubham patil'
##if 'a' in name:
##    print("a is present in name")
##else:
##    print("a is not present")
##O/P==> a is present in name

#========================================================

## CHECK EMPTY OR NOT:
#=====================

# 1]                            
                            
##name = "shubham"
##if name:
##    print('yes')
##else:
##    print('no')
##O/P==> yes

# 2]

##name = "" -->here if we give space then o/p will be yes  
##if name:
##    print('yes')
##else:
##    print('no')
##O/P==> no

#====================================================================

## WHILE LOOP:
#==============

##print('hello world')----. 10 times.

# 1]

##i = 1
##while i<=10:
##    print('hello world')
##    i += 1
##O/P==>hello world
##      hello world
##      hello world
##      hello world
##      hello world
##      hello world
##      hello world
##      hello world
##      hello world
##      hello world

# 2]

##i = 1
##while i<=10:
##    print(f'hello world {i}')
##    i += 1
##O/P==>   hello world 1
##         hello world 2
##         hello world 3
##         hello world 4
##         hello world 5
##         hello world 6
##         hello world 7
##         hello world 8
##         hello world 9
##         hello world 10

#===============================================================

## EXERCISE :
#=============

# Q] => 1. sum of n natural number
#       2. ask user for natural number
#       3. print total from 1 to n

## ANS:
#======

##natural_number = int(input('enter natural number'))
##
##total = 0
##i = 1
##while i <= natural_number:
##    total += i
##    i +=1
##print(total)
## O/P==> enter natural number50
##        1275

#=========================================================================

## EXERCISE :
#=============

# Q] ask user to input number conatining more than one digit e.g-1256
#    calculate 1+2+5+6 and print the O/P

## ANS:
#=======

##number=input('enter the number')
##total = 0
##i = 0
##while i < len(number):
##    total += int(number[i])
##    i += 1
##print(total)
##O/P==> enter the number1256
##       14

#=========================================================================

## EXERCISE :
#=============

# Q] ask user a name ex. shubham and print count of each words.

## ANS:
#=======

##name = input('enter your name')
##var = ""
##i = 0
##while i < len(name):
##    if name[i] not in var:
##        var += name[i]
##        print(f'{name[i]}:{name.count(name[i])}')
##        i += 1
##O/P==>enter your nameshubham
##      s:1
##      h:2
##      u:1
##      b:1

#==================================================================

##INFINITE LOOP:
#================

##i = 0
##while i<10:
##    print('hello world')
##O/P==> hello world get printed infinite time.

#==================================================================

##FOR LOOP:
#==========

## ====> Range fuction:
#-----------------------

## 1]

##for i in range(1,11):
##    print('hello world')
##O/P==>  hello world
##        hello world
##        hello world
##        hello world
##        hello world
##        hello world
##        hello world
##        hello world
##        hello world
##        hello world

## 2]

##for i in range(1,11):
##    print(f'hello world : {i}')
##O/P==> hello world : 1
##       hello world : 2
##       hello world : 3
##       hello world : 4
##       hello world : 5
##       hello world : 6
##       hello world : 7
##       hello world : 8
##       hello world : 9
##       hello world : 10


## PRINT SUM 1 to 10 :
#=======================

##total = 0
##for i in range(1,11):
##    total += i
##    
##print(total)
##O/P==> 55    

## PRINT SUM USING USER INPUT:
#=============================

##n = int(input('enter the number'))
##total = 0
##for i in range(1,n+1):
##    total += i
##
##print(total)
##O/P==> enter the number50
##       1275

#====================================================================

# Ask user number,calculate the sum of that number i.e 2367==>18

# First Way To Do:

##number=input('enter the number:')
##total=0
##
##for i in range(0,len(number)):
##    total += int(number[i])
##    
##print(total)

# Second Way To Do:

##total = 0
##number = input('enter number:')
##for i in number:
##    total += int(i)
##print(total)

#====================================================================

## Ask user to input name and O/p should be in such a way that we should get
## cout of each letter.Letters should not repeat.

##SOLTION:
#=========


##name = input('Enter your name')
##temp =" "
##for i in range(0,len(name)):
##    if name[i] not in temp:
##        temp += str(name[i])
##        print(f'{name[i]}:{name.count(name[i])}')
##O/P==> Enter your nameshubhampatil
##       s:1
##       h:2
##       u:1
##       b:1
##       a:2
##       m:1
##       p:1
##       t:1
##       i:1
##       l:1

#==========================================================

## BREAK & CONTIUNE KEYWORD:
#===========================

# Break ==> Used to exit the loop OR Stop the loop

# 1]

##for i in range(1,11):
##    if i == 5:
##        break
##    print(i)
##O/P==. 1
##       2
##       3
##       4


# 2]

##for i in range(1,11):
##    if i == 5:
##        continue
##    print(i, end=',')
##O/P==>1,2,3,4,6,7,8,9,10,

#================================================================


## EXERCISE :  Modify Number Guessing Game
#===============


##import random
##winning_number = random.randint(1,100)
##guess = 1
##number = int(input('enter your number'))
##game_over = False
##
##while not game_over:
##    if number == winning_number:
##        print(f'you win ,and gussed this number in {guess} times')
##        game_over = True
##    else:
##        if number < winning_number:
##            print('low')
##            guess += 1
##            number = int(input('guess again'))
##        else:
##            print('high')
##            guess += 1
##            number = int(input('guess again'))
##            
##O/P==> EVERY TIME O/P VARRIES
##
##       enter your number70
##       low
##       guess again90
##       high
##       guess again80
##       low
##       guess again85
##       you win ,and gussed this number in 4 times

#========================================================


## END OF CHAPTER 3  ====>           THANK YOU!!!!


#========================================================



































































































































