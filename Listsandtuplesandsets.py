#slicing lists & strings

courses = ['History', 'Math', 'Physics', 'CompSci']

courses_2 = ['Spanish', 'PhysEd']

sort1 = ['G','D','F','X','R']

nums = [1, 5, 2, 4, 3]

courses.append('Art') #adds an item to the list

courses.insert(0,'German') #insert a value to a specific place in the list

courses.extend(courses_2) #use extend when you have multiple values that you want to add to the list

courses.remove('Math') #removes item from list

popped = courses.pop() #removes last value of a list

courses.reverse #reverses items in list

sort1.sort() #sorts items alphabetically (if there's words)
sort1.sort(reverse=True) #reverses order of sorted items
nums.sort() #sorts items numerically (if there's numbers)
nums.sort(reverse=True) #reverses order of sorted items

sorted_courses = sorted(courses) #doesn't alter original list, but allows for a new list to be sorted

print(popped) # shows which one got removed
print(courses)
print(sorted_courses)
print(sort1)
print(nums)
print(courses.index('CompSci')) #find index of a specific item in a given list
print('Psych' in courses) #checks if item is contained in a given list (T/F)

for item in courses: #prints out each item in the list (item is just a variable not a key word -- you could also say "for course in courses", etc.)
    print(item)

for index, course in enumerate(courses, start=2): #gives a numbered indexed list that allows you start at a specific item
    print(index, course)

course_str = ', '.join(courses) #gives comma separated string of items (or any other thing you put in like a - or +)
print(course_str)

new_list = course_str.split (', ') #removes commas from a string of items
print(new_list)

print(min(nums)) #gives minimum value of list
print(max(nums)) #gives maximum value of list
print(sum(nums)) #gives sum of list

print(courses[0]) #lists specific course based on order

print(courses[:2]) #gives courses based on range (all of the values starting with beginning and up to but NOT including 2)
print(courses[2:]) #gives courses based on range (all of the values starting with 2 and all the way to end)

print(courses[-1]) #-1 always gives you the last item

print(len(courses)) #gives you number of courses


#lists are mutable and touples are immutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art' #by changing list 1's first value, we also change list 2's first value (mutable!)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci') #instead of square brackets -- we use parentheses
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)

#tuple_1[0] = 'Art' gives us an error because tuple does not support item assignments (immutable!)



#sets are values that are unordered and have no duplicates (membership checker)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} #uses curly brackets instead of square or parentheses
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses) #does not keep order I kept it in and changes everytime you run it -- sets do not care about order & throw away duplicates
print('Math' in cs_courses) #sets are optimized to find if items are present or not (T/F)
print(cs_courses.intersection(art_courses)) #determines what values two sets share
print(cs_courses.difference(art_courses)) #determines what values two sets don't share
print(cs_courses.union(art_courses)) #combines two sets


#create empty lists, tuples, and sets

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #this is NOT right and won't work
empty_set = set()