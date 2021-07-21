##               DICTIONARY
#               =============
#=========================================================================

# In dictionary we use curely bracket --> {}
# {key:value}

# 1]

##user = {'name':'shubham','age':25}
##print(user)
##O/P==> {'name': 'shubham', 'age': 25}


# 2]

##user = dict('name'='shubham',age=25)
##print(user)
##O/P==> {'name': 'shubham', 'age': 25}

#==========================================================================

## Access the data from dictionary:
#===================================

# There is no indexing bcoz of unordered collection of data.

# 1]

##user = {'name': 'shubham', 'age': 25}
##print(user['name'])
##print(user['age'])
##O/P==> shubham
##       25

#=========================================================================

# Which type of data in dictionary cab store?
# We can store anything like numbers,list,& dict inside the dict.

# 1]

##user = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##print(user[fav_movies])
##O/P==> ['coco','kiwi no na wa']

#============================================================================

## ADD DATA IN EMPTY DICTIONARY:
#================================

##user = {}
##user['name']='shubham'
##user['salary']=100000
##print(user)
##O/P==> {'name': 'shubham', 'salary': 100000}

#===========================================================================

## Looping and in keyword:
#=========================

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}

# Q] --> i] check if key exist in dictionary:
#        ii] check if value exist in dictionary:

# i]

##if 'name' in user_info:
##    print('present')
##else:
##    print('not present')
##O/P==> present

# ii]

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##if 'shubham' in user_info:
##    print('present')
##else:
##    print('not present')
##O/P==> not present --> IT'S PRESENT BUT IT'S SHOWING NOT PRESENT.

# Now using function

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##if 'shubham' in user_info.values():
##    print('present')
##else:
##    print('not present')
##O/P==> present --> USE function while accessing the values.

#==============================================================================

## LOOP IN DICTIONARY:
#=====================

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}

# 1]

##for i in user_info:
##    print(i)
##O/P==> name
##       age
##       fav_movies
##       fav_tunes

# 2] Get values using loop:

##for i in user_info.values():
##    print(i)
##O/P==> shubham
##       25
##       ['coco', 'kiwi no na wa']
##       ['aweking', 'fairy tails']

#=============================================================================

## values method:
#================


##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##user = user_info.values()
##print(user)
##print(type(user))
##O/P==> dict_values(['shubham', 25, ['coco', 'kiwi no na wa'], ['aweking', 'fairy tails']])
##       <class 'dict_values'>

#=========================================================================

## key method:
#=============

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##user = user_info.keys()
##print(user)
##O/P==> dict_keys(['name', 'age', 'fav_movies', 'fav_tunes'])
##HERE,o/p is in tuple but keys are inside list.

#=========================================================================

## ITEMS METHOD:
#===============

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##user = user_info.items()
##print(user)
##print(type(user))
##O/P==> dict_items([('name', 'shubham'), ('age', 25), ('fav_movies', ['coco', 'kiwi no na wa']), ('fav_tunes', ['aweking', 'fairy tails'])])
##       <class 'dict_items'>
## HERE, key and values are getting in tuple form and all are inside the list
## in all we get tuple 



### WHY ITEMS METHOD IS USEFULL METHOD:
#=======================================

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}

##for i,j in user_info.items():
##    print(f'key is {i} and values is {j}')
##O/P==> key is name and values is shubham
##       key is age and values is 25
##       key is fav_movies and values is ['coco', 'kiwi no na wa']
##       key is fav_tunes and values is ['aweking', 'fairy tails']

#===========================================================================

## Add and delete data from dictionaries:
#=========================================

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##user_info['fav_song']=['song1','song2']
##print(user_info)
##O/P==> {'name': 'shubham', 'age': 25, 'fav_movies': ['coco', 'kiwi no na wa'], 'fav_tunes': ['aweking', 'fairy tails'], 'fav_song': ['song1', 'song2']}
##At last position fav_song gest added

#===========================================================================

## POP METHOD:- use to delete values using keys.
#================================================

# 1] FISRT WAY

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##user_info.pop('name')
##print(user_info)
##O/P==> {'age': 25, 'fav_movies': ['coco', 'kiwi no na wa'], 'fav_tunes': ['aweking', 'fairy tails']}
##name key and values get's delete.

# 2] SECOND WAY

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##popped = user_info.pop('name')
##print(popped)
##O/P==> shubham
##we have creted one variable pooped in that POPPED variable the pop value is
##  stored

#==============================================================================

