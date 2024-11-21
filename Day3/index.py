# # string
# print('nikita')

# # multiline string
# print("""
# this is me, one of the beautiful girl in the world
# jsfjs
# asdf
# asdf

# """)


# firstname= 'nikita   rc'
# lastname='rc'
# print(firstname.upper())
# print(firstname.split("k"))
# print(firstname + lastname)
# print(firstname.strip())



# # fstring
# name = 'nikita '
# last= 'rc'
# print("My name is:", name, 'and my last name is', last)


# print(f'my name is {name} and my last name is {last}')



#boolean
# print(1 == int('1'))
# print(1 == '1')
# print( 1> 10)


#list is like an array in c;
# names = ['nikita', 'saman', 'aman', 'nitesh', 'rc']
# namesIndex = [0, 1, 2, 3]
# number = [1, 2, 4, 5, 6]
# mixedArray =['nikita', 1, 'saman', 2]

# for i in names:
#     print(i)

# print(names[int(len(names) /2)])

# print(names[2:-1])



# randomList = ['orange', 'apple','banana', 'graps', 'berry']
# print(randomList [:-1])


# print("my name is nikita")


# Dictonary
# lisstss = ['saman',True, 1, 3.6, {
#     "name": 'saman',
#     "age": 19,
#     "male": True
# }]

# for items in lisstss:
#     print(items)

# personInformation = {
#     "name": "nikita rc",
#     "age": 16,
#     "study": True
# }
# personInformation['name'] ='Nikita RC'
# personInformation['gender']='Female'
# print(personInformation)
# Dictonary is combination of key value pair.


# Function
def phone(balance, battery, network):
    print('call saman')
    # check balance should have battery network coverage
    
    return 'call'

# Write a function that return the length of array = [1, 2,3, 4,100, 389, 3903]
randomArray = [1, 2,3, 4,100, 389, 3903]
# def find_length_of_array (nikita):
#     print(len(nikita))
#     return'okay'

# find_length_of_array([1,2,3,45,6,7,7,7,7,7,7,7,7,7])


# last ko matra number 
# def find_last_ko_number(last):
#     print(last[-1])
    
#     return 'done'

# find_last_ko_number(randomArray)

# If else
# def check_value_is_1(value):
#     if value == 2:
#         print('value is 2')
#     elif value == 1:
#         print("value is 1")
#     else:
#         print('neither 1 nor 2')


# check_value_is_1(2)

# write a function that check weather the number is even or odd
def check_odd_or_even(value):
    if value % 2 ==0:
        print(f"The value {value} is even")
    elif value % 2 ==1:
        print("This is odd value")
    else:
        print("Neither even nor odd")   

check_odd_or_even(80)






