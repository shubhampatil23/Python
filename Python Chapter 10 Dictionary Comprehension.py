##           DICTIONARY COMPREHENSION
#          ============================


## let's see some examples:
#===========================

# O/P should be [1:1,2:4,.....10:1000] in value
# there should be square of key no.

# 1]

##square_list = {num:num**2 for num in range(1,11)}
##print(square_list)
##O/P==> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# 2]

##Square_list = {f"square of {num} is":num**2 for num in range(1,11)}
##for k,v in square.items():
##    print(square_list)


#============================================================================

## O/P should be , how many times character are present count that characters.

##string = ["shubham"]
##word_count = {char:string.count(char) for char in string}
##print(word_count)
##O/P==> {s:1,h:2,u:1,b:1,a:1,m:1}

#============================================================================

## DICTIONARY COMPREHENSION WITH  ==> if-else
#================================


# O/P should be {1:odd,2:even,3:odd,4:even........10:even}

##odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
##print(odd_even)
##O/P==> {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even',
##        7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

#==============================================================================

#                       END OF DICTIONARY COMPREHENSION
#                      =================================


#=============================================================================









