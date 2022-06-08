# Lone Star Development Training - String Data Types
# STRINGS
# Strings are one of the data types that you will see the most. Strings can be created in multiple ways within
# Python. You can use single, double or triple quotes. Generally double quotes are used for string representation and
# single quotes are used for regular expressions, sql, or similar other needs.

# Examples
my_string1 = "Welcome to the Lone Star Development Python Training!"
my_string2 = 'Welcome to Lone Star\'s Development Python Training!'
my_string3 = "Welcome to Lone Star's Development Python Training!"
my_string4 = "Wecome to 'Lone Star'"
my_string5 = "Welcome to \"Lone Star\""
my_string6 = """This is a multi-line string so that it can
                span over several lines in the IDE."""
my_string7 = "This is a string that is going to wrap if it is oversized. This is different than a " \
             "multi-line string in the fact that it can keep on going and going till it is not readable."

# Print each of the string examples above
print(my_string1)
print(my_string2)
print(my_string3)
print (my_string4)
print (my_string5)
print (my_string6)
print (my_string7)


# Exercises
# Exercise 1
# Lets create a string that displays 'Hello <your name here>', assign it to my_name1 variable and print it out
# Do It Here!

# Exercise 2
# Lets create a string that displays "Hello "<your name here>"" without escape characters, assign it to
# my_name2 variable and print it out
# Do It Here!

# Exercise 3
# Lets create a string that displays 'Hello "<your name here>"' with escape characters, assign it to
# my_name3 variable and print it out
# Do It Here!


# STRING CONCATENATION
# STRING CONCATENATION is the operation of joining two or more strings together to form a larger string
# Variables for the examples
string_concat1 = "Hello my name is "
string_concat2 = "Brandon"

# Example 1 concatenation using the "+" operator
string_concat_result1 = string_concat1 + string_concat2
string_concat_result2 = string_concat1 + ": " + string_concat2
# Should print (Hello my name is Brandon)
print(string_concat_result1)
# Should print (Hello my name is : Brandon)
print(string_concat_result2)

# Example 2 concatenation using the "%" operator
# With the "%" operator, we can insert a variable into a string.
# %s: for string.
# %d: for integer.
string_concat_result3 = "Hello my name is %s"%string_concat2
# Should print (Hello my name is Brandon)
print(string_concat_result3)

# Example 3 concatenation using the "%" operator
string_concat_result4 = "%s%s"%(string_concat1, string_concat2)
string_concat_result5 = "%s: %s"%(string_concat1, string_concat2)
# Should print (Hello my name is Brandon)
print(string_concat_result4)
# Should print (Hello my name is  : Brandon)
print(string_concat_result5)

# Example 4 concatenation using f-string (newer most modern and preferred approach)
string_concat_result6 = f"{string_concat1}{string_concat2}"
string_concat_result7 = f"{string_concat1}: {string_concat2}"
print(string_concat_result6)
print(string_concat_result7)

# Exercises
# Exercise 1
# Create the following with concatenation using the '+' operator
# Create a variable with your first and last name
# Create a variable with the name of the company you work for
# Create a concatenated string that includes the two variables (name, company) that results in the following
# string 'Hello, I am <name> and I work for <company>!'
# Print out the results of the string you concatenated.

# Exercise 2
# Create the following with concatenation using the '%' operator
# Create a variable with your first name
# Create a variable with the name of your position at Lone Star
# Create a concatenated string that includes the two variables (name, position) that results in the following
# string 'Hello, I am <name> and I work at Lone Star as a <position>!'
# Print out the results of the string you concatenated.

# Exercise 3
# Create the following with concatenation using f-string
# Create a variable with your first name
# Create a variable with your last name
# Create a variable with the name of your position at Lone Star
# Create a concatenated string that includes the three variables (first_name, last_name, position) that results in the following
# string 'Hello, I am <full name> and I work at Lone Star as a/an <position>!'
# Print out the results of the string you concatenated.