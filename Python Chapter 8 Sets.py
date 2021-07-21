##                        SETS
#                       ========

#=============================================================================


# sets are unordered collection of unique items.

##s = {1,2,3,2}
##print(s)
##O/P==> {1, 2, 3}
# Removes the duplicate values.

# no indexing
# Removes duplicates

# 1]

##s = {1,2,3,4,5,5,5,6,7,7,8}
##s2 = set(s)
##print(s)
##O/P==> {1, 2, 3, 4, 5, 6, 7, 8}


# 2]

##s = {1,2,3,4,5,5,5,6,7,7,8}
##S2 = list(set(s))
##print(s2)
##O/P==> [1, 2, 3, 4, 5, 6, 7, 8]

# 3]

##s={1,2,3}
##s.add(4)
##print(s)
##O/P==> {1, 2, 3, 4}

# 4]

##s={1,2,3}
##s.add(4)
##s.add(5)
##s.add(4)
##print(s)
##O/P==> {1, 2, 3, 4, 5}

# 5]

##s={1,2,3}
##s.remove(3)
##print(s)
##O/P==> {1, 2}

# 6]

##s={1,2,3}
##s.discard(3)
##print(s)
##O/P==>{1, 2}

# 7]

##s={1,2,3}
##s.clear()
##print(s)
##O/P==> set()

# 8]

##s = {1,2,3}
##s1 = s.copy()
##print(s1)
##O/P==>{1, 2, 3}

#=========================================================================



# Q] What can we store in set
#    we can't store list,dictionar and tuple


## ==> But we can store floating number,string,integer


#==========================================================================

##  in keyword in set and for loop


# 1]

##s = {'a','b','c'}
##
##if 'a' in s:
##    print('present')
##else:
##    print('not present')
##O/P==> present

# 2]

##s = {'a','b','c'}
##
##for i in s:
##    print(i)
##O/P==> {'a','b','c'}


#=============================================================================


# If we have list in that we have same value or duplicate value in list we can
#  remove it using set


##l = [1,2,3,4,5,6,6,100,1000,1000,1000]
##print(set(l))
##O/P==> {1, 2, 3, 4, 5, 6, 100, 1000}

#============================================================================


## SET MATH:
#===========

##s1 = {1,2,3,4}
##s2 = {3,4,5,6}

# i] union os s1 and s2

##union_set = s1 | s2
##print(union_set)
##O/P==> {1, 2, 3, 4, 5, 6}

# ii] Intesection of s1 & s2

##intersection = s1 & s2
##print(intersection)
##O/P==> {3, 4}

#=============================================================================

##                       END OF SET
#                       ============








