# Python allows for user input.
# That means we are able to ask the user for input.

firstName = input("Enter Your First Name : ");
lastName = input("Enter Your Last Name : ");
age = int(input("Enter Your Age : "));
fullName = firstName + " " + lastName;
print("Name : ",fullName, " Age : ",age);

# The entered value is always stored in inputString.
# We can convert an input to an integer using int().
# We can convert an input to a floating point using float().