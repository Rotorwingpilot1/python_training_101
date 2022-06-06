# Lone Star Development Training - Integer Data Types
# INTEGERS
# Integers are one of the data types that you will see the most. They are represented as a whole number and
# actually recognized as a whole number for any math or numerical structure. Notice that there are no
# quotes in declaring an integer. If there are quotes, it is a string and not identified as an integer.
# If it is a string and you want an integer, you need to try and cast it as an integer.

# Casting - The ability to specify a type on to a variable.

# Example1 - Result should be 23
my_int1_ex1 = 1
my_int2_ex1 = 22

my_int3_ex1 = my_int1_ex1 + my_int2_ex1

print(my_int1_ex1)
print(my_int2_ex1)
print("Result of Example 1 =",  my_int3_ex1)

# Example 2 - Casting string so result should be 3 + 7 = 10
my_string1_ex2 = "3"
my_int1_ex2 = 7
my_int2_ex2 = int(my_string1_ex2) + my_int1_ex2
print("Result of Example 2 =",  my_int2_ex2)


# Exercises
# Exercise 1 - Create two variables with integers assigned to each and they create a third variable that is var 1 and var 2
# added together.
# Do It Here!

# Exercise 2 - Lets get this to work by changing the variables so that the return value is the addition of
# exercise_int1 + exercise_int2
exercise_int1 = "7"
exercise_int2 = "21"
exercise_int3 = exercise_int1 + exercise_int2
print(exercise_int3)

# Exercise 3 -

# Exercise 4 - Lets get this to work without changing the variables exercise_int1 or exercise_int2
# Hint: try casting
# Expected result is 7 + 21 = 28
exercise_int1 = "7"
exercise_int2 = "21"
exercise_int3 = exercise_int1 + exercise_int2
print(exercise_int3)
