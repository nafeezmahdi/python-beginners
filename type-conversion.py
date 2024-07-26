# Python Type Conversion
# In programming, type conversion is the process of converting data of one type to another.

# There are two types of type conversion in Python.

# Implicit Conversion - automatic type conversion
# Explicit Conversion - manual type conversion

# ---> Implicit Conversion
num1 = 5;
num2 = 10.2;
result = num1 + num2;
print(result);

# In the above example, we have created two variables: integer_number and float_number of int and float type respectively.
# Then we added these two variables and stored the result in new_number.

# It is because Python always converts smaller data types to larger data types to avoid the loss of data.

# Note:
# We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
# Python has a solution for these types of situations which is known as Explicit Conversion.

# ---> Explicit Conversion

num1 = "55.8";
num2 = 10.2;
result = float(num1) + num2;
print(result);
