##       Lambda Expresion (Anonymous Function):
#       ========================================

#==========================================================================

# 1]

##def add(a,b):
##    return a+b

# i]

##add2 = lambda a,b:a+b
##print(add2(2,3))
##O/P==> 5

#   ii]

##multiply = lambda a,b : a*b
##print(multiply(2,3))
##O/P==> 6

# LAMBDA FUNCTION HAS NO NAME

#============================================================================

# Lambda Practice:
#==================

# i]

##def is_even(a):
##    return a%2==0
##print(is_even(2))
##O/P==> True

# ii]

##def is_even(a):
##    return a%2==0
##print(is_even(5))
##O/P==> False

#=========================================================================

## USING LAMBDA EXPRESSION:
#==========================

# i]

##is_even = lambda a:a%2==0
##print(is_even(4))
##O/P==> True

# ii]

##is_even = lambda a:a%2==0
##print(is_even(5))
##O/P==> Flase

#iii]

##def last_char(s):
##    return[-1]
##
##last_char = lambda s:s[-1]
##print(last_char('shubham'))
##O/P==> m

#===========================================================================

## Lambda function with ==> is-else

# 1] 1st way:
#============

##def func(s):
##    if len(s)>5:
##        return True
##    return False
##
##func = lambda s: True if len(s)>5 else Flase
##print(func('abcdefg'))
##O/P==> True

# 2] 2nd way:
#============

##def func(s):
##    return len(s)>5
##
##func= lambda s : len(s)>5
##print(func('abcdefg'))
##O/P==> True

#===========================================================================

#                         END POF LAMBDA EXPRESSION
#                       ============================

#===========================================================================









































