# Lone Star Development Training - Boolean Data Type
# BOOLEAN
# Boolean data type is one of the bult in data types within Python. The boolean data type
# represents one of two values, either True or False. It is usually used to represent
# truth values for expressions

# Operators
# ==  equivalent operator
# !=  not equivalent operator
# not  not operator
# or  or operator
# and  and operator

# Examples - Booleans
my_bool1 = True
my_bool2 = False
print("Examples of assigned bool values")
print(my_bool1)
print(my_bool2)


# Examples - Integers as Booleans
# TODO


# Examples - Equivalent and not Equivalent
# Assigning various int values to variables
my_int1 = 5
my_int2 = 7
my_int3 = 10
my_int4 = 12

# This code should be looking at if (my_int1)5 + (my_int2)7 == (my_int3)10
bool_result1 = (my_int1 + my_int2 == my_int3)
print("Bool Result 1 - should be looking at 5+7==10 which should return a false result")
# Below will print the result of the variable
print(bool_result1)
# Below will print the result of the expression
print(bool(my_int1 + my_int2 == my_int3))

# This code should be looking at if (my_int1)5 + (my_int2)7 != (my_int3)10
bool_result2 = (my_int1 + my_int2 != my_int3)
print("Bool Result 2 - should be looking at 5+7!=10 which should return a true result")
# Below will print the result of the variable
print(bool_result2)

# This code should be looking at if (my_int1)5 + (my_int2)7 == (my_int4)12
bool_result3 = (my_int1 + my_int2 == my_int4)
print("Bool Result 3 - should be looking at 5+7==12 which should return a true result")
# Below will print the result of the variable
print(bool_result3)

# This code should be looking at if (my_int1)5 + (my_int2)7 != (my_int4)12
bool_result4 = (my_int1 + my_int2 != my_int4)
print("Bool Result 4 - should be looking at 5+7!=12 which should return a false result")
# Below will print the result of the variable
print(bool_result4)


# Examples = IS
bool_result5 = my_int1 + my_int2 is my_int3
print("Bool Result 5 - should be looking at 5+7 is 10 which should have a false return")
print(bool_result5)

bool_result6 = my_int1 + my_int2 is my_int4
print("Bool Result 6 - should be looking at 5+7 is 12 which should have a true return")
print(bool_result5)

my_int5 = 4
my_int6 = 7
my_int7 = 11
if my_int5 + my_int6 is my_int7:
    print(str(my_int5) + "+" + str(my_int6) + "=" + str(my_int7) + "is" + " True")
else:
    print(str(my_int5) + "+" + str(my_int6) + "=" + str(my_int7) + "is" + " True")

# Exercise 1
# Take the print statements up above and lets try to create a function that will take care of that for us.

def create_string(num1, num2, num3, bool_value):
    return_string = (f"{num1} + {num2} = {num3} is {bool_value}")
    return return_string

result = create_string(my_int5, my_int6, my_int7)
print(result)

