# Lone Star Development Training - Decimal Data Type
# DECIMAL
# Decimal's are one of the data types that you will see often.


# Many decimal numbers don’t have exact representations in binary floating-point such as 0.1.
# When using these numbers in arithmetic operations, you’ll get a result that you would not expect.
# In the following example one might expect .1+.1+.1 = .3. Lets run this and see what we actually get
decimal1 = 0.1
decimal2 = 0.1
decimal3 = 0.1
decimal_results = decimal1 + decimal2 + decimal3
print("Result for adding decimal .1 + .1 + .1 = " + str(decimal_results))
