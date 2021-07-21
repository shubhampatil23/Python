##CHAPTER 4 :==> FUNCTIONS:
#==========================    

##Python provides the def keyword to define the function.
##The syntax of the define function is given below.

## BASIC CODE FORMAT:
#====================

##def my_function(parameters):  
##      function_block  
##return expression  
#========================================================================


## Let's see some examples:
#-------------------------

# 1]

##def add_two(num1,num2):
##    return num1 + num2
##
##print(add_two(5,10))
##O/P==> 15

#2]

##def add_two(num1,num2):
##    return num1 + num2
##
##
##a = int(input('enter first number:'))
##b = int(input('enter second number:'))
##print(add_two(5,4))
##O/P==> 9

# 3]

##first_name = input('enter your first name:')
##last_name = input('enter your second name:')
##
##def full_name(first_name,last_name):
##    return first_name + last_name
##
##print(full_name(first_name,last_name))
##O/P==> shubhampatil

#========================================================================

## PRINT vs RETURN :
#=====================

# ==>> RETURN is the best fit in define function code.Bcoz,in real life work
#      RETURN will do best work then PRINT

#============================================================================

## FUNCTION PRACTICE:
#====================

## Q]-> Define one function as one parameter and Rteurn Last Character.

## ANS:
#======

# 1]

##def Last_character(name):
##    return name[-1]
##
##print(Last_character('shubham'))
##O/P==> m

# 2]

##a = input('enter your name:')
##
##def Last_character(a):
##    return a[-1]
##
##print(Last_character(a))
##O/P==> enter your name:shubham
##       m

#=============================================================================

## Q]--> Define a function in such a way that we will come to know the number
##       is OOD or EVEN

# 1]

##def odd_even(num):
##    if num%2==0:
##        return 'even'
##    else:
##        return 'odd'
##
##print(odd_even(10))
##O/P==> even

# 2]

##def odd_even(num):
##    if num%2==0:
##        return 'even'
##    else:
##        return 'odd'
##
##print(odd_even(11))
##O/P==> odd

# 3]

##def odd_even(num):
##    return num%2==0
##
##print(odd_even(23))
##O/P==> odd

#=============================================================================

## EMPTY FUNCTION: This function is empty we get o/p which we will return or
#================= print.

##def song():
##    return 'happy bday'
##
##print(song())
##O/P==> 'happy bday'

#============================================================================

## EXERCISE:
#============

# Q]--> Ask user to input 2 number and compare which number is big

# 1]

##num1 = int(input('enter your number'))
##num2 = int(input('enter your number'))
##
##def big_number(num1,num2):
##    if num1>num2:
##        return num1
##    else:
##        return num2
##
##print(big_number(num1,num2))
##O/P==> enter your number5000
##       enter your number10000
##       10000

# 2]

##def greater(a,b):
##    if a>b:
##        return a
##    return b
##
##a = int(input('enter your number:'))
##b = int(input('enter your number:'))
##great = greater(a,b)
##print(f'{great} is greatest')
##O/P==> enter your number:5000
##       enter your number:20000
##       20000 is greatest

#============================================================================

## DEFINE GREATEST:
#==================

##def greatest(a,b,c):
##    if a>b and a>c:
##        return a
##    elif b>a and b>c:
##        return b
##    else:
##        return c
##
##Greatest = greatest(10000,20000,30000)
##print(f'{Greatest} is the greatest number among this three number')
##O/P==> 30000 is the greatest number among this three number

#=============================================================================

## FUNCTION INSIDE FUNCTION: Just explore on internet
#============================

##def new_greater(a,b,c):
##    return greater(greater(a,b),c)
##
##print(new_greater(10,20,30))

#============================================================================

## EXRCISE:
#===========

# Q]--> Define is_palindrome function that take one word in string as input and
#       Return True if it is palindrome, else Return False
#    -> palindrome ==> wors that read some backward or forword
#  E.g--->  is_palindrome('madam')--> True => this word backwrd and frwrd is same
#           is_palindrome('naman')--> True
#           is_palindrome('horse')--> False

##ANS:
#======

# 1]

##def is_palindrome(word):
##    reverse_word = word[::-1]
##    if word == reverse_word:
##        return True
##    else:
##        return False
##
##print(is_palindrome('naman'))
##print(is_palindrome('madam'))
##print(is_palindrome('horse'))
##print(is_palindrome('shubham'))
##O/P==> True
##       True
##       False
##       False

# 2]

##def is_palindrome(word):
##    if word == word[::-1]:
##        return True
##    return False

##print(is_palindrome('naman'))
##print(is_palindrome('madam'))
##print(is_palindrome('horse'))
##print(is_palindrome('shubham'))
##O/P==> True
##       True
##       False
##       False

#=============================================================================

## FABONACCI SERIES PROGRAM: (OPTIONAL)::
#=========================================

# Fabonacci series means it add last 2 numbers and 3rd number is the addition
# of that last 2 numbers

## DEFAULT PARAMETERS:
#======================

# 1]

##def user_info(name,last_name,age=23):
##    print(f'your name is{name}')
##    print(f'your name is{last_name}')
##    print(f'your name is {age}')
##
##user_info(' shubham', ' patil')
##O/P==> your name is shubham
##       your name is patil
##       your name is 23

# 2] Below one parameter (last_name) is not having value so its a rule that 
#    parameter which is not having value should be at first palce 

##def user_info(last_name,name = 'shubham ',age=23):
##    print(f'your name is{name}')
##    print(f'your name is{last_name }')
##    print(f'your name is {age}')
##
##user_info(' patil')
##O/P==> your name is shubham
##       your name is patil
##       your name is 23

#=============================================================================

winning_number = 23
guess = 1
user_input = input('guess the number')
def game(user_input):
    if user_input == winning_number:
        print('you won!!!')
    else:
        if user_input != winning_number:
            print('wrong guess, guess again')
            guess += 1
            user_input= input('guess a number again')
        else:
            print('gues is correct')

print(guess(user_input))










































