
if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is



#Boolean operations: and, or, not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')


if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b) #is comparsion checks whether the IDs are the same while '==' checks if values are the same


#False Values:
    #False
    #None
    #Zero of any numeric type
    #Any empty sequence - ex. '', (), []
    #Any empty mapping - ex. {}

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')