##POPITEM METHOD:
#=================    

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##poped_item = user_info.popitem()
##print(poped_item)
##O/P==> ('fav_tunes', ['aweking', 'fairy tails'])
##HERE,popitem randomly picks the key and value and it delet it's key and value
##NO argumrt in paramthesis.

#===============================================================================

## UPDATE METHOD:
#=================

##user_info = {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'], 'fav_tunes':['aweking','fairy tails']}
##more_info = {'state':'maharashtra'}
##user_info.update(more_info)
##print(user_info)
##O/P==> {'name': 'shubham', 'age': 25, 'fav_movies': ['coco', 'kiwi no na wa'], 'fav_tunes': ['aweking', 'fairy tails'], 'state': 'maharashtra'}
##here,,ORE_INFO gets added at last in dictionary.
 
## ==> if both dictionary has same key then it will update the new key in
##      new one,if there is different value in name then only it update both
##      otherwise it keeps same value in name
#============================================================================

## SOME MORE METHOD:
#=====================

# 1] ==> FROMKEYS ---> Create new dictionary

# i]

##d = dict.fromkeys(['name','age'], 'unknown') --> dict is keyword used to convert that in dictionary.
##print(d)
##O/P==> {'name': 'unknown', 'age': 'unknown'}

# ii]

##d = dict.fromkeys(range(1,11), 'OK')
##print(d)
##O/P==> {1: 'OK', 2: 'OK', 3: 'OK', 4: 'OK', 5: 'OK', 6: 'OK', 7: 'OK', 8: 'OK', 9: 'OK', 10: 'OK'}

# iii]

##d = dict.fromkeys(['name','age'], 'unknown')
##print(d)
##O/P==> {'name': 'unknown', 'age': 'unknown'}

#===========================================================================

## GET METHOD:
#==============

# 1]

##d = {'name': 'shubham', 'age': 25}
##print(d.get('name'))
##O/P==> shubham

#-> IF we give argument as 'salary' which is not in about dictionary then we
#   will not get error but we get Null which means there is nothing called as
#   'salary' in dictionary.

##--> We can use if statement in to ways:
#========================================

# i]

##d = {'name': 'shubham', 'age': 25}
##if 'name' in d:
##    print('present')
##else:
##    print('not present')
##O/P==> present

# ii]

##d = {'name': 'shubham', 'age': 25}
##if d.get('name'):
##    print('present')
##else:
##    print('not present')
##O/P==> present

#===============================================================================

## CLEAR METHOD:- Delete's all the data inside the dictionary and remains only
#===============  empty dictionary 

#=============================================================================

## COPY METHOD:
#==============

##d = {'name': 'shubham', 'age': 25}
##d1 = d.copy()
##print(d.clear())
##print(d1.get('age'))
##O/P==> None
##       25

#===========================================================================

##user = {'name': 'shubham', 'age': 25,'age': 34}
##print(user)
##O/P==> {'name': 'shubham', 'age': 34} --> same key as age and they get's
#       override.so,key which next is counted in dictionary.


#================================================================================

## EXERCISE:
#===========

# Q]-> Define function and o/p should be --> {1:1,2:8,3:27}

## ANS:
#=======

##def cube(n):
##    cube = {}
##    for i in range(1,n+1):
##        cube[i]=i**3
##    return cube
##
##print(cube(3))
##O/P==> {1: 1, 2: 8, 3: 27}

#===========================================================================

## WORD COUNT DICTIONARY:
#========================

##def counter(s):
##    count = {}
##    for char in s:
##        count[char] = s.count(char)
##    return char
##print(counter('shubham'))
##O/P==> {'S':1,'h':2,'u':1,'b':1,'a':1,'m':1}

#=============================================================================

## EXERCISE:
#===========

# Q ]-> we have to take o/p as we have taken out the o/p in that format o/p
#       should be

## ANS:
#======


##user = {}
##name = input('your name')
##age = input('your age')
##fav_movie = input('your fav movie').split(',')
##fav_song = input('your fav song').split(',')
##
##user[name] = name
##user[age] = age
##user[fav_movie] = fav_movie
##user[fav_song] = fav_song
##
##for key,value in user:
##    print(f'{keys}:{values}')
##O/P==> {'name': 'shubham', 'age': 25, 'fav_movies':['coco','kiwi no na wa'],
##        'fav_tunes':['aweking','fairy tails']}

#==============================================================================


##                 END OF DICTIONARY
#                 ===================

#==============================================================================















































































